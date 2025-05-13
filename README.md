# 🧮 Python Tax Calculator

A simple Python-based tax calculator that computes tax, gross pay, and net pay based on Nigerian tax rules.

## 💡 Tax Rules
```
- First ₦200,000 of salary is **tax-free**
- Next ₦500,000 is taxed at **10%**
- Next ₦300,000 is taxed at **15%**
- Any amount **above ₦1,000,000** is taxed at **20%**
- **Bonuses are not taxed**, but are included in gross pay
```

## 📦 Features
```
- Accurate tax breakdown
- Handles edge cases (e.g., negative values)
- Includes unit tests with `pytest`
```

## ✅ Requirements
```
- Python 3.12+
- Install dependencies:
```

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```python
from tax_calculator import TaxRequest, calculate_tax
from decimal import Decimal

req = TaxRequest(salary=Decimal("900000"), bonus=Decimal("100000"))
res = calculate_tax(req)

print("Tax:", res.tax_amount)
print("Gross Pay:", res.gross_pay)
print("Net Pay:", res.net_pay)
```

## 🧪 Run Tests

```bash
pytest
```

## 🗂️ Project Structure

```
.
├── main.py          # Main tax logic
├── test/
│   └── test_tax_calculator.py # Pytest unit tests
├── requirements.txt
└── README.md
```

## 👤 Author

Favour Oluwademilade Bamgboye
[GitHub](https://github.com/iamagbacoder) | [LinkedIn](https://linkedin.com/in/iamAgbaCoder)

