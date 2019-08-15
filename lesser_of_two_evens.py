def lesser_of_two_evens(a,b):

    '''
    returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
    '''

    if a %2 == 0 and b %2 == 0:
        number = min(a, b)
    else:
        number = max(a, b)
    return number
