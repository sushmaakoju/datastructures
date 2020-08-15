
def least_significan_bit(n):
    """Least significant bit of a number
       num AND -num = LSB 

    Args:
        n ([type]): [description]

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if type(n) != int:
        raise TypeError("Number must be Integer.")
    if n > 0 :
        return (n&-n)
    
def least_significant_bit_index(n):
    ((1 + (n ^ (n-1))) >> 1).bit_length()

def is_even(n):
    """Find if specified number is even using Bitwise XOR operator.
       number XOR == n + 1
    Args:
        n (integer): [description]

    Returns:
        boolean: True if even
    """
    if type(n) != int:
        raise TypeError("Number must be Integer.")
    return n ^ 1 == n + 1

def is_odd(n):
    """Find if given number is odd using Bitwise AND operator.
       If least significant bit is set, return True.

    Args:
        n(integer) : integer number

    Returns:
        boolean: True if odd
    """
    if type(n) != int:
        raise TypeError("Number must be Integer.")
    return (n & 1) ==  1
