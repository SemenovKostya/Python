from random import randint
from pprint import pprint
a = [[randint(1,100)for x in range(10)] for y in range (5)]
for x in a:
    for i in range(len(x)):
        if x[i] % 2 != 0:
            x[i] = -x[i]
pprint(a)

