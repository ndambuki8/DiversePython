import unittest

from accountant import Accountant

class TestAccountant(unittest.TestCase):
    """TEsts for the class Accountant"""

    '''When testing a class, you usually have to make an instance
of the class. The setUp() method is run before every test.
Any instances you make in setUp() are available in every
test you write.'''
    def setUp(self):
        self.acc = Accountant()


    def test_initial_balance(self):
        #Default balance should be 0
        acc = Accountant()
        self.assertEqual(acc.balance, 0)

        #Test non-default balance
        acc = Accountant(200)
        self.assertEqual(acc.balance, 200)

    def test_deposit(self):
        #Test single deposit
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)

        #Test multiple deposits
        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        #Test single withdrawal
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900)

if __name__== '__main__':
    unittest.main()