import numpy as np
grid=[[],[],[],[],[],[],[],[],[]]
for i in range(1,10):
    for j in range(1,10):
        x=int(input("Enter the number  :"))
        grid[i][j]=x
        
print(np.matrix(grid))