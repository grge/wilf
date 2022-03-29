from dataclasses import dataclass
from functools import lru_cache
from typing import Callable
from numbers import Integral, Number, Real
import cmath

from wilf.utils import product

@dataclass
class PowerSeries:
    """A formal power series defined by a coefficient function.
    
    This represents the formal power series:

        $\sigma_i{f(i) x^i}$

    Where f is a coefficient function f :: int -> float

    """
    f : Callable[int, float]

    def __post_init__(self):
        """Post init hook. Used to memoise the coefficient function"""
        self.f = lru_cache(self.f)
        self._pow_cache = {}

    def __repr__(self):
        """Return a polynomial representation of the power series"""
        N = 6
        out = []
        i = 0 
        ss_digits = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        while len(out) < N and i < 100:
            coef = self.f(i)

            if coef != 0:
                if i == 0:
                    out.append(str(coef))
                elif i == 1:
                    out.append(f'{"" if coef == 1 else coef}x')
                else:
                    exponent = ''.join(ss_digits[int(d)] for d in str(i))
                    out.append(f'{"" if coef == 1 else coef}x{exponent}')
            i += 1
        s = ' + '.join(out).replace(" + -", " - ")
        return f"<{s} + ...>"

    def __call__(self, x : float, precision : int = 30):
        return sum(self.f(i) * x ** i for i in range(precision))

    def __add__(self, other : 'PowerSeries') -> 'PowerSeries':
        match other:
            case PowerSeries():
                f = lambda i: self.f(i) + other.f(i)
            case Number():
                f = lambda i: self.f(i) + other if i == 0 else self.f(i)
        return PowerSeries(f=f)

    def __radd__(self, other : 'Number') -> 'PowerSeries':
        return self + other
            
    def __sub__(self, other : 'PowerSeries') -> 'PowerSeries':
        match other:
            case Number():
                return PowerSeries(f=lambda i: self.f(i) - other if i == 0 else self.f(i))
            case PowerSeries():
                return PowerSeries(f=lambda i: self.f(i) - other.f(i))

    def __rsub__(self, other : 'Number') -> 'PowerSeries':
        return -self + other

    def __neg__(self) -> 'PowerSeries':
        return PowerSeries(f=lambda i: -self.f(i))

    def __mul__(self, other : 'Number | PowerSeries') -> 'PowerSeries':
        match other:
            case Number():
                f = lambda i: self.f(i) * other
            case PowerSeries():
                f = lambda i : sum(self.f(j) * other.f(i - j) for j in range(i+1))
        return PowerSeries(f=f)

    def __rmul__(self, other : 'Number | PowerSeries') -> 'PowerSeries':
        return self * other

    def __truediv__(self, other : 'Number | PowerSeries') -> 'PowerSeries':
        match other:
            case PowerSeries():
                return self * other.inverse() 
            case Number():
                return PowerSeries(f=lambda i: self.f(i) / other)

    def __rtruediv__(self, other : 'Number | PowerSeries') -> 'PowerSeries':
        return other * self.inverse()

    def inverse(self):
        a = self.f(0)
        q = 1 - self / a
        print(a)
        return PowerSeries(f=lambda n: sum((q**i).f(n) for i in range(n+1)) / a) 

    def __pow__(self, other : 'Number') -> 'PowerSeries':
        # Memoised power function... Maybe there's a cleaner way to do this?
        match other:
            case Integral():
                def pow(i):
                    if i == 0:
                        return PowerSeries.one
                    else:
                        i2 = self ** (i // 2)
                        return i2 * i2 if i % 2 == 0 else i2 * i2 * self
            case Real():
                def pow(i):
                    a = self.f(0)
                    ar = a ** i
                    q = self / a - 1
                    def coef(n : int):
                        return product(i - j for j in range(n)) / product(range(1, n+1))
                    def f(n : int) -> float:
                        return sum(coef(j)*(q**j).f(n) for j in range(n+1)) * ar
                    return PowerSeries(f=f)
            case _:
                raise NotImplementedError(f"Can't raise {self} to {other}")

        return self._pow_cache.setdefault(other, pow(other))

    @classmethod
    @property
    def one(cls):
        """Constructs the trivial power series 1"""
        return cls(lambda i: 1 if i==0 else 0)

    @classmethod
    @property
    def x(cls):
        """Constructs the trivial power series x"""
        return cls(lambda i: 1 if i==1 else 0)

    @classmethod
    @property
    def e(cls):
        return cls.one.exp()


def derivative(x:PowerSeries, n:int = 1) -> 'PowerSeries':
    def f(k: int):
        return product(range(k + 1, k + n + 1)) * x.f(k + n)
    return PowerSeries(f=f)


def exp(x : PowerSeries) -> PowerSeries:
    a = x.f(0)
    q = x - a
    ea = cmath.exp(a)
    def fact(n: int):
        return product(range(1, n+1))
    return PowerSeries(lambda n: sum((q**i).f(n) / fact(i) for i in range(n+1)) * ea)


def cos(x: PowerSeries) -> PowerSeries:
    return (exp(1j * x) + exp(-1j * x)) / 2


def sin(x: PowerSeries) -> PowerSeries:
    return (exp(1j * x) - exp(-1j * x)) / 2j