x="acbcf"
y="abcdaf"

#question:print shortest common supersequence
#answer="acbcdaf"
table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0 or j==0:
            table[i][j]=0

for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=1+table[i-1][j-1]
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])
i=len(y)
j=len(x)
scs=""
while(i>0 and j>0):
    if x[j-1]==y[i-1]:
        scs+=x[j-1]
        i-=1
        j-=1
    elif table[i][j-1]>table[i-1][j]:
        scs+=x[j-1]
        j-=1
    else:
        scs+=y[i-1]
        i-=1
print(scs[::-1])
