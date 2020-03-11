x=input()
c,l=[],[]
for i in range(len(x)):
    l=[]
    for j in range(i,len(x)):
        if(x[j] not in l):
            l.append(x[j])
        else:
            break
    c.append(len(l))
print(max(c))
