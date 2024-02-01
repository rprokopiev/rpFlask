from random import randint

def get_array(size):
    arr = []
    for i in range(1, size+1):
        arr.append(randint(1, 10))
    return arr

def sum_array(a):
    result = 0
    for i in a:
        result += i
    return result
