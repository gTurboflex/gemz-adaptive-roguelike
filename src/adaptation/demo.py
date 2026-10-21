"""Deterministic synthetic demonstration. All probabilities are manually supplied."""
import json
from .core import Controller


def main():
    controller = Controller("Hard")
    print("SYNTHETIC INPUTS — no ML training, player data or measured performance")
    for tick in range(1, 25):
        # A known change from ranged to close combat after twelve windows.
        prediction = (.05, .85, .05, .05) if tick <= 12 else (.85, .05, .05, .05)
        controller.update_budget(.6, tick * 5, 40, 45, 5, boundary=True)
        controller.update_profile(prediction, 5, shift=tick in (13, 14))
        if tick in (1, 12, 13, 18, 24):
            print(json.dumps({"seconds":tick * 5, "eas":round(controller.eas, 3),
                              "difficulty":round(controller.difficulty, 3),
                              "memory":[round(x, 3) for x in controller.memory],
                              "specialization":controller.specialization()}))


if __name__ == "__main__":
    main()

