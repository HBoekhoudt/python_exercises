def makes_twenty(n1,n2):
    '''
    Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    '''
    
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
            result = 'True'
    else:
        result = 'false'
    
    return result