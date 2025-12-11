"""
Test suite for calc.py calculator module
"""
import pytest
from calc import add, subtract, multiply, divide


class TestAddition:
    """Test cases for the add function"""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 5) == 15
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, -3) == -8
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers"""
        assert add(5, -3) == 2
        assert add(-10, 15) == 5
    
    def test_add_zero(self):
        """Test adding with zero"""
        assert add(0, 5) == 5
        assert add(7, 0) == 7
        assert add(0, 0) == 0


class TestSubtraction:
    """Test cases for the subtract function"""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(10, 3) == 7
        assert subtract(5, 2) == 3
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -15) == 5
    
    def test_subtract_zero(self):
        """Test subtracting zero"""
        assert subtract(10, 0) == 10
        assert subtract(0, 5) == -5


class TestMultiplication:
    """Test cases for the multiply function"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(4, 5) == 20
        assert multiply(3, 7) == 21
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-4, -5) == 20
        assert multiply(-3, 2) == -6
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
    
    def test_multiply_by_one(self):
        """Test multiplying by one"""
        assert multiply(7, 1) == 7
        assert multiply(1, 9) == 9


class TestDivision:
    """Test cases for the divide function"""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(20, 4) == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, -2) == 5
        assert divide(-20, 4) == -5
    
    def test_divide_by_one(self):
        """Test dividing by one"""
        assert divide(10, 1) == 10
        assert divide(-7, 1) == -7
    
    def test_divide_zero_numerator(self):
        """Test dividing zero by a number"""
        assert divide(0, 5) == 0
        assert divide(0, -3) == 0
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises an exception"""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


# Edge cases and integration tests
class TestEdgeCases:
    """Test edge cases and special scenarios"""
    
    def test_large_numbers(self):
        """Test with very large numbers"""
        assert add(1000000, 2000000) == 3000000
        assert multiply(1000, 1000) == 1000000
    
    def test_float_numbers(self):
        """Test with floating point numbers"""
        assert add(1.5, 2.5) == 4.0
        assert divide(10, 3) == pytest.approx(3.333, rel=1e-2)
    
    def test_chained_operations(self):
        """Test chaining multiple operations"""
        result = add(10, 5)
        result = subtract(result, 3)
        result = multiply(result, 2)
        result = divide(result, 4)
        assert result == 6
