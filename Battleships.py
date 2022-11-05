from random import randint

board=[]

for i in range(5):
    board.append(["O"]*5)    

def p_board(x):
    for i in x:
        print("    ".join(i))

p_board(board)        

    