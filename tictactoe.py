"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

counter=0


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board==initial_state():
        return X

    xcounter = 0
    ocounter = 0
    for row in board:
        xcounter += row.count(X)
        ocounter += row.count(O)
    return X if xcounter==ocounter else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()

    if terminal(board):
        return actions

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                actions.add((i,j))
    
    
    return actions
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
   
    new_board=copy.deepcopy(board)
    (i,j)=action

    if len(action)!=2 or i>2 or j>2 or i<0 or j<0 or board[i][j]!=EMPTY:
        raise Exception("Invalid action passed to result")

    if player(board)==X:
        
        new_board[i][j]=X
        return new_board
    elif player(board)==O:
        new_board[i][j]=O
        return new_board
    else:
        return None



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows

    for row in board:
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O
    
    columns=[]

    for i in range(len(board)):
        column=[row[i] for row in board]
        columns.append(column)

    # check columns
    for row in columns:
        if row.count(X)==3:
            return X
        elif row.count(O)==3:
            return O

    #check diagonals

    if board[0][0]==X and board[1][1]==X and board[2][2]==X:
        return X
    if board[0][0]==O and board[1][1]==O and board[2][2]==O:
        return O
    if board[0][2]==X and board[1][1]==X and board[2][0]==X:
        return X
    if board[0][2]==O and board[1][1]==O and board[2][0]==O:
        return O






def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)is not None:
        return True
    
    if sum([row.count(EMPTY) for row in board])==0:
        return True

    return False
    



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1 +sum([row.count(EMPTY) for row in board])
    elif winner(board)==O:
        return -1 -sum([row.count(EMPTY) for row in board])
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
   
   
    best_move=None

    if player(board)==X:

       
       best_value=-math.inf
       for action in actions(board):
           k=max_value(board)
           if k > best_value:
               best_value=k
               best_move=action

    elif player(board)==O:
        best_value=math.inf
        for action in actions(board):
            k=min_value(board)
            if k < best_value:
                best_value=k
                best_move=action

    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,min_value(result(board,action))) 
    return v 

def min_value(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,max_value(result(board,action))) 
    return v 

