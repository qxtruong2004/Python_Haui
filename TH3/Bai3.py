a = [1,2,3,4]
b = ['a','b']
i = 0
j = 0
c=[]
while(i < len(a) and j < len(b) ):
    c.append(a[i])
    c.append(b[j])
    i+=1
    j+=1
while (i < len(a)):
    c.append(a[i])
    i+=1
while (j < len(b)):
    c.append(b[j])
    j+=1
print(c)
