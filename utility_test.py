import unittest
from utility import find_solutions


class MyTestCase(unittest.TestCase):
    def test_find_solutions_multiple(self):
        self.assertEqual(find_solutions(1, -5, 6), [3.0, 2.0])

    def test_find_solutions_single(self):
        self.assertEqual(find_solutions(1, 4, 4), -2.0)

    def test_find_solutions_no(self):
        self.assertEqual(find_solutions(1, 2, 2), "No real solutions")

    def test_find_solutions_value_error(self):
        with self.assertRaises(ValueError):
            find_solutions(1, 4, 4)


if __name__ == '__main__':
    unittest.main()
