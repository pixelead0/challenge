import unittest

from problem_002_counting_valleys import counting_valleys


class TestCountingValleys(unittest.TestCase):
    def test_zero(self):
        steps = 0
        path = ""
        result = 0
        assert counting_valleys(steps, path) == result

    def test_one(self):
        steps = 8
        path = "UDDDUDUU"
        result = 1
        assert counting_valleys(steps, path) == result

    def test_two(self):
        steps = 12
        path = "DDUUDDUDUUUD"
        result = 2
        assert counting_valleys(steps, path) == result

    def test_three(self):
        steps = 10
        path = "DUDDDUUDUU"
        result = 2
        assert counting_valleys(steps, path) == result

    def test_four(self):
        steps = 10
        path = "DDUDDUUDUU"
        result = 1
        assert counting_valleys(steps, path) == result


if __name__ == "__main__":
    unittest.main()
