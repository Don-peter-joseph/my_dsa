#find longest increasing subsequence's length
#eg [4,2,7,4,3,5] ans: longest increasing subsequence is [2,3,5] , therefore len is 3

arr=[4,2,7,4,3,5]

table=[[-1 for i in range(len(arr)+1)]]*(len(arr)+1)

for i in range(len(arr)+1):
    for j in range(len(arr)+1):
        