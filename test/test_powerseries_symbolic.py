from pytest import approx
from wilf.powerseries import PowerSeries, exp
from wilf.utils import factorial
from wilf.symbolics import Symbol

t = Symbol('t')
x = PowerSeries.x
        
def test_power_series_lmul_symbol():
    a = t * x
    assert isinstance(a, PowerSeries)

def test_power_series_rmul_symbol():
    a = x * t
    assert isinstance(a, PowerSeries)

