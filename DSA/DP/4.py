#count of n_ queens configurations

col=4
row=4
board=[[0 for _ in range(col)]for j in range(row)]
count=0


def placable(row,column):
    global board
    for i in range(row):
        if board[i][column]==1:
            return False
    
    i=row
    j=column
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    i=row
    j=column
    while(i>=0 and j<col):
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    return True

def n_queens(row):
    global board,count
    count+=1
    if row==len(board):
        return 1
    total=0
    for i in range(col):
        if placable(row,i):
            board[row][i]=1
            total+=n_queens(row+1)
            board[row][i]=0
    return total


ans=n_queens(0)
print(ans,count)
# print(board)