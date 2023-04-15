import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """TEsts for names.py"""

    def test_first_last(self):
        """Test names like Lynn Pvris"""

        full_name = get_full_name('Lynn', 'Pvris')
        self.assertEqual(full_name, 'Lynn Pvris')
    
    def test_middle(self):
        """Test names like David Lee Roth"""
        full_name = get_full_name('david', 'roth', 'lee')

        self.assertEqual(full_name, "David Lee Roth")


if __name__ == '__main__':
    unittest.main()
