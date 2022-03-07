import unittest
from name_function import get_formatted_name as g_f_n


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = g_f_n('W..', 'A..', 'M..')
        self.assertEqual(formatted_name, 'W.. M.. A..')


if __name__ == '__main__':
    unittest.main()
