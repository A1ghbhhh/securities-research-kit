import math

from researchkit.valuation import dcf, relative_valuation


def test_dcf_positive():
    ev = dcf([100, 110, 121], 0.10, 0.02)
    pv = 100 / 1.1 + 110 / 1.21 + 121 / 1.331
    tv = 121 * 1.02 / (0.10 - 0.02)
    pv_tv = tv / 1.331
    assert abs(ev - (pv + pv_tv)) < 1e-6


def test_dcf_invalid_rate():
    raised = False
    try:
        dcf([100], 0.05, 0.06)
    except ValueError:
        raised = True
    assert raised


def test_relative_valuation_mean():
    assert abs(relative_valuation([10, 12, 14], 2.0) - 24.0) < 1e-9


def test_relative_valuation_median():
    assert abs(relative_valuation([10, 12, 14], 2.0, method="median") - 24.0) < 1e-9
