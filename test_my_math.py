import my_math
import unittest

class TestAdd(unittest.TestCase):

    def test_add_integers(self):
        result = my_math.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
