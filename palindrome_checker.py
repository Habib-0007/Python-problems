# Write a function that checks if a given string is a palindrome.

def palindrome(word):
  main_list = list(word.lower())
  pal_list = main_list[::-1]
  
  if main_list == pal_list:
    return "This is a palindrome"
  else:
    return "This is not a palindrome"

print(palindrome("Hannah"))
print(palindrome("Beget"))
print(palindrome("wow"))
print(palindrome("now"))