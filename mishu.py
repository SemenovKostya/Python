f = open('Script.txt','r',encoding = 'utf-8')   
JJ = f.read()

letter_count = {letter: JJ.lower().count(letter) for letter in set(JJ.lower()) if letter.isalpha()}
letter_countB = {letter: JJ.upper().count(letter) for letter in set(JJ.upper()) if letter.isalpha()}

print(letter_count)
print(letter_countB)

unused_letters = ''.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - set(JJ.lower())))
print(unused_letters)

A = []
for i in letter_count:
    A.append(i)
    A.sort()
print(A)
print(len(A))

Aa = []
for i in letter_countB:
    Aa.append(i)
    Aa.sort()
print(Aa)
print(len(Aa))
    
