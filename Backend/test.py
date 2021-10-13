import unittest
import main

class TestStringMethods(unittest.TestCase):

 # Before
  def setUp(self):
    print("\n")
    print("Before testing...")
    
    
    
  #Flora
  def test_check_username(self)
    self.assertEqual(main.check_username("12csaver4e3w  "), False)

  def test_check_username2(self):
    self.assertEqual(main.check_username("^*!(&#%($"), False)    
      
     
  # Emily
  def test_check_valid_password(self):
    # ensures that password satisfies length requirement
    password = main.check_valid_password("supercalifragilisticexpialidocious")
    self.assertEqual(password, True)

  def test_check_valid_password2(self):
    # ensures that password DOES NOT satisfy length requirement
    password = main.check_valid_password("hello")
    self.assertEqual(password, False)

    
  # Nathan
  def test_check_wordbank(self):
      word = main.check_wordbank("moon")
      self.assertEqual(word, True)

  def test_check_wordbank2(self):
      word = main.check_wordbank("sun")
      self.assertEqual(word, False)
     
    
  #Neha
  #ensures that this username is not taken
  def test_check_username_bool(self):
      username = main.check_username("JohnnyJune")
      self.assertFalse(username)

  def test_check_username_bool2(self):
      username = main.check_username("JohnnyJune123")
      self.assertFalse(username)

  # After
  def tearDown(self):
    print("Finishing test...")



#run in console with command python -m unittest

