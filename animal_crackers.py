def animal_crackers(text):
    '''
    takes a two-word string and returns True if both words begin with same letter
    '''

    words = text.split(" ")
    a = words[0][0]
    b = words[1][0]

    if a == b:
        result = 'True'
    else:
        result = 'False'
    
    return result
