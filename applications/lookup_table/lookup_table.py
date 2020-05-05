import math
import random
import time
my_dict = {}
def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    try:
        return my_dict[x][y]
    except KeyError:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        try:
            my_dict[x][y] = v
        except KeyError:
            my_dict[x] = {}
            my_dict[x][y] = v
        return v


# Do not modify below this line!
start = time.time()
for i in range(50000): 
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    # if time.time()-start > 60:
    #     break

print(my_dict)
