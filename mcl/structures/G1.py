from .. import utils
from .. import builder
from . import base
from abc import ABC, abstractmethod
from .Fp import Fp
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
class G1(base.Structure):
    _fields_ = [
        ("x", Fp),
        ("y", Fp),
        ("z", Fp),
    ]

    def __init__(self, s=None):
        if s is not None:
            self.setStr(s)

    @abstractmethod
    def __add__(self, other: 'G1') -> 'G1':
        pass

    @abstractmethod
    def __eq__(self, other: 'G1') -> bool:
        pass

    @abstractmethod
    def __mul__(self, other: Fr) -> 'G1':
        pass

    @abstractmethod
    def __neg__(self) -> 'G1':
        pass

    @abstractmethod
    def __sub__(self, other: 'G1') -> 'G1':
        pass

    @abstractmethod
    def deserialize(self, value: bytes) -> None:
        pass

    @abstractmethod
    def getStr(self) -> bytes:
        pass

    @staticmethod
    def hashAndMapTo(value: bytes) -> 'G1':
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
