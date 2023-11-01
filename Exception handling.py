try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This will always be executed.")
