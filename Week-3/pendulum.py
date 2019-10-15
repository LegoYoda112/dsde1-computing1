import math

def period(L, g):

    # Check that both L and g are either ints or floats
    # otherwise, throw a TypeError
    if( not ((type(L) is int) or (type(L) is float))):
        raise TypeError("L must be an int or a float")

    if(not ((type(g) is int) or (type(g) is float))):
        raise TypeError("g must be an int or a float")

    
    # Check that both L and g are positive (because of the square root)
    # and that g is non-zero (because of the division)
    # if they are not, throw a ValueError
    if(L < 0):
        raise ValueError("L must be non-negative")
    if(g == 0):
        raise ValueError("g must be non-zero")
    if(g < 0):
        raise ValueError("g must be non-negative")

    T = 2 * math.pi * math.sqrt(L / g)

    return T