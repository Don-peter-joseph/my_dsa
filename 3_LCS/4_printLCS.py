x="acbcf"
y="abcdaf"

#question: print lcs
#output :abcf

table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0 or j==0:
            table[i][j]=0

for i in range(1,len(y)+1)  :
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=table[i-1][j-1]+1
        else:
            table[i][j]=max(table[i-1][j],table[i][j-1])

print(table)
i=len(y)
j=len(x)
lcs=""
while(i>=1 and j>=1):
    if x[j-1]==y[i-1]:
        lcs+=x[j-1]
        i-=1
        j-=1
    else:
        if table[i][j-1]>table[i-1][j]:
            j-=1
        else:
            i-=1
            
print(lcs[::-1])


















"""Another method"""
# maxstring=""
# table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

# for i in range(len(y)+1):
#     for j in range(len(x)+1):
#         if i==0 or j==0:
#             table[i][j]=""

# for i in range(1,len(y)+1):
#     for j in range(1,len(x)+1):
#         if x[j-1]==y[i-1]:
#             table[i][j]=max(x[j-1]+table[i-1][j-1],table[i-1][j],table[i][j-1])
#             if len(table[i][j])>=len(maxstring):
#                 maxstring=table[i][j]
#         else:
#             table[i][j]=max(table[i-1][j],table[i][j-1])
# print(maxstring[::-1])
# print(table)