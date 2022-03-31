from dataclasses import dataclass
from numbers import Number
from typing import List, Tuple

import numpy as np

from wilf.powerseries import PowerSeries, exp, derivative
from wilf.density import provost_estimate

@dataclass
class RV:
    """A random variable defined by its characteristic function"""
    # characteristic function
    cf : PowerSeries
    support : Tuple[float, float]

    def moment(self, k:int) -> float:
        return (1j ** (-k)) * derivative(self.cf, k).f(0)

    def mean(self):
        return self.moment(1)

    def var(self):
        return self.moment(2) - self.mean() ** 2

    def std(self):
        return self.var() ** 0.5

    def pdf(self, x):
        return provost_estimate(self)(x)

    def __add__(self, other: 'RV | Number') -> 'RV':
        match other:
            case RV():
                return RV(
                    cf=self.cf * other.cf,
                    support=(
                        self.support[0] + other.support[0],
                        self.support[1] + other.support[1]
                    )
                )
            case Number():
                return NotImplemented

    def __mul__(self, other: 'RV | Number') -> 'RV':
        match other:
            case RV():
                return NotImplemented
            case Number():
                return RV(
                    cf=lambda i: self.cf(i)*other, 
                    support=(self.support[0]*other, self.support[1]*other)
                )


x = PowerSeries.x

# Note: maybe a better idea would be to have a subclass for each type of RV,
# instead of all of these constructor functions?

# For now the intention is to support continuous RVs only. Discrete RV's are
# fundamentally the same, but will need some explicit discretisation of the
# random variates generated, which I will worry about how to do later on.
def binomial(n, p) -> RV:
    return RV(cf=exp(1 - p + p * (x * 1j))**n, support=(0, n))

def poisson(l) -> RV:
    return RV(cf=exp((exp(x * 1j) - 1) * l), support=(0, np.inf))

def uniform(a, b) -> RV:
    return RV(cf=(exp(1j * b * x) - exp(1j * a * x)) / (1j * x * (b - a)), support=(a, b))

def normal(m, s) -> RV:
    return RV(cf=exp((1J * x * m) - (0.5 * s**2 * x**2)), support=(-np.inf, np.inf))

def exponential(l) -> RV:
    return RV(cf=1/(1 - 1J * x * 1/l), support=(0, np.inf))

def gamma(k, theta) -> RV:
    return RV(cf=(1 - 1j*x*theta)**(-k), support=(0, np.inf))

def empirical(data : List[Number]) -> RV:
    return RV(cf=sum(exp(1J * x * d) for d in data)/len(data), support=(min(data), max(data)))