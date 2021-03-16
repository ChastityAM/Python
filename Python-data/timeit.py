import timeit
import random

def search_list():
    lst = [1,2,3,4,5,6,7]
    elem = random.randint(1,8)
    for e in lst:
        if e == elem: return True
    return False 

def_string = """def search_list():
    lst = [1,2,3,4,5,6,7]
    elem = random.randint(1,8)
    for e in lst:
        if e == elem: return True
    return False """

t = timeit.timeit(stmt=def_string, setup="import random", number=1000)
print(t)