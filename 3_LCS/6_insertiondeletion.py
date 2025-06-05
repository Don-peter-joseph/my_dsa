x="bolder"
y="brimer"

# x="heap"
# y="pea"

#question: find the no of insertion and deletion to make x==y
#answer:3  ('h' deleted,'p' inserted ,'p' deleted)



table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]


#My method
"""
for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0:
            table[i][j]=len(x)
        if j==0:
            table[i][j]=len(y)
        if i==0 and j==0:
            table[i][j]=0

for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=table[i-1][j-1]
        else:
            table[i][j]=min(1+table[i][j-1],2+table[i-1][j-1])

print(table[len(y)][len(x)])
"""


#original method
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

# print(table[len(y)][len(x)])
lcs=table[len(y)][len(x)]
output=len(x)-lcs+len(y)-lcs
print(output)