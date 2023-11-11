from .. import utils
from .. import builder
from . import base
from .G1 import G1
from .G2 import G2
from .Fp import Fp
from .Fr import Fr
from abc import ABC, abstractmethod

@builder.provide_methods(
    builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
    builder.method("pairing").using(builder.buildPairing).with_args(G1, G2),
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__mul__").using(builder.buildThreeOp).with_args("mul"),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("__pow__").using(builder.buildPow).with_args(Fr),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("isZero"),
    builder.method("serialize"),
    builder.method("setStr"),
)
class GT(base.Structure):
    _fields_ = [
        ("d", (Fp * 12)),
    ]

    @abstractmethod
    def __invert__(self) -> 'GT':
        pass

    @abstractmethod
    def pairing(self, g1: G1, g2: G2) -> 'GT':
        pass

    @abstractmethod
    def __add__(self, other: 'GT') -> 'GT':
        pass

    @abstractmethod
    def __eq__(self, other: 'GT') -> bool:
        pass

    @abstractmethod
    def __mul__(self, other: 'GT') -> 'GT':
        pass

    @abstractmethod
    def __neg__(self) -> 'GT':
        pass

    @abstractmethod
    def __sub__(self, other: 'GT') -> 'GT':
        pass

    @abstractmethod
    def __pow__(self, other: Fr) -> 'GT':
        pass

    @abstractmethod
    def deserialize(self, value: bytes) -> None:
        pass

    @abstractmethod
    def getStr(self) -> bytes:
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