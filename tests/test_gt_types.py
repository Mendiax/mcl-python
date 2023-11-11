# test_gt.py
import unittest
from mcl import GT, G1, G2, Fr

class GTTestsTypes(unittest.TestCase):

    def setUp(self):
        self.gt = GT()
        self.g1 = G1()
        self.g2 = G2()
        self.fr = Fr()

    def test_invert(self):
        result = ~self.gt
        self.assertIsInstance(result, GT, "__invert__ should return an instance of GT")

    def test_pairing(self):
        result = self.gt.pairing(self.g1, self.g2)
        self.assertIsInstance(result, GT, "pairing should return an instance of GT")

    def test_add(self):
        result = self.gt + self.gt
        self.assertIsInstance(result, GT, "__add__ should return an instance of GT")

    def test_eq(self):
        self.assertTrue(self.gt == self.gt, "__eq__ should return True for the same GT instance")

    def test_mul(self):
        result = self.gt * self.gt
        self.assertIsInstance(result, GT, "__mul__ should return an instance of GT")

    def test_neg(self):
        result = -self.gt
        self.assertIsInstance(result, GT, "__neg__ should return an instance of GT")

    def test_sub(self):
        result = self.gt - self.gt
        self.assertIsInstance(result, GT, "__sub__ should return an instance of GT")

    def test_pow(self):
        result = self.gt ** self.fr
        self.assertIsInstance(result, GT, "__pow__ should return an instance of GT")

    def test_deserialize(self):
        value = b"serialized_data"
        result = self.gt.deserialize(value)
        self.assertIsNone(result, "deserialize should return None")

    def test_get_str(self):
        result = self.gt.getStr()
        self.assertIsInstance(result, bytes, "getStr should return bytes")

    def test_is_zero(self):
        result = self.gt.isZero()
        self.assertIsInstance(result, bool, "isZero should return a bool")

    def test_serialize(self):
        result = self.gt.serialize()
        self.assertIsInstance(result, bytes, "serialize should return bytes")

    def test_set_str(self):
        value = b"data_to_set"
        result = self.gt.setStr(value)
        self.assertIsNone(result, "setStr should return None")

if __name__ == '__main__':
    unittest.main()
