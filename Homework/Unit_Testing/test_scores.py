import unittest
import scores

class TestScores(unittest.TestCase):
    def test(self):
        self.assertGreater(scores.exam(),0)
        self.assertEqual(scores.exam(),15)
if __name__ == "__main__":
    unittest.main()
