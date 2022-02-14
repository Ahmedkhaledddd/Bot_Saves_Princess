from math import floor
# We can use int() instead

def displayPathtoPrincess(n, grid):
    # X,y = grid.index('p')
    loc = []
    X = floor(n / 2) #starting from the middle "rows"
    Y = floor(n / 2) #starting from the middle "columns
    for i in range(n):
        for j in range(n):
            if grid[i][j] =='p':
                #getting the location of the princess
                loc.append(i)
                loc.append(j)
    # print(loc)

    while loc[0] < X:
        print("UP")
        X -= 1
    while loc[0] > X:
        print("DOWN")
        X += 1
    while loc[1] > Y:
        print("RIGHT")
        Y += 1
    while loc[1] < Y:
        print("LEFT")
        Y -= 1


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)