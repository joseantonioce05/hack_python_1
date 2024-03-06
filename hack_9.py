"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    counter = 1
    while counter <= 3:
        index = result.index(counter)
        index += 1
        result.insert(index, "@")
        counter += 1
    return result  

f = fn_hack_9()
print(f)