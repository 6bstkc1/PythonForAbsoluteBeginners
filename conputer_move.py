# Tic-Tac-Toe

# Pseudocode

# display the game instructions
# determine who goes first
# create an empty tic-tac-toe board
# display the board
# while nobody's won and it's not a tie
    # if its the human's turn
        # get the human's move
        # updatethe board with the move
    # otherwise
        # calculate the computer's move
        # update the board witht he move
    # display the baord
    # switch turns
# congratulatie the winner or declare a tie

# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent

# global constants
X = "X"             
O = "O"             
EMPTY = " "         # Represents an empty square on the board.
TIE = "TIE"         # Represents a tie game.
NUM_SQUARES = 9     # Number of squares on the tic-tac-toe board.


def display_instruct():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    You will make your move known by entering a number, 0 - 8. The number
    will correspond to the baord position as illustrated:
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
    Prepare yourself, human. The ultimate bettle is about to begin. \n
    """
    )

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    if response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Create new game board."""
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Create a list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4 ,6))
    for row in WAYS_TO_WIN: # if one row in WAYS_TO_WIN are all equal and not
                            # empty, the winner is equal to symbol filling the
                            # squares.
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board: # if not empty squares on the board, it's a tie
            return TIE

    return None # there isn't a winner yet

def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose"
                  " another. \n")
    print("Fine...")
    return move

def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    CENTER = 4
    CORNERS = (0,2,6,8)
    SIDEs = (1,3,5,7)
    
    print("I shall take square number", end=" ")

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY


    ai_move = recursive_move(board,computer,human,[])
    print(ai_move)
    return ai_move

    
    """  # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move """

def recursive_move(board,computer,human,moves = []):
    
    for computer_move in legal_moves(board): #move the computer to a legal spot

        stack = moves # for each possible computer move save the inital move
        stack.append(computer_move)
        print(stack)
        
        board[computer_move] = computer
        
        if winner(board) == computer or EMPTY not in board: # if the computer wins or ties return the inital move and clean up the previous move
                board[computer_move] = EMPTY
                print(stack[0])
                return stack[0]
            
        # if the game is ongoing nothing then the human moves
        for human_move in legal_moves(board): #move the human to a legal spot
            board[human_move] = human

            stack.append(human_move) # add the move to the stack
            
            if winner(board) == human: # if the human wins the game, pop stack, clear the old move and check another path
                print("Detecting human winner", stack)
                board[human_move] = EMPTY
                stack.remove(human_move)
                continue
            
            elif EMPTY not in board: # if human ties then computer makes initial move
                board[human_move] = EMPTY
                print("Found a tie")
                return stack[0]
            
            else: # the game is still ongoing
                return recursive_move(board,computer,human,stack)
                
                
                
            
            
        

def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n"\
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" \
              "But never again! I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" \
              "Celebrate today... for this is the best you will ever achieve.")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# start the program
main()

input("\n\nPress the enter key to quit.")
