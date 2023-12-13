f = open('Script.txt','r',encoding = 'utf-8')   
s = f.read()
JJ = s.split()
word_count = {}
for i in (JJ):
    word_count[i] = word_count.get(i,0) +1
    print(i, word_count[i])
    

