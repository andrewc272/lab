import unittest
from account import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account('Matthew')

    def tearDown(self) -> None:
        del self.account

    def test_init(self):
        self.assertEqual(self.account.get_name(), 'Matthew')
        self.assertEqual(self.account.get_balance(), 0.0)

        #passing a incorrect type
        self.assertRaises(TypeError, self.account.__init__, 5)


    def test_deposit(self):
        self.assertEqual(self.account.get_balance(), 0.0)

        #test float
        self.assertEqual(self.account.deposit(100.5), True)
        self.assertEqual(self.account.get_balance(), 100.5)

        #test negative float
        self.assertEqual(self.account.deposit(-55.2), False)
        self.assertEqual(self.account.get_balance(), 100.5)

        #test int
        self.assertEqual(self.account.deposit(10), True)
        self.assertEqual(self.account.get_balance(), 110.5)

        # test zero
        self.assertEqual(self.account.deposit(0.0), False)
        self.assertEqual(self.account.get_balance(), 110.5)

        #test str
        self.assertRaises(TypeError, self.account.deposit, 'x')

    def test_withdraw(self):
        #add some money
        self.account.deposit(80.3)

        #test max withdraw
        self.assertEqual(self.account.withdraw(80.3), True)
        self.assertEqual(self.account.get_balance(), 0.0)

        # add some money
        self.account.deposit(80.3)

        #test more than max withdraw
        self.assertEqual(self.account.withdraw(90.2), False)
        self.assertEqual(self.account.get_balance(), 80.3)

        #test less than max withdraw
        self.assertEqual(self.account.withdraw(3.2), True)
        self.assertEqual(self.account.get_balance(), 77.1)

        #test int
        self.assertEqual(self.account.withdraw(5), True)
        self.assertEqual(self.account.get_balance(), 72.1)

        #test 0
        self.assertEqual(self.account.withdraw(0.0), False)
        self.assertEqual(self.account.get_balance(), 72.1)

        #test negative
        self.assertEqual(self.account.withdraw(-1.8), False)
        self.assertEqual(self.account.get_balance(), 72.1)

        #test str
        self.assertRaises(TypeError, self.account.withdraw, 'x')


if __name__ == '__main__':
    unittest.main()
