def add(a, b):
    # BUG 1: Logic Error (Subtraction instead of Addition)
    return a - b

def subtract(a, b):
    # BUG 2: Argument Swap (Returns b - a instead of a - b)
    return b - a

def multiply(a, b):
    # BUG 3: Copy-Paste Error (Still doing addition instead of multiplication)
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def average(a, b):
    # BUG 4: Order of Operations (Missing parentheses!)
    # Computes a + (b/2) instead of (a+b)/2
    return a + b / 2

if __name__ == "__main__":
    print("🧪 Running internal tests...")

    # Test 1: Addition
    try:
        assert add(2, 3) == 5
    except AssertionError:
        print(f"❌ Test Failed: add(2, 3) returned {add(2, 3)}, expected 5")
        exit(1) # Fail immediately so CI catches it

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

    # Test 4: Average
    try:
        assert average(10, 20) == 15
    except AssertionError:
        # returns 20.0 (10 + 10) instead of 15.0
        print(f"❌ Test Failed: average(10, 20) returned {average(10, 20)}, expected 15")
        exit(1)

    print("✅ All tests passed!")