"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    counter = 5
    while counter > -1:
        result.append(counter)
        counter -= 1
    return result  