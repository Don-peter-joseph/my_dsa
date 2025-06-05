# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, helper):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, helper, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, helper, destination, source)
        
# Driver code
n = 4
TowerOfHanoi(n,'A','C','B') 
# A, C, B are the name of rods