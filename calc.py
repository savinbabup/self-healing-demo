def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # Test cases
    assert add(2, 3) == 5, "add(2, 3) should equal 5"  
    assert add(10, 5) == 15, "add(10, 5) should equal 15"  
    assert subtract(10, 3) == 7, "subtract(10, 3) should equal 7"
    print("All tests passed!")