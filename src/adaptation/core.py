"""Reference controller only. No gameplay telemetry or trained ML model is included."""
from dataclasses import dataclass, field
from math import exp, isfinite

STYLES = ("Close", "Ranged", "Evasive", "Mixed")


def finite_nonnegative(value):
    if not isfinite(value) or value < 0:
        raise ValueError("Expected a finite nonnegative value")
    return float(value)


def clamp(value, low, high):
    return max(low, min(high, value))


def target_eas(depth, active_seconds, total_gemz, dps):
    """Initial design coefficients; not empirically tuned."""
    values = [finite_nonnegative(x) for x in (depth, active_seconds, total_gemz, dps)]
    d, seconds, gemz, damage = values
    return clamp(1 + .35 * min(d, 1) + .15 * min(seconds / 900, 1)
                 + .15 * min(gemz / 100, 1)
                 + .15 * clamp(damage / 30 - 1, 0, 1), 1, 1.8)


@dataclass
class Controller:
    starting_difficulty: str = "Easy"
    mode: str = "profile"
    eas: float = field(default=1.0, init=False)
    memory: tuple = field(default=(.25, .25, .25, .25), init=False)

    def __post_init__(self):
        if self.starting_difficulty not in ("Easy", "Hard"):
            raise ValueError("Starting difficulty must be Easy or Hard")
        if self.mode not in ("static", "rules", "profile"):
            raise ValueError("Unknown experimental mode")

    @property
    def difficulty(self):
        base = .85 if self.starting_difficulty == "Easy" else 1.15
        return clamp(base * self.eas, .75, 2.1)

    def update_budget(self, depth, active_seconds, total_gemz, dps, dt, *, boundary):
        target = target_eas(depth, active_seconds, total_gemz, dps)
        step_time = min(finite_nonnegative(dt), 5)
        if self.mode == "static":
            self.eas = 1.0
        elif boundary:
            step = .02 * step_time
            self.eas += clamp(target - self.eas, -step, step)
            self.eas = clamp(self.eas, 1, 1.8)
        return self.eas

    def update_profile(self, probabilities, dt, *, shift=False):
        """Receive externally supplied probabilities; this method does not infer them."""
        dt = min(finite_nonnegative(dt), 5)
        if len(probabilities) != 4:
            raise ValueError("Four style probabilities required")
        p = tuple(finite_nonnegative(x) for x in probabilities)
        if abs(sum(p) - 1) > 1e-6:
            raise ValueError("Probabilities must sum to one")
        if self.mode == "static":
            return self.memory
        # Low confidence removes specialized evidence rather than reinforcing it.
        target = p if max(p) >= .6 else (.25,) * 4
        rate = .015 + .035 * (self.eas - 1) / .8 + (.03 if shift else 0)
        alpha = 1 - exp(-rate * dt)
        memory = tuple((1 - alpha) * old + alpha * new
                       for old, new in zip(self.memory, target))
        # Keep normalization stable across long synthetic runs.
        self.memory = tuple(x / sum(memory) for x in memory)
        return self.memory

    def specialization(self, *, valid_result=True, age_seconds=0):
        age_seconds = finite_nonnegative(age_seconds)
        if self.mode == "static" or not valid_result or age_seconds > 10:
            return "Neutral"
        index = max(range(4), key=self.memory.__getitem__)
        if self.memory[index] < .6 or STYLES[index] == "Mixed":
            return "Neutral"
        return STYLES[index]

    def inference_failure(self):
        """Explicit static fallback in this reference model; Unity recovery is future work."""
        self.eas = 1.0
        self.memory = (.25,) * 4


