"Tests for my custom list implementation"
import unittest

from parameterized import parameterized

from custom_list import CustomList


class CustomListTests(unittest.TestCase):

    "Test case for CustomList."

    @parameterized.expand([
        ([0, 1, 2], [-1, 2, 10], [-1, 3, 12]),
        ([0, 1, 2, 3, 4], [-1, 2, 10], [-1, 3, 12, 3, 4]),
        ([0, 1, 2], [-1, 2, 10, -2, 0], [-1, 3, 12, -2, 0]),
    ])
    def test_add(self, list_0: list, list_1: list, correct_result: list):
        "Test addition of CustomList and list."
        self.assertEqual(list(list_0 + CustomList(list_1)), correct_result)
        self.assertEqual(list(list_1 + CustomList(list_0)), correct_result)
        self.assertEqual(list(CustomList(list_0) + list_1), correct_result)
        self.assertEqual(list(CustomList(list_1) + list_0), correct_result)
        self.assertEqual(list(CustomList(list_0) + CustomList(list_1)), correct_result)
        self.assertEqual(list(CustomList(list_1) + CustomList(list_0)), correct_result)

    @parameterized.expand([
        ([0, 1, 2], [-1, 2, 10], [1, -1, -8]),
        ([0, 1, 2, 3, 4], [-1, 2, 10], [1, -1, -8, 3, 4]),
        ([0, 1, 2], [-1, 2, 10, -2, 0], [1, -1, -8, 2, 0]),
    ])
    def test_sub(self, list_0: list, list_1: list, correct_result: list):
        "Test subtraction of CustomList and list."
        self.assertEqual(list(list_0 - CustomList(list_1)), correct_result)
        self.assertEqual(list(CustomList(list_0) - list_1), correct_result)
        self.assertEqual(list(CustomList(list_0) - CustomList(list_1)), correct_result)

    @parameterized.expand([
        ([-1, 0, 1], [5, 5, 4, -10, -4], True),
        ([0, 2], [5, -7, 10], False)
    ])
    def test_eq(self, list_0: list, list_1: list, correct_result: bool):
        "Test == of CustomList and list."
        self.assertEqual(list_0 == CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) == list_1, correct_result)
        self.assertEqual(CustomList(list_0) == CustomList(list_1), correct_result)

    @parameterized.expand([
        ([-1, 0, 1], [5, 5, 4, -10, -4], False),
        ([0, 2], [5, -7, 10], True)
    ])
    def test_neq(self, list_0: list, list_1: list, correct_result: bool):
        "Test != of CustomList and list."
        self.assertEqual(list_0 != CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) != list_1, correct_result)
        self.assertEqual(CustomList(list_0) != CustomList(list_1), correct_result)

    @parameterized.expand([
        ([-1, 5, 1], [5, 5, 4, -2], True),
        ([0, 2, 3], [5, -7], False),
        ([-1, 0, 1], [5, 5, 4, -10, -4], False),
    ])
    def test_lt(self, list_0: list, list_1: list, correct_result: bool):
        "Test < of CustomList and list."
        self.assertEqual(list_0 < CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) < list_1, correct_result)
        self.assertEqual(CustomList(list_0) < CustomList(list_1), correct_result)

    @parameterized.expand([
        ([-1, 5, 1], [5, 5, 4, -2], True),
        ([0, 2, 3], [5, -7], False),
        ([-1, 0, 1], [5, 5, 4, -10, -4], True),
    ])
    def test_le(self, list_0: list, list_1: list, correct_result: bool):
        "Test <= of CustomList and list."
        self.assertEqual(list_0 <= CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) <= list_1, correct_result)
        self.assertEqual(CustomList(list_0) <= CustomList(list_1), correct_result)

    @parameterized.expand([
        ([5, 5, 4, -2], [-1, 5, 1], True),
        ([5, -7], [0, 2, 3], False),
        ([-1, 0, 1], [5, 5, 4, -10, -4], False),
    ])
    def test_gt(self, list_0: list, list_1: list, correct_result: bool):
        "Test > of CustomList and list."
        self.assertEqual(list_0 > CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) > list_1, correct_result)
        self.assertEqual(CustomList(list_0) > CustomList(list_1), correct_result)

    @parameterized.expand([
        ([5, 5, 4, -2], [-1, 5, 1], True),
        ([5, -7], [0, 2, 3], False),
        ([-1, 0, 1], [5, 5, 4, -10, -4], True),
    ])
    def test_ge(self, list_0: list, list_1: list, correct_result: bool):
        "Test >= of CustomList and list."
        self.assertEqual(list_0 >= CustomList(list_1), correct_result)
        self.assertEqual(CustomList(list_0) >= list_1, correct_result)
        self.assertEqual(CustomList(list_0) >= CustomList(list_1), correct_result)
