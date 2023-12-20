from .. import utils
from .. import builder
from . import base
from abc import ABC, abstractmethod
from .Fp2 import Fp2
from .Fr import Fr


@builder.provide_methods(
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__mul__").using(builder.buildMul).with_args(Fr),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("hashAndMapTo"),
    builder.method("isZero"),
    builder.method("serialize"),
    builder.method("setStr"),
)
class G2(base.Structure):
    _fields_ = [
        ("x", Fp2),
        ("y", Fp2),
        ("z", Fp2),
    ]

    def __init__(self, s=None):
        if s is not None:
            self.setStr(s)

    @abstractmethod
    def __add__(self, other: 'G2') -> 'G2':
        pass

    @abstractmethod
    def __eq__(self, other: 'G2') -> bool:
        pass

    @abstractmethod
    def __mul__(self, other: Fr) -> 'G2':
        pass

    @abstractmethod
    def __neg__(self) -> 'G2':
        pass

    @abstractmethod
    def __sub__(self, other: 'G2') -> 'G2':
        pass

    @abstractmethod
    def deserialize(self, value: bytes) -> None:
        pass

    @abstractmethod
    def getStr(self) -> bytes:
        pass

    @staticmethod
    def hashAndMapTo(value: bytes) -> 'G2':
        pass

    @abstractmethod
    def isZero(self) -> bool:
        pass

    @abstractmethod
    def serialize(self) -> bytes:
        pass

    @abstractmethod
    def setStr(self, value: bytes) -> None:
        pass