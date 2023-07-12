import unittest
import account


class TestAccount(unittest.TestCase):
    def test_create(self):
        ac = account.Account("John Doe", 123, 0)
        self.assertEqual(ac.client_balance(), 0)
        self.assertNotEqual(ac.client_balance(), 5)

    def test_withdraw(self):
        ac = account.Account("John Doe", 123, 50)
        ac.withdraw(20)
        self.assertEqual(ac.client_balance(), 30)
        self.assertNotEqual(ac.client_balance(), 5)

    def test_deposit(self):
        ac = account.Account("John Doe", 123, 50)
        ac.deposit(20)
        self.assertEqual(ac.client_balance(), 70)
        self.assertNotEqual(ac.client_balance(), 5)
