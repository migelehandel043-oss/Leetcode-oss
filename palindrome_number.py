def isPalindrome(x: int) -> bool:
    # Palindrome numbers must be non-negative.
    # For example, -121 is not a palindrome because of the '-' sign.
    if x < 0:
        return False
    
    # Convert the integer into a string.
    # Example: 121 -> "121"
    s = str(x)
    
    # Compare the string with its reverse.
    # If they are the same, it's a palindrome.
    return s == s[::-1]


# Example tests
print(isPalindrome(121))   # True (reads the same forwards and backwards)
print(isPalindrome(-121))  # False (negative numbers can't be palindromes)
print(isPalindrome(10))    # False (10 reversed is 01)
