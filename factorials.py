# Problem: Write a Python function that calculates the factorial of a number using recursion.
# Example: factorial(5) should return 120.
# Example: factorial(9) should return 5040.
# Example: factorial(0) should return 1.

def get_factorial(val):
  if val < 0:
    return "Numbers below 0 does not have factorial"
  elif val == 0:
    return 1
  else:
    return val * get_factorial(val - 1)
    
print(get_factorial(7))