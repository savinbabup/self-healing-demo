def add(a, b):
    # BUG 1: The "Fat Finger" Error (Multiplication instead of Addition)
    return a / b

def subtract(a, b):
    # BUG 2: The "Incomplete Thought" (Forgot to actually subtract b)
    return a * b

def multiply(a, b):
    # BUG 3: The "Wrong Operator" (Power instead of Multiplication)
    # returns a to the power of b (e.g., 3^4 = 81 instead of 12)
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a * b

def power(a, b):
    # BUG 4: The "Bitwise XOR" Trap
    # In Python, '^' is XOR, not Power! 2^3 is 1, not 8.
    return a ^ b

if __name__ == "__main__":
    print("🧪 Running internal tests...")

    # Test 1: Addition
    try:
        assert add(2, 3) == 5
    except AssertionError:
        print(f"❌ Test Failed: add(2, 3) returned {add(2, 3)}, expected 5")
        exit(1)

    # Test 2: Subtraction
    try:
        assert subtract(10, 3) == 7
    except AssertionError:
        print(f"❌ Test Failed: subtract(10, 3) returned {subtract(10, 3)}, expected 7")
        exit(1)

    # Test 3: Multiplication
    try:
        assert multiply(3, 4) == 12
    except AssertionError:
        print(f"❌ Test Failed: multiply(3, 4) returned {multiply(3, 4)}, expected 12")
        exit(1)

    # Test 4: Power
    try:
        assert power(2, 3) == 8
    except AssertionError:
        # Returns 1 (XOR) instead of 8
        print(f"❌ Test Failed: power(2, 3) returned {power(2, 3)}, expected 8")
        exit(1)

    print("✅ All tests passed!")