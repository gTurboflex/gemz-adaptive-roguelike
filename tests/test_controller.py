import math
import random
import unittest
from src.adaptation.core import Controller, target_eas


class ControllerContracts(unittest.TestCase):
    def test_bounds_across_extreme_progression(self):
        rng = random.Random(42)
        for difficulty in ("Easy", "Hard"):
            c = Controller(difficulty)
            for _ in range(1000):
                old = c.eas
                c.update_budget(*(rng.random() * 10000 for _ in range(4)), 5, boundary=True)
                self.assertTrue(1 <= c.eas <= 1.8)
                self.assertTrue(.75 <= c.difficulty <= 2.1)
                self.assertLessEqual(abs(c.eas-old), .100000001)

    def test_combat_does_not_change_budget(self):
        c = Controller()
        c.update_budget(1, 900, 100, 1000, 900, boundary=False)
        self.assertEqual(c.eas, 1)

    def test_long_elapsed_interval_cannot_cause_large_jump(self):
        c = Controller()
        c.update_budget(1, 900, 100, 1000, 900, boundary=True)
        self.assertAlmostEqual(c.eas, 1.1)

    def test_static_control_ignores_profile_and_progress(self):
        c = Controller("Hard", "static")
        for _ in range(100):
            c.update_budget(1, 900, 100, 1000, 5, boundary=True)
            c.update_profile((1, 0, 0, 0), 5, shift=True)
        self.assertEqual(c.eas, 1)
        self.assertEqual(c.memory, (.25,)*4)
        self.assertEqual(c.specialization(), "Neutral")

    def test_old_style_fades_after_switch(self):
        c = Controller()
        for _ in range(60):
            c.update_profile((0, 1, 0, 0), 5)
        before = c.memory[1]
        for _ in range(60):
            c.update_profile((1, 0, 0, 0), 5)
        self.assertLess(c.memory[1], before)
        self.assertGreater(c.memory[0], .95)
        self.assertAlmostEqual(sum(c.memory), 1)

    def test_shift_accelerates_turnover(self):
        slow, fast = Controller(), Controller()
        for c in (slow, fast):
            for _ in range(60):
                c.update_profile((0, 1, 0, 0), 5)
        slow.update_profile((1, 0, 0, 0), 5)
        fast.update_profile((1, 0, 0, 0), 5, shift=True)
        self.assertGreater(fast.memory[0], slow.memory[0])

    def test_low_confidence_decays_towards_neutral(self):
        c = Controller()
        for _ in range(100):
            c.update_profile((1, 0, 0, 0), 5)
        old = c.memory[0]
        c.update_profile((.3, .3, .2, .2), 5)
        self.assertLess(c.memory[0], old)

    def test_stale_or_invalid_inference_has_neutral_tactics(self):
        c = Controller()
        for _ in range(100):
            c.update_profile((1, 0, 0, 0), 5)
        self.assertEqual(c.specialization(), "Close")
        self.assertEqual(c.specialization(age_seconds=11), "Neutral")
        self.assertEqual(c.specialization(valid_result=False), "Neutral")
        c.inference_failure()
        self.assertEqual(c.eas, 1)
        self.assertEqual(c.specialization(), "Neutral")

    def test_invalid_input_rejected(self):
        for bad in (-1, math.nan, math.inf):
            with self.assertRaises(ValueError):
                target_eas(bad, 0, 0, 0)
        for p in ((.5, .5), (1, 1, 0, 0), (math.nan, 0, 0, 0), (-1, 1, 1, 0)):
            with self.assertRaises(ValueError):
                Controller().update_profile(p, 5)
        with self.assertRaises(ValueError):
            Controller("Impossible")

    def test_stale_and_invalid_results_latch_static_fallback(self):
        for difficulty, base in (("Easy", .85), ("Hard", 1.15)):
            for result in ({"age_seconds": 11}, {"valid_result": False}):
                with self.subTest(difficulty=difficulty, result=result):
                    c = Controller(difficulty)
                    for _ in range(100):
                        c.update_budget(1, 900, 100, 90, 5, boundary=True)
                        c.update_profile((1, 0, 0, 0), 5)
                    self.assertGreater(c.eas, 1)
                    self.assertEqual(c.specialization(**result), "Neutral")
                    self.assertEqual(c.eas, 1)
                    self.assertEqual(c.memory, (.25,) * 4)
                    for _ in range(20):
                        c.update_budget(1, 900, 100, 90, 5, boundary=True)
                        c.update_profile((1, 0, 0, 0), 5)
                        self.assertEqual(c.eas, 1)
                        self.assertEqual(c.difficulty, base)
                        self.assertEqual(c.specialization(), "Neutral")
                        self.assertEqual(c.memory, (.25,) * 4)

    def test_failure_requires_fresh_explicit_recovery(self):
        c = Controller()
        c.inference_failure()
        c.update_budget(1, 900, 100, 90, 5, boundary=True)
        self.assertEqual(c.eas, 1)
        self.assertEqual(c.specialization(), "Neutral")
        self.assertTrue(c.recover_inference((1, 0, 0, 0), 5, age_seconds=10))
        self.assertEqual(c.eas, 1)
        c.update_budget(1, 900, 100, 90, 5, boundary=False)
        self.assertEqual(c.eas, 1)
        c.update_budget(1, 900, 100, 90, 5, boundary=True)
        self.assertAlmostEqual(c.eas, 1.1)
        for _ in range(100):
            c.update_profile((1, 0, 0, 0), 5)
        self.assertEqual(c.specialization(), "Close")

    def test_stale_or_malformed_recovery_cannot_release_fallback(self):
        c = Controller()
        c.inference_failure()
        self.assertFalse(c.recover_inference((1, 0, 0, 0), 5, age_seconds=11))
        for probabilities in ((1, 1, 0, 0), (math.nan, 0, 0, 0)):
            with self.assertRaises(ValueError):
                c.recover_inference(probabilities, 5)
        c.update_budget(1, 900, 100, 90, 5, boundary=True)
        self.assertEqual(c.eas, 1)
        self.assertEqual(c.specialization(), "Neutral")

    def test_starting_difficulty_is_independent_of_style(self):
        easy, hard = Controller("Easy"), Controller("Hard")
        self.assertGreater(hard.difficulty, easy.difficulty)
        self.assertEqual(hard.memory, easy.memory)


if __name__ == "__main__":
    unittest.main()

