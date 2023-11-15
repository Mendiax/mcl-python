import ctypes
from abc import ABC, abstractmethod
from .. import builder
from .. import consts
from . import base


@builder.provide_methods(
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
    builder.method("__mul__").using(builder.buildThreeOp).with_args("mul"),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("__truediv__").using(builder.buildThreeOp).with_args("div"),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("isOne"),
    builder.method("isZero"),
    builder.method("serialize"),
    builder.method("setByCSPRNG"),
    builder.method("setInt"),
    builder.method("setStr"),
    builder.method("setHashOf"),
)
class Fr(base.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FR_SIZE)]

    def __init__(self, value:None|int|bytes=None):
        if isinstance(value, int):
            self.setInt(value)
        elif isinstance(value, bytes):
            self.setStr(value)
        elif value is not None:
            raise TypeError("Fr can only be instantiated with int, bytes, or None")

    @abstractmethod
    def __add__(self, other: 'Fr') -> 'Fr':
        """Perform addition operation."""
        pass

    @abstractmethod
    def __eq__(self, other: 'Fr') -> bool:
        """Check for equality."""
        pass

    @abstractmethod
    def __invert__(self) -> 'Fr':
        """Perform inversion operation."""
        pass

    @abstractmethod
    def __mul__(self, other: 'Fr') -> 'Fr':
        """Perform multiplication operation."""
        pass

    @abstractmethod
    def __neg__(self) -> 'Fr':
        """Negate the current value."""
        pass

    @abstractmethod
    def __sub__(self, other: 'Fr') -> 'Fr':
        """Perform subtraction operation."""
        pass

    @abstractmethod
    def __truediv__(self, other: 'Fr') -> 'Fr':
        """Perform true division operation."""
        pass

    @abstractmethod
    def deserialize(self, value: bytes) -> None:
        """Deserialize a serialized object."""
        pass

    @abstractmethod
    def getStr(self, mode: int = 10) -> bytes:
        """Get string representation."""
        pass

    @abstractmethod
    def isOne(self) -> bool:
        """Check if the value is one."""
        pass

    @abstractmethod
    def isZero(self) -> bool:
        """Check if the value is zero."""
        pass

    @abstractmethod
    def serialize(self, mode: int = 10) -> bytes:
        """Serialize the current object."""
        pass

    @abstractmethod
    def setByCSPRNG(self) -> None:
        """Set the value using a CSPRNG."""
        pass

    @abstractmethod
    def setInt(self, value: int) -> None:
        """Set the value to an integer."""
        pass

    @abstractmethod
    def setStr(self, value: bytes, mode: int = 10) -> None:
        """Set the value from a string."""
        pass

    @staticmethod
    def setHashOf(value: bytes) -> 'Fr':
        """Set the value by hashing."""
        pass

    @staticmethod
    def rnd() -> 'Fr':
        fr = Fr()
        fr.setByCSPRNG()
        return fr

    @staticmethod
    def get_int(val : int) -> 'Fr':
        fr = Fr()
        fr.setByCSPRNG()
        return fr
