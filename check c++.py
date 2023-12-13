a = []
k = 0
dr_ch = 0
while k != 5:
    b = float(input('Number: ' ))
    a.append(b)
    k += 1
    b = 0
print(a)
for i in range(len(a)):
    if a[i] - int(a[i]) > dr_ch:
        dr_ch = round(a[i] - int(a[i]),3)
print(dr_ch)
    
