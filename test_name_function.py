import unittest
from name_function import get_formatted_name

# any method starting with 'test_' is run automatically.
# methods can have long descriptive names, as they won't be
# called by the program, but automatically by the unittest module


class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """

    def test_first_last_name(self):
        """ do names with name/surname work? """
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """ do names with name/middlename/surname work? """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
