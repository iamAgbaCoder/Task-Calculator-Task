import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from decimal import Decimal
from main import TaxRequest, calculate_tax


def test_tax_below_threshold():
    req = TaxRequest(salary=Decimal("150000"), bonus=Decimal("50000"))
    res = calculate_tax(req)
    assert res.tax_amount == Decimal("0.00")
    assert res.gross_pay == Decimal("200000.00")
    assert res.net_pay == Decimal("200000.00")


def test_tax_at_700k():
    req = TaxRequest(salary=Decimal("700000"), bonus=Decimal("0"))
    res = calculate_tax(req)
    # ₦500,000 taxed at 10% = ₦50,000
    assert res.tax_amount == Decimal("50000.00")
    assert res.gross_pay == Decimal("700000.00")
    assert res.net_pay == Decimal("650000.00")


def test_tax_above_1m():
    req = TaxRequest(salary=Decimal("1300000"), bonus=Decimal("100000"))
    res = calculate_tax(req)
    # Taxable = 1300000 - 200000 = 1100000
    # 500k @10% = 50,000
    # 300k @15% = 45,000
    # 300k @20% = 60,000
    # Total = 155,000
    assert res.tax_amount == Decimal("155000.00")
    assert res.gross_pay == Decimal("1400000.00")
    assert res.net_pay == Decimal("1245000.00")


def test_negative_salary_bonus():
    req = TaxRequest(salary=Decimal("-50000"), bonus=Decimal("-10000"))
    res = calculate_tax(req)
    assert res.tax_amount == Decimal("0.00")
    assert res.gross_pay == Decimal("-60000.00")
    assert res.net_pay == Decimal("-60000.00")

