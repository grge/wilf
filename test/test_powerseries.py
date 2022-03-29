from pytest import approx
from wilf.powerseries import PowerSeries, exp
from wilf.utils import factorial

def test_geometric_series():
    gs = 1 / (1 - PowerSeries.x)
    for coef_ix in range(20):
        assert gs.f(coef_ix) == 1

def test_exp():
    e_to_x = exp(PowerSeries.x)
    for coef_ix in range(20):
        assert e_to_x.f(coef_ix) == approx(1 / factorial(coef_ix))
        