# Write a program that takes a user input (a number) and prints whether the number is even or odd.

def odd_or_even(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"
    
print(odd_or_even(5))
print(odd_or_even(8))
print(odd_or_even(16))
print(odd_or_even(27))