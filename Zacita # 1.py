f = open('Script.txt','r',encoding = 'utf-8')   
s = f.read()
count_unique = []
flag = True

'''import nltk
from nltk import TreebankWordTokenizer  # import NLTK
wpt = TreebankWordTokenizer()
JJ = wpt.tokenize(s)'''

JJ = s.split()
print(len(JJ)) #it means count of all words in text

word_count = {}
for token in JJ:
    word_count[token] = word_count.get(token, 0) + 1
unique_tokens = 0
for word, count in word_count.items():
    if count == 1:
        unique_tokens += 1
print(unique_tokens) #it means count of all unique words in text


def FW(index): #function named after Find Word
    if index.isalpha() == False:
        if str(abs(int(index))).isdigit() :
            index = int(index)
            if index < len(JJ) and index >= - len(JJ):
                print(JJ[index])
            else:
                print("Index Error")
    else:
        print("Type Error")

j = input("Enter the digital: ")
FW(j)

while flag == True:
    print('Do you want to continue?')
    answer = input('Enter your answer (Only yes/no) : ')
    if answer == 'yes':
        j = input("Enter the new digital: ")
        FW(j)
    else:
        flag = False
        
# First part of work is ends._______________________________________________________________________________________________________________________________________________________________________________________

def HT(index): #function named after Head and Tail
    if index.isalpha() == False:
        if str(abs(int(index))).isdigit():
            index = int(index)
            if index < len(JJ) and index >= - len(JJ):
                if index == -1 or index == (len(JJ) - 1):
                    print("The word with last index do not has a pair")                    
                else:
                    print( "Head: ", JJ[index])
                    print( "Tail: ", JJ[index+1])
            else:
                print("Index Error")
    else:
        print("Type Error")
        
flag2 = True        
j = input("Enter the digital: ")
HT(j)

while flag2 == True:
    print('Do you want to continue?')
    answer = input('Enter your answer (Only yes/no) : ')
    if answer == 'yes':
        j = input("Enter the new digital: ")
        HT(j)
    else:
        flag2 = False

import nltk
from nltk import bigrams
c = nltk.bigrams(JJ)
print("Count of Binagrams equals: ", len(list(c)))

# Second part of work is ends.______________________________________________________________________________________________________________________________________________________________________________________

j = input("Enter the word: ")
m = []
if j not in JJ:
    print("KeyError. Запрашиваемое слово отсутствует в модели. Пожалуйста, введите другое слово.")
else:
    for i in range(len(JJ)):
        if JJ[i] == j:
            m.append(JJ[i+1])
    NM = set(m)

    Extendedm = []
    for i in NM:
        M = []
        M.append(i)
        count = m.count(i)
        M.append(count)
        Extendedm.append(M)
        M = []
    dictionary2 = dict(Extendedm)

    for i in dictionary2:
        print("Head: ",j)
        print("Tail: ",i, "Count: ",dictionary2[i])

# Third part of work is ends._______________________________________________________________________________________________________________________________________________________________________________________

def FHB(j): #function named after Find Highest Binars
    A = []
    count_words = 1
    while count_words != 10:
        j = ''.join(j)
        if A == []:
            A.append(j)
        m = []
        for i in range(len(JJ)):
            if JJ[i] == j:
                m.append(JJ[i+1])
        NM = set(m)
        Extendedm = []
        for i in NM:
            M = []
            M.append(i)
            count = m.count(i)
            M.append(count)
            Extendedm.append(M)
            M = []
        dictionary2 = dict(Extendedm)
        zcount = -1
        zword = ''
        for i in dictionary2:
            if dictionary2[i] > zcount:
                zword = i
                zcount = dictionary2[i]
        A.append(zword)
        count_words+=1
        j = zword
    A = ' '.join(A)
    return A
    
from random import choices
for i in range(3):
    j = choices(JJ)
    print(j)
    print(FHB(j))
    print(" ")
    
# Fourth part of work is ends._______________________________________________________________________________________________________________________________________________________________________________________       

def FHB(j):
    A = []
    count_words = 1
    while count_words != 10:
        j = ''.join(j)
        if A == []:
            A.append(j)
        m = []
        for i in range(len(JJ)):
            if JJ[i] == j:
                m.append(JJ[i+1])
        NM = set(m)
        Extendedm = []
        for i in NM:
            M = []
            M.append(i)
            count = m.count(i)
            M.append(count)
            Extendedm.append(M)
            M = []
        dictionary2 = dict(Extendedm)
        zcount = -1
        zword = ''
        if count_words == 9:
            for i in dictionary2:
                if dictionary2[i] > zcount and '?' in i or '.' in i or '!' in i and i.islower():
                    zword = i
                    zcount = dictionary2[i]
            A.append(zword)
            count_words+=1
        else:
            for i in dictionary2:
                if dictionary2[i] > zcount:
                    zword = i
                    zcount = dictionary2[i]
            A.append(zword)
            count_words+=1
        j = zword
    A = ' '.join(A)
    return A
    

from random import choices
k = 0
while k != 10:
    j = choices(JJ)
    j = ''.join(j)
    if j.istitle() and j.isalpha():
        print(FHB(j))
        k+=1

    
# Fifth part of work is ends._______________________________________________________________________________________________________________________________________________________________________________________       

    
    
        
    


