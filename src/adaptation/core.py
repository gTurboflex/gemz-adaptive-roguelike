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


def validated_probabilities(probabilities):
    if len(probabilities) != 4:
        raise ValueError("Four style probabilities required")
    p = tuple(finite_nonnegative(x) for x in probabilities)
    if abs(sum(p) - 1) > 1e-6:
        raise ValueError("Probabilities must sum to one")
    return p


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
    fallback_active: bool = field(default=False, init=False)
    fallback_reason: str | None = field(default=None, init=False)

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
        if self.mode == "static" or self.fallback_active:
            self.eas = 1.0
        elif boundary:
            step = .02 * step_time
            self.eas += clamp(target - self.eas, -step, step)
            self.eas = clamp(self.eas, 1, 1.8)
        return self.eas

    def update_profile(self, probabilities, dt, *, shift=False):
        """Receive externally supplied probabilities; this method does not infer them."""
        dt = min(finite_nonnegative(dt), 5)
        p = validated_probabilities(probabilities)
        if self.mode == "static" or self.fallback_active:
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
        if not valid_result or age_seconds > 10:
            self.inference_failure(reason="invalid_result" if not valid_result else "stale_result")
        if self.mode == "static" or self.fallback_active:
            return "Neutral"
        index = max(range(4), key=self.memory.__getitem__)
        if self.memory[index] < .6 or STYLES[index] == "Mixed":
            return "Neutral"
        return STYLES[index]

    def inference_failure(self, *, reason="worker_error"):
        """Latch static fallback until a fresh result is explicitly accepted."""
        self.fallback_active = True
        self.fallback_reason = reason
        self.eas = 1.0
        self.memory = (.25,) * 4

    def recover_inference(self, probabilities, dt, *, age_seconds=0):
        """The caller supplies result age; only a valid result at most 10s old recovers."""
        age_seconds = finite_nonnegative(age_seconds)
        dt = finite_nonnegative(dt)
        p = validated_probabilities(probabilities)
        if age_seconds > 10:
            self.inference_failure(reason="stale_result")
            return False
        self.fallback_active = False
        self.fallback_reason = None
        self.update_profile(p, dt)
        return True


