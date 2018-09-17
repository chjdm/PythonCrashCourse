import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('liu', 'wei')
        self.assertEqual(formatted_name, 'Liu wei')


unittest.main()
