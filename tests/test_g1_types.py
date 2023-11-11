# test_g1.py
import unittest
from mcl import G1, Fr

class G1TestsTypes(unittest.TestCase):

    def setUp(self):
        self.g1 = G1()
        self.fr = Fr()

    def test_add(self):
        # Assuming that G1 addition requires another G1 instance
        result = self.g1 + self.g1
        self.assertIsInstance(result, G1, "__add__ should return an instance of G1")

    def test_eq(self):
        # Assuming that G1 equality check requires another G1 instance
        self.assertTrue(self.g1 == self.g1, "__eq__ should return True for the same G1 instance")

    def test_mul(self):
        # Assuming that G1 multiplication requires an Fr instance
        result = self.g1 * self.fr
        self.assertIsInstance(result, G1, "__mul__ should return an instance of G1")

    def test_neg(self):
        result = -self.g1
        self.assertIsInstance(result, G1, "__neg__ should return an instance of G1")

    def test_sub(self):
        result = self.g1 - self.g1
        self.assertIsInstance(result, G1, "__sub__ should return an instance of G1")

    def test_deserialize(self):
        # Assuming deserialize method modifies the object itself and returns None
        value = b"serialized_data"
        result = self.g1.deserialize(value)
        self.assertIsNone(result, "deserialize should return None")

    def test_get_str(self):
        result = self.g1.getStr()
        self.assertIsInstance(result, bytes, "getStr should return bytes")

    def test_hash_and_map_to(self):
        value = b"data_to_hash"
        result = self.g1.hashAndMapTo(value)
        self.assertIsInstance(result, G1, "hashAndMapTo should return an instance of G1")


    def test_is_zero(self):
        result = self.g1.isZero()
        self.assertIsInstance(result, bool, "isZero should return a bool")

    def test_serialize(self):
        result = self.g1.serialize()
        self.assertIsInstance(result, bytes, "serialize should return bytes")

    def test_set_str(self):
        value = b"data_to_set"
        result = self.g1.setStr(value)
        self.assertIsNone(result, "setStr should return None")

if __name__ == '__main__':
    unittest.main()
