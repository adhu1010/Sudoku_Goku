import numpy as np
grid=[]
for i in range(1,10):
    row=[]
    for j in range(1,10):
        print("Enter the number for",j,"th element of",i,"th row")
        x=int(input())
        row.append(x)
    grid.append(row)
        
print(np.matrix(grid))
def possible(y,x,n):
    global grid
    for i in range (9):
        if grid[y][i]==n:
            return False
    for i in range(9):
        if grid[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid [y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    print(np.matrix(grid))  
                          
solve()