#!/usr/bin/env python3

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

# Function to convert decimal to Roman Numerals
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))
def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be 1..3999)')
    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

# Main ()
if __name__ == "__main__":
    '''Try to find any number between 1 to 3999 and function should fail on any other value'''
    print("Roman equivalent of 3999 is %s" %(to_roman(3999)))
    print("Roman equivalent of 100 is %s" %(to_roman(100)))

    '''Uncomment below should return an error'''
    #print("Roman equivalent of 0.5 is %s" %(to_roman(0.5)))
