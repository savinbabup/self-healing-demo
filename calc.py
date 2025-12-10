def divide(a, b):
    return a / b  # Intentionally unsafe

if __name__ == "__main__":
    print(divide(10, 0))  # This will CRASH with ZeroDivisionError
