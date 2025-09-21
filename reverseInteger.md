```python
def reverse(x: int) -> int:
    # Define 32-bit signed integer limits
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    result = 0   # this will hold the reversed number
    
    # Loop until x becomes 0
    while x != 0:
        # Extract the last digit:
        # For positive numbers → x % 10
        # For negative numbers → x % -10 gives the correct last digit
        digit = int(x % 10) if x > 0 else int(x % -10)
        
        # Remove the extracted digit from x
        # int(x / 10) ensures truncation toward zero (like in C/C++)
        x = int(x / 10)
        
        # ----- Overflow check before updating result -----
        # If result is already larger than INT_MAX//10, adding another digit will overflow
        # Or if result == INT_MAX//10 but digit > 7 (last digit of INT_MAX = 7), overflow
        if (result > INT_MAX // 10 or 
            (result == INT_MAX // 10 and digit > 7)):
            return 0
        
        # Similarly, check for underflow for INT_MIN
        # If result < INT_MIN//10, multiplying by 10 will underflow
        # Or if result == INT_MIN//10 but digit < -8 (last digit of INT_MIN = -8), underflow
        if (result < INT_MIN // 10 or 
            (result == INT_MIN // 10 and digit < -8)):
            return 0
        # ------------------------------------------------
        
        # Append the digit to the reversed number
        result = result * 10 + digit
    
    # Return the reversed integer if within range
    return result
