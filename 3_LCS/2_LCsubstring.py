x="aabcc"
y="abcac"

#question: Find the length of longest common substring
#output :3 ,lc substring= abc
maxlength=0

table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0 or j==0:
            table[i][j]=0


for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=max(1+table[i-1][j-1],table[i-1][j],table[i][j-1])
            if table[i][j]>maxlength:
                maxlength=table[i][j]
        else:
            table[i][j]=0

print(maxlength)
print(table)        