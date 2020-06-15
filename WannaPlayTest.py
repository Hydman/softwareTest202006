import unittest
import WannaPlay

class TestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(WannaPlay.plus(1, 2), 3)


if __name__ == "__main__":
    unittest.main()