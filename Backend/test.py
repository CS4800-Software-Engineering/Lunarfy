import unittest
import main

class TestStringMethods(unittest.TestCase):
    # Before
    def setUp(self):
        print("\n")
        print("Before testing...")

 
    #Flora
    def test_check_username(self):
        self.assertEqual(main.check_username("12csaver4e3w  "), False)

    def test_check_username2(self):
        self.assertEqual(main.check_username("^*!(&#%($"), False)    
        
    # Emily
     def test_check_username_bool(self):
        # ensures that this username is not taken
        username = main.check_username("JohnnyJune")
        self.assertFalse(username)
     def test_check_valid_password(self):
        # ensures that password satisfies length requirement
        password = main.check_valid_password("supercalifragilisticexpialidocious")
        self.assertEqual(password, True)
        
        
    # After
    def tearDown(self):
        print("Finishing test...")

#if name == '__main__':
#    unittest.main()



#run in console with command python -m unittest

