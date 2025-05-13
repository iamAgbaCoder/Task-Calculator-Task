from decimal import Decimal
from dataclasses import dataclass


@dataclass
class TaxRequest:
    salary: Decimal
    bonus: Decimal


@dataclass
class TaxResponse:
    tax_amount: Decimal
    gross_pay: Decimal
    net_pay: Decimal


def calculate_tax(request: TaxRequest) -> TaxResponse:
    """
    Calculate the tax based on a progressive system:
    - First ₦200,000 is tax-free
    - Next ₦500,000 is taxed at 10%
    - Next ₦300,000 is taxed at 15%
    - Any amount above ₦1,000,000 is taxed at 20%
    Bonuses are not taxed but added to gross pay.

    Args:
        request (TaxRequest): Contains salary and bonus as Decimal

    Returns:
        TaxResponse: Contains tax_amount, gross_pay, net_pay
    """
    salary = request.salary
    bonus = request.bonus
    taxable_income = max(Decimal("0.00"), salary - Decimal("200000.00"))
    tax = Decimal("0.00")

    # Tax on next ₦500,000 at 10%
    if taxable_income > 0:
        tier_1 = min(taxable_income, Decimal("500000.00"))
        tax += tier_1 * Decimal("0.10")
        taxable_income -= tier_1

    # Tax on next ₦300,000 at 15%
    if taxable_income > 0:
        tier_2 = min(taxable_income, Decimal("300000.00"))
        tax += tier_2 * Decimal("0.15")
        taxable_income -= tier_2

    # Remaining taxable income at 20%
    if taxable_income > 0:
        tax += taxable_income * Decimal("0.20")

    gross_pay = salary + bonus
    net_pay = gross_pay - tax

    return TaxResponse(
        tax_amount=tax.quantize(Decimal("0.01")),
        gross_pay=gross_pay.quantize(Decimal("0.01")),
        net_pay=net_pay.quantize(Decimal("0.01"))
    )

