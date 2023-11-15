import unittest
from mcl import Fr

class FrTestsTypes(unittest.TestCase):

    def test_set_str(self):
        # Check if setStr accepts bytes and doesn't return anything (None)
        fr = Fr()
        input_value = b"1234567890"
        result = fr.setStr(input_value)
        self.assertIsNone(result, "setStr should not return anything")

    def test_get_str(self):
        # Check if getStr returns a str
        fr = Fr()
        fr.setStr(b"1234567890")
        result_10 = fr.getStr()
        self.assertIsInstance(result_10, bytes, "getStr should return a str")
        result_16 = fr.getStr(16)
        self.assertIsInstance(result_16, bytes, "getStr should return a str")
        self.assertNotEqual(result_10, result_16, "different modes are the same")

    def test_set_hash(self):
        # Check if getStr returns a str
        fr = Fr.setHashOf(b"1234567890")
        self.assertIsInstance(fr, Fr, "setHashOf returns string")

    def test_add(self):
        # Check if __add__ returns an instance of Fr
        fr1 = Fr()
        fr2 = Fr()
        fr1.setStr(b"1")
        fr2.setStr(b"1")
        result = fr1 + fr2
        self.assertIsInstance(result, Fr, "__add__ should return an instance of Fr")

    # ... Add similar tests for __sub__, __mul__, and __truediv__

if __name__ == '__main__':
    unittest.main()
