import random

board=['#','X','X','O','X','O','X','O','O','X']
turn=0
game_state=True

def display_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def board_reset(board):
    for i in range(1,10):
        board[i]=' '

def auto_marker_selection():
    list=['X','O']
    m=random.sample(['X','O'],1)
    marker1=m[0]
    marker1_index=list.index(m[0])
    if(marker1_index==0):
        marker2=list[1]
    else:
        marker2=list[0]
    return marker1,marker2
def manual_marker_selection():
    marker1=input("Player 1 choose marker")
    if(marker1=='X'):
        marker2='O'
    else:
        marker2='X'
    return marker1,marker2

def begin_play():
    global game_state
    if(input("Begin Play!!!")==('yes' or 'y' or 'Y' or 'Yes' or 'YES')):
        game_state=True
        return game_state
    else:
        game_state=False
        return game_state

def replay():
    if(input("play again")==('yes' or 'y' or 'Y' or 'Yes' or 'YES')):
        game()
    else:
        exit(0)

def choose_first_turn():
    t=random.sample([1,2],1)[0]
    global turn
    if(t==1):
        turn=1
    else:
        turn=2
    return turn

def space_check(board):
    global game_state
    i=' '
    if i not in board:
        game_state=False
        return False
    else:
        game_state=True
        return True

def position_check(pos,board):
    if(board[pos]!=' '):
        return False
    else:
        return True
def turn_play(t,board,position):
    global turn
    if(t==1):
        board[position]=player1_marker
        turn=2
    else:
        board[position]=player2_marker
        turn=1

def win_check(board,marker):
    if((board[1]==board[2]==board[3]==marker) \
            or (board[4]==board[5]==board[6]==marker) \
            or (board[7]==board[8]==board[9]==marker) \
            or (board[1]==board[4]==board[7]==marker) \
            or (board[2]==board[5]==board[8]==marker)\
            or (board[3]==board[6]==board[9]==marker)\
            or (board[7]==board[5]==board[3]==marker)\
            or (board[1]==board[5]==board[9]==marker)):
        return True
    else:
        return False

def game():
    board_reset(board)
    display_board(board)
    global player1_marker
    global player2_marker
    if (input("select marker automatically??") == ('yes' or 'y' or 'Y' or 'Yes' or 'YES')):
        player1_marker, player2_marker = auto_marker_selection()
    else:
        player1_marker, player2_marker = manual_marker_selection()

    print("player 1 marker is ", player1_marker, "and player 2 marker is", player2_marker)

    if(choose_first_turn()==1):
        print("player 1 plays first")
    else:
        print("player 2 plays first")
    global game_state
    while(game_state==True):
        if(space_check(board)):
            position=int(input("where to place the marker"))
            if(position_check(position,board)):
                turn_play(turn,board,position)
                display_board(board)
                if(turn==1):
                    if(win_check(board,player2_marker)):
                        print("player 2 winsss")
                        break
                else:
                    if(win_check(board,player1_marker)):
                        print("player 1 winss")
                        break
            else:
                print("invalid position")
                continue
        else:
            print("No space left")
            print("Game tie")
            break
            replay()

    replay()




game()

