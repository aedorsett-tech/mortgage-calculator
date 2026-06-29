"""Tests for mortgage calculator"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mortgage_calculator import calculate_monthly_payment


def test_monthly_payment():
    payment = calculate_monthly_payment(300000, 0.045, 30)
    assert abs(payment - 1520.06) < 0.01


def test_zero_interest():
    payment = calculate_monthly_payment(120000, 0.0, 10)
    assert payment == 1000.0
