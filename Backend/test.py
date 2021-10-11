import unittest
import main

class TestStringMethods(unittest.TestCase):
    #Flora
    def test_check_username(self):
        self.assertEqual(main.check_username("12csaver4e3w  "), False)

    def test_check_username2(self):
        self.assertEqual(main.check_username("^*!(&#%($"), False)    
        
    # Emily
    def test_check_username_bool(self):
        self.assertFalse(main.check_username("JohnnyJune"))

#if name == '__main__':
#    unittest.main()



#run in console with command python -m unittest

