def palindrome(string):
    return 1 if string == string[::-1] else 0

num = input("Enter your Number or string")
print("The number is "+ "Palindrome" if palindrome(num) else " Not Palindrome")