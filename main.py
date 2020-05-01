#Autor:Evgeni Pogoster
#Tic Tac Toe Game 

#Initilization of paramaeters
isWinner=False;
turn=0;
playingBoard=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']];

nameA=input("player A, Enter your name: ");
nameB=input("player B, Enter your name: ");

#Prints the Board
def print_board():
    print(' '+' 1 '+'  2 '+'  3');
    print('1 '+playingBoard[0][0]+' | '+playingBoard[0][1]+' | '+playingBoard[0][2]);
    print('  '+'---------');
    print('2 '+playingBoard[1][0]+' | '+playingBoard[1][1]+' | '+playingBoard[1][2]);
    print('  '+'---------');
    print('3 '+playingBoard[2][0]+' | '+playingBoard[2][1]+' | '+playingBoard[2][2]);

#Checking if there is a winner
def CheckWin():
    for i in range(2):
        if ((playingBoard[i][0]==playingBoard[i][1]) and (playingBoard[i][1]==playingBoard[i][2]) and playingBoard[i][0]!=' '):
            return True;
        elif ((playingBoard[0][i]==playingBoard[1][i]) and (playingBoard[1][i]==playingBoard[2][i]) and playingBoard[0][i]!=' '):
            return True;
    if ((playingBoard[0][0]==playingBoard[1][1]) and (playingBoard[1][1]==playingBoard[2][2]) and playingBoard[0][0]!=' '):
        return True;
    elif ((playingBoard[0][2]==playingBoard[1][1]) and (playingBoard[1][1]==playingBoard[2][0]) and playingBoard[0][2]!=' '):
        return True;
    else:
        return False;

#Game Process
while not(isWinner):
    print_board();
    if(turn%2==0):
        print(nameA+' it is your turn');
        print('Where to put X?');
        i = int(input("Enter a row number: "));
        j = int(input("Enter a column number: "));
        if (isinstance(i, int) and isinstance(j, int)):
            i=i-1;
            j=j-1;
        if (0<=j and j<3 and 0<=i and i<3):
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
    if(turn<4):
        turn=turn+1;
        continue;
    
    if (CheckWin()):
        print_board();
        if(turn%2==0):
            print (nameA+' is the Winner!');
        else:
            print (nameB+' is the Winner!');
        isWinner==True;
        break;
    if(turn==8):
        print_board();
        print("It's a Draw!");
        break;
        
    turn=turn+1;
