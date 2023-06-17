import unittest
import databurst


class TestDataburst(unittest.TestCase):
    def test_generate_name(self):
        name = databurst.generate_name()
        self.assertIsInstance(name, str)
        self.assertNotEqual(name, "")

    def test_generate_address(self):
        address = databurst.generate_address()
        self.assertIsInstance(address, str)
        self.assertNotEqual(address, "")

    def test_generate_phone_number(self):
        phone_number = databurst.generate_phone_number()
        self.assertIsInstance(phone_number, str)
        self.assertNotEqual(phone_number, "")

    def test_generate_email(self):
        email = databurst.generate_email()
        self.assertIsInstance(email, str)
        self.assertNotEqual(email, "")


if __name__ == '__main__':
    unittest.main()
