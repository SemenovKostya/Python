'''from math import ceil
a = float(input("Enter the digital "))
a = ceil(a+2.3)
print(a)'''


from math import tan
from math import radians
a = float(input('Enter the degrees: '))
a = radians(a)
r = tan(a)
print(r)



from math import factorial
x = int(input("enter: "))
v = factorial(x)
print(v)



from random import randint

for i in range(10):
    print(randint(1, 10), end=',')



from random import choice
from random import sample
a = [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,189,200]
b = choice(a)
c = sample(a,5)
d = sample(a,10)
print(b,c,d,sep = '\n')


