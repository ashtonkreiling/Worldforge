import unittest
import sys
import os

# Add project root to path to import rollers
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from rollers.settlement_growth_roller import determine_growth


class TestDetermineGrowth(unittest.TestCase):
    
    def test_roll_1_returns_negative_one(self):
        """Test that rolling a 1 returns -1 (settlement shrinks)"""
        self.assertEqual(determine_growth(0), -1)
    
    def test_roll_2_returns_zero(self):
        """Test that rolling a 2 returns 0 (settlement stays the same)"""
        self.assertEqual(determine_growth(1), 0)
    
    def test_roll_3_returns_zero(self):
        """Test that rolling a 3 returns 0 (settlement stays the same)"""
        self.assertEqual(determine_growth(2), 0)
    
    def test_roll_4_returns_zero(self):
        """Test that rolling a 4 returns 0 (settlement stays the same)"""
        self.assertEqual(determine_growth(3), 0)
    
    def test_roll_5_returns_one(self):
        """Test that rolling a 5 returns 1 (settlement grows)"""
        self.assertEqual(determine_growth(4), 1)
    
    def test_roll_6_returns_one(self):
        """Test that rolling a 6 returns 1 (settlement grows)"""
        self.assertEqual(determine_growth(5), 1)


if __name__ == '__main__':
    unittest.main()

