"""
Mortgage Calculator Application
A comprehensive mortgage payment calculator
"""


def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculate monthly mortgage payment

    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as decimal)
        years (int): Loan term in years
    Returns:
        float: Monthly payment amount
    """
    if annual_rate == 0:
        return principal / (years * 12)

    monthly_rate = annual_rate / 12
    num_payments = years * 12

    payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** num_payments)
        / ((1 + monthly_rate) ** num_payments - 1)
    )
    return round(payment, 2)


if __name__ == "__main__":
    loan_amount = 300000
    annual_rate = 0.045
    loan_years = 30

    payment = calculate_monthly_payment(loan_amount, annual_rate, loan_years)
    print(f"Monthly Payment: ${payment:,.2f}")
