import unittest
import MovieRentalStoreFunctions

class TestCaterer(unittest.TestCase):
    def test_ValidName(self):
        self.assertTrue(MovieRentalStoreFunctions.ValidName("Omar"))
    def test_ValidRating(self):
        self.assertTrue(MovieRentalStoreFunctions.ValidRating("PG"))
    def test_OverdueCharge(self):
        self.assertEqual((MovieRentalStoreFunctions.OverdueCharge(10,5)),0)
    def test_InStock(self):
        self.assertFalse(MovieRentalStoreFunctions.InStock(4,4))

if __name__ == "__main__":
    unittest.main()
