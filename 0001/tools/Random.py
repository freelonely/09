import random
import string

list=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
def randomSample():
    string = ''.join(random.sample(list,16))+''.join(random.sample(list,16))
    return string

list2=['1','2','3','4','5','6','7','8','9','0']

def randomSample2():
    string = ''.join(random.sample(list2,6))
    return string

# print(randomSample())