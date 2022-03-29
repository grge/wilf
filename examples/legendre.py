"""
Having a lazily evaluated PowerSeries object that can have symbolic expressions
in each coefficient is extremely powerful. Below, the generating function
for the legendre polynomials is defined as a PowerSeries object using ordinary
python expressions. The symbol 't' is represents the domain of the Legendre
polynomials, while 'x' is the formal variable of the power series.

See https://en.wikipedia.org/wiki/Legendre_polynomials

To draw the nth polynomial, we just pick out the nth coefficient of the power
series, and substitute out the symbolic term t.
"""
import numpy as np
import matplotlib.pyplot as plt

from wilf.powerseries import PowerSeries
from wilf.symbolics import Symbol

# t is an algebraic symbol. x is the formal argument of a power series
t = Symbol('t')
x = PowerSeries.x

# We can mix and match the symbols freely in order to build the closed form of
# the generating function. The result is a PowerSeries object with SymbolicExpression
# objects for each coefficient.
legendre = 1/((1 - 2 * x * t + x**2)**0.5)

# Draw the first few polynomials
xs = np.linspace(-1, 1, 50)
for n in range(1, 9):
    ys = [legendre.f(n).subs({t:xv}) for xv in xs]
    plt.plot(xs, ys, label=f'n={n}')
plt.legend()
plt.show()