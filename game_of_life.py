def neighbours(i,j):            # For getting the neighbours position
    lis = [
        [i-1 , j-1], [i-1 , j], [i-1 , j+1],
        [i , j-1], [i , j+1],
        [i+1 , j-1],[i+1 , j],[i+1 , j+1],
    ]
    return lis

def check_neighbours_state(i, j, lis, row, col):        # Finding the alive/dead cells
    pos = neighbours(i, j)
    alive = 0
    dead = 0
    for x in range(0,len(pos)):
        if pos[x][0] >= 0 and pos[x][0] < row and pos[x][1] >= 0 and pos[x][1] < col :
            _value = lis[pos[x][0]][pos[x][1]]
            if _value == 1:
                alive = alive + 1
            else:
                dead = dead + 1
        else:
            continue
    return alive
  

def Game(row, col, lis):
    newList = []
    for i in range(0,row):
        rows = []
        for j in range(0,col):
            alive = check_neighbours_state(i, j, lis, row, col)
            if alive < 2 :                          # Under Population
                rows.append(0)      
            elif alive == 2 or alive == 3:          # if alive  = 2 Nothing Happends (Lives On Next Gen)
                if alive == 3 and lis[i][j] == 0:   # Reproduction
                    rows.append(1)
                elif alive == 2:
                    rows.append(lis[i][j])
                else:
                    rows.append(lis[i][j])
            else:
                if lis[i][j] == 1 and alive >3:     # Over Population
                    rows.append(0)
                else:
                    rows.append(0)
        newList.append(rows)
    return newList


def display(lis,row,cols):
    for x in range(0,row):
        for y in range(0, cols):
            print(lis[x][y], end="\t")
        print("\n")


    