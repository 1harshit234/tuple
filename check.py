l = (10,10,1)
f = len(l)-1
for i in range(1,f):
    for j in range(f,-1,-1):
        if (l[i] != l[j]):
            return False
           
