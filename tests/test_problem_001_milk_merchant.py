import unittest

from problem_001_milk_merchant import milk_merchant


class TestMilkMerchant(unittest.TestCase):
    def test_zero(self):
        assert milk_merchant(0, []) == 0

    def test_one(self):
        n = 1
        ar = [1]
        result = 0
        assert milk_merchant(n, ar) == result

    def test_two(self):
        n = 2
        ar = [1, 2]
        result = 0
        assert milk_merchant(n, ar) == result

    def test_three(self):
        n = 2
        ar = [2, 2]
        result = 1
        assert milk_merchant(n, ar) == result

    def test_four(self):
        n = 9
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        result = 3
        assert milk_merchant(n, ar) == result

    def test_five(self):
        n = 20
        ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
        result = 9
        assert milk_merchant(n, ar) == result

    def test_six(self):
        n = 10
        ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
        result = 4
        assert milk_merchant(n, ar) == result

    def test_seven(self):
        n = 15
        ar = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
        result = 6
        assert milk_merchant(n, ar) == result


if __name__ == "__main__":
    unittest.main()
