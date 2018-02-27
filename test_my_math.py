import my_math
import unittest

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
        result = my_math.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = my_math.add(10.5, 2)
        self.assertEqual(result, 12.5)

class TestMultiply(unittest.TestCase):

    def test_multiply_integers(self):
        result = my_math.multiply(1, 2)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
