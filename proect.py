f = open('Script.txt','r',encoding = 'utf-8')
s = f.read()
count_unique = []
flag = True
flag2 = True

from nltk import TreebankWordTokenizer
wpt = TreebankWordTokenizer()
JJ = wpt.tokenize(s)

print(len(JJ)) #it means count of all words in text
print(len(set(JJ)))

'''for i in range(len(JJ)):
    if JJ.count(JJ[i]) == 1:
        count_unique.append(JJ[i])
    else:
        continue
print(len(count_unique)) #it means count of all unique words'''

def fund(index):
    if index.isdigit():
        index = int(index)
        if index < len(JJ):
            print(JJ[index])
        else:
            print("Index Error")
    else:
        print("Type Error")

j = input("Enter the index: ")
fund(j)
while flag == True:
    print('Do you want to continue?')
    answer = input('Enter your answer (Only yes/no) : ')
    if answer == 'yes':
        j = input("Enter the new index: ")
        fund(j)
    else:
        flag = False

# First part of work is ends.

def ch(index):
    if str(abs(int(index))).isdigit():
        index = int(index)
        if index < len(JJ):
            if index == -1 or index == (len(JJ) - 1):
                print("The word with last index do not has a pair")
            else:
                print( "Head: ", JJ[index])
                print( "Tail: ", JJ[index+1])
        else:
            print("Index Error")
    else:
        print("Type Error")

j = input("Enter the digital: ")
ch(j)

while flag2 == True:
    print('Do you want to continue?')
    answer = input('Enter your answer (Only yes/no) : ')
    if answer == 'yes':
        j = input("Enter the new index: ")
        ch(j)
    else:
        flag2 = False

j = 0
count = 0
while j != len(JJ) - 1:
    count+=1
    j+=1
print(count)


import nltk
from nltk import bigrams
c = nltk.bigrams(JJ)
print(len(list(c)))
















