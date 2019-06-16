import unittest #unnitest module import
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_user = User("Murtallah","Omtatah","tygr21")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name,"Murtallah")
        self.assertEqual(self.new_user.second_name,"Omtatah")
        self.assertEqual(self.new_user.password,"tygr21")