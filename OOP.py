'''from random import randint
for i in range(10):
    print(randint(i,10))
    
class Classy:
    def visible(self):
        print('You are visible! Its not working')
    def invisble(self):
        print('You are invisible! Its working')
    
object = Classy()
k = object.visible
k()
''''''
class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
'''
word = 'Mississippi'
print(word.lstrip('ips'))
