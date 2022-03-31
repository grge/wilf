from functools import lru_cache

import scipy.stats as stats
from numpy.polynomial.polynomial import polyval
import numpy as np

def _random_fit_start_sample(rv, size=3):
    """
    We need a random sample to bootstrap the fitting process. To do that we use
    normally distributed samples fitted to our data mean and stdev.
    """
    m, s = rv.mean().real, rv.std().real
    return stats.norm(m,s).rvs(size=size)

def provost_estimate(rv, base=stats.norm, order=4):
    """
    Forms the approximant of the density function of the form
        f(x) = b(x) * p(x)
    where
        b(x) is a beta distribution fitted to the first two moments
        p(x) is a polynomial of degree N

    Using this model, the coefficients of p(x) using least squares in order to
    minimise the sum of square errors on the first N moments.

    Reference: https://ir.lib.uwo.ca/cgi/viewcontent.cgi?article=8671&context=etd
    """
    theta = base.fit(_random_fit_start_sample(rv, size=40))
    base_dist = base(*theta)
    moment_order = np.tile(np.arange(0, order+1), [order+1, 1]) + np.arange(order+1).reshape(-1, 1)
    X = np.vectorize(lru_cache(base_dist.moment))(moment_order)
    y = np.array([rv.moment(i).real for i in range(order+1)])
    a, residuals, rank, s = np.linalg.lstsq(X.real, y, rcond=None)
    fitted = lambda x: base_dist.pdf(x) * polyval(x, a)
    return fitted
