import unittest
import main

class TestStringMethods(unittest.TestCase):
    #Flora
    def test_check_username(self):
        self.assertEqual(main.check_username("12csaver4e3w  "), False)

    def test_upper(self):
        self.assertEqual(main.check_username("^*!(&#%($"), False)    

#if name == '__main__':
#    unittest.main()