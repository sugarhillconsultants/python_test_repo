# import pytest
import pytest

# import the function from your file
from session import add_numbers

# Check if it properly adds positive numbers
def test_add_positive():
    assert add_numbers(1,2) == 3

# Check if it properly adds zero
def test_add_zero():
    assert add_numbers(1,0) == 1

# Check if it properly adds negative numbers
def test_add_negative():
    assert add_numbers(4, -100) == -96

# Now check if it correctly produces an error when provided
def test_add_string_expect_exception():
    with pytest.raises(TypeError):
        add_numbers(5, 'I do not belong here')
