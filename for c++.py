def score(a,c,b):
    if c == '+':
        k = a + b
    if c == '-':
        k = a - b
    if c == '*':
        k = a * b
    if c == '/':
        k = a / b
    return k

a = int(input("Enter the first digital: "))
while True:
    c = str(input("Enter the sign of operation (+,-,*,/) : "))
    if c == 'Q':
        print("Last result equals: ",a)
        break
    if c == 'C':
        print("Starting again")
        a = int(input("Enter the first digital: "))
        c = str(input("Enter the sign of operation (+,-,*,/) : "))
        b = int(input("Enter the second digital: "))
        a = score(a,c,b)
        print(a)
    else :
        b = int(input("Enter the second digital: "))
        a = score(a, c, b)
        print(a)


