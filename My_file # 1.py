f = open('qwerty.txt','r',encoding = 'utf-8')
s = f.read()
count = 0
for i in range (len(s)):
    for j in range(i+1, len(s) - 1):
        if s[i] == 'K':
            if s[j] == 'O':
                count+= 1
        else:
            continue
print(count)
