from random import randint

end=False
guess=[]
a=0
r=0
c=0

def Welcome():
    print("\n \nWelcome to the Game of Battleships")
    start=input("Press X to start the game ")
    return start

def Rules():
    print('''\n \n1. Each player places the 5 ships somewhere on their board.  
2.The ships can only be placed vertically or horizontally. 
3.Diagonal placement is not allowed. 
4.No part of a ship may hang off the edge of the board.  
5.Ships may not overlap each other.  
6.No ships may be placed on another ship. 
7.Once the guessing begins, the players may not move the ships.
8.The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).  \n\n''')

def Loc():
    r=str(randint(0,4))
    a=chr(65+randint(0,4))
    return a,r

def board():
    x=[[0,0,0,0,0]]
    for i in range(4):
       x.append([0,0,0,0,0])
    return x

def board_print():
    for i in range(0,5):
        print((str(board()[i])[1:-1]).replace(',',"   "),"\n\n")

def Input():
    Al=input("Enter Your Guess ")  
    num=input("Enter Your Guess ")
    return Al,num

N=Loc()

def X(m):
    while(end==False and m<5):
        if Input()==N:
            print("Ship sunken")
            m+=1
        else:
            print("Missed") 
    else:
        print("You lost")
    return m    


def Game(n):
    x=Welcome()
    if x=="X":
        Rules()
        board_print()
        n=X(n)

Game(c)        
