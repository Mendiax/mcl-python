import unittest
from mcl import Fr
import random

class FrTests(unittest.TestCase):

    def setUp(self):
        self.fr = Fr()  # Create a common Fr instance for use in tests
        self.fr1 = Fr()
        self.fr1.setByCSPRNG()
        self.fr2 = Fr()
        self.fr2.setByCSPRNG()

    def test_init_fr(self):
        # Ensures an Fr instance can be created
        self.assertIsInstance(self.fr, Fr, "The object should be an instance of Fr")

    def test_set_str_valid(self):
        # Tests setting a valid string
        self.fr.setStr(b"12345678901234567")
        self.assertEqual(self.fr.getStr(), b"12345678901234567", "The string should be set correctly")

    def test_is_equal(self):
        # Ensures that an Fr object is equal to itself
        self.fr.setByCSPRNG()
        self.assertTrue(self.fr == self.fr,\
                        "The object should be equal to itself")

    def test_set_int(self):
        # Tests setting an integer
        self.fr.setInt(1)
        self.assertEqual(self.fr.getStr(), b"1",\
                         "The integer value should be set correctly")

    def test_mul(self):
        # Tests multiplication of two Fr instances
        result = self.fr * Fr()
        self.assertIsInstance(result, Fr,\
                              "The result of multiplication should be an instance of Fr")

    def test_get_str(self):
        # Tests the retrieval of a string representation
        self.fr.setStr(b"255")
        self.assertEqual(self.fr.getStr(), b"255", \
                         "The getStr method should return the correct string representation")

    def test_set_by_csprng(self):
        # Tests setting a value by CSPRNG
        self.fr.setByCSPRNG()
        self.assertNotEqual(self.fr.getStr(), "", \
                            "The CSPRNG value should not be an empty string")

    def test_not_equal(self):
        # Tests inequality
        fr1 = Fr()
        fr2 = Fr()
        fr1.setByCSPRNG()
        fr2.setByCSPRNG()
        self.assertNotEqual(fr1, fr2, \
                            "Two CSPRNG values should not be equal")

    def test_add(self):
        # Test the addition operation
        sum_fr = self.fr1 + self.fr2
        self.assertIsInstance(sum_fr, Fr, "The result of addition should be an instance of Fr")

    def test_sub(self):
        # Test the subtraction operation
        diff_fr = self.fr1 - self.fr2
        self.assertIsInstance(diff_fr, Fr, "The result of subtraction should be an instance of Fr")

    def test_truediv(self):
        # Test the true division operation
        self.fr2.setInt(1)  # Set to a non-zero value to avoid division by zero
        div_fr = self.fr1 / self.fr2
        self.assertIsInstance(div_fr, Fr, "The result of division should be an instance of Fr")

    def test_massive_instance_creation(self):
        # Stress test for creating a large number of instances
        for _ in range(10000):
            _ = Fr()

    def test_intensive_math_operations(self):
        # Stress test for performing intensive math operations
        fr1 = Fr()
        fr1.setByCSPRNG()
        fr2 = Fr()
        fr2.setByCSPRNG()
        for _ in range(10000):
            _ = fr1 * fr2
            fr1.setInt(random.randint(1, 100))
            fr2.setInt(random.randint(1, 100))

    def test_serialization_deserialization_stress(self):
        # Stress test for serialization and deserialization
        for _ in range(10000):
            self.fr.setByCSPRNG()
            serialized = self.fr.serialize()
            deserialized = Fr()
            deserialized.deserialize(serialized)
            self.assertEqual(self.fr, deserialized, "Deserialized object should be equal to the original")


if __name__ == '__main__':
    unittest.main()
