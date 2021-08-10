#
import unittest
from example_112 import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('alif','hasan')
        self.assertEqual(formatted_name,'alif hasan')


unittest.main()
