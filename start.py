from game_of_life import *

choice = 1
layout = []
print("enter the Rows And coluns (Eg : 4x4 or 5x5 ..) :\t")
row = int(input("Rows :\t"))
cols = int(input("Cols :\t"))

print("Input the Cells :  (\t 0 for Dead cell \t 1 for alive ) \n>\t")

for x in range(0,row):
    data = []
    for y in range(0, cols):
        data.append(int(input(" ")))
    layout.append(data)
    print("\n")

print("The layout look like")
display(layout,row,cols)

while(choice == 1):
    ch = int(input("Enter your Choice \n 1. Build Next Generation \n 2. exit\n >\t"))
    print("\n--------------------------------------------")
    if ch == 1:
        layout = Game(row, cols, layout)
        display(layout, row, cols)
        choice = 1
    elif ch == 2:
        choice = 0