import unittest
from cities_functions import print_city_country

class CitiesFormatTest(unittest.TestCase):
    def test_city_country(self):
        
        formatted_output = print_city_country('Rome','italy')
        self.assertEqual(formatted_output, 'Rome, Italy')

    def test_city_country_population(self):

        formatted_output = print_city_country('Rome', 'italy', 25000)
        self.assertEqual(formatted_output, 'Rome, Italy - population 25000')

if __name__ == "__main__":
    unittest.main()
