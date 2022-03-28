from dataclasses import dataclass
from numbers import Number
from typing import List

from wilf.powerseries import PowerSeries, exp, derivative

@dataclass
class RV:
    """A random variable defined by its characteristic function"""
    # characteristic function
    cf : PowerSeries

    def moment(self, k:int) -> float:
        return (1j ** (-k)) * derivative(self.cf, k).f(0)

    def mean(self):
        return self.moment(1)

    def var(self):
        return self.moment(2) - self.mean() ** 2

    def std(self):
        return self.var() ** 0.5

    def __add__(self, other: 'RV') -> 'RV':
        return RV(self.cf * other.cf)



x = PowerSeries.x

# Note: maybe a better idea would be to have a subclass for each type of RV,
# instead of all of these constructor functions?

# For now the intention is to support continuous RVs only. Discrete RV's are
# fundamentally the same, but will need some explicit discretisation of the
# random variates generated, which I will worry about how to do later on.
def binomial(n, p) -> RV:
    return RV(exp(1 - p + p * (x * 1j))**n)

def poisson(l) -> RV:
    return RV(exp((exp(x * 1j) - 1) * l))

def uniform(a, b) -> RV:
    return RV((exp(1j * b * x) - exp(1j * a * x)) / (1j * x * (b - a)))

def normal(m, s) -> RV:
    return RV(exp((1J * x * m) - (0.5 * s**2 * x**2)))

def exponential(l) -> RV:
    return RV(1/(1 - 1J * x * 1/l))

def gamma(k, theta) -> RV:
    return RV((1 - 1j*x*theta)**(-k))

def empirical(data : List[Number]) -> RV:
    return RV(sum(exp(1J * x * d) for d in data)/len(data))