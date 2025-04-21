
# Scott Macioce
# Module 7 - test_cities.py
# Purpose: Unit test for city_country function using unittest

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Test that Santiago and Chile returns 'Santiago, Chile'."""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
