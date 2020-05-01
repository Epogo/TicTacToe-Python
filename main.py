'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Autor:Evgeni Pogoster
#Tic Tac Toe Game 
#Input players names




isWinner=False;
turn=0;
playingBoard=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']];

nameA=input("player A, Enter your name: ");
nameB=input("player B, Enter your name: ");
def print_board():
    print(' '+' 1 '+'  2 '+'  3');
    print('1 '+playingBoard[0][0]+' | '+playingBoard[0][1]+' | '+playingBoard[0][2]);
    print('  '+'---------');
    print('2 '+playingBoard[1][0]+' | '+playingBoard[1][1]+' | '+playingBoard[1][2]);
    print('  '+'---------');
    print('3 '+playingBoard[2][0]+' | '+playingBoard[2][1]+' | '+playingBoard[2][2]);

def CheckWin:

#Game Process
while not(isWinner):
    print_board();
    if(turn%2==0):
        print(nameA+' it is your turn');
        print('Where to put X?');
        i = int(input("Enter a row number: "))-1;
        j = int(input("Enter a column number: "))-1;
        if (0<=j and j<3 and 0<=i and i<3 and isinstance(i, int) and isinstance(j, int)):
            if(playingBoard[i][j]!=' '):
                print("Sorry, Cell is occupied");
                continue;
            else:
                playingBoard[i][j]='X';
        else:
            print("Illegal Input");
            continue;
        
    else:
        print(nameB+' it is your turn');
        print('Where to put O?');
        i = int(input("Enter a row number: "))-1;
        j = int(input("Enter a column number: "))-1;
        if (0<=j and j<3 and 0<=i and i<3 and isinstance(i, int) and isinstance(j, int)):
            if(playingBoard[i][j]!=' '):
                print("Sorry, Cell is occupied");
                continue;
            else:
                playingBoard[i][j]='O';
        else:
            print("Illegal Input");
            continue;
        
    turn=turn+1;
        
    




