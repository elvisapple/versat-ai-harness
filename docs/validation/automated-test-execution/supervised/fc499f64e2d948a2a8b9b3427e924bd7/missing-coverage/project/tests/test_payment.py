import unittest

from src.payment import charge


class Payment(unittest.TestCase):
    def test_new(self):
        seen = set()
        self.assertTrue(charge(seen, "a", 1))
        self.assertEqual(seen, {"a"})

    def test_duplicate(self):
        seen = set()
        self.assertTrue(charge(seen, "a", 1))
        self.assertFalse(charge(seen, "a", 2))
        self.assertEqual(seen, {"a"})

    def test_distinct_keys_can_each_charge(self):
        seen = set()
        self.assertTrue(charge(seen, "a", 1))
        self.assertTrue(charge(seen, "b", 1))
        self.assertEqual(seen, {"a", "b"})

    def test_empty_key_is_rejected_without_changing_seen(self):
        seen = {"existing"}
        with self.assertRaises(ValueError):
            charge(seen, "", 1)
        self.assertEqual(seen, {"existing"})

    def test_zero_amount_is_rejected_without_consuming_key(self):
        seen = {"existing"}
        with self.assertRaises(ValueError):
            charge(seen, "new", 0)
        self.assertEqual(seen, {"existing"})
        self.assertTrue(charge(seen, "new", 1))
        self.assertEqual(seen, {"existing", "new"})

    def test_negative_amount_is_rejected_without_consuming_key(self):
        seen = {"existing"}
        with self.assertRaises(ValueError):
            charge(seen, "new", -1)
        self.assertEqual(seen, {"existing"})
        self.assertTrue(charge(seen, "new", 1))
        self.assertEqual(seen, {"existing", "new"})

    def test_invalid_duplicate_amount_is_rejected(self):
        seen = {"a"}
        with self.assertRaises(ValueError):
            charge(seen, "a", 0)
        self.assertEqual(seen, {"a"})
