#creating gameboard as 2d list
def make_board():
  gameboard = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
  return gameboard

def print_board(gameboard):
	header = ' '
	for num in range(1, len(gameboard) + 1):
	    header += ' '+ str(num) +'  '
	print(header)
	print('+---' * (len(gameboard)) + '+')

	for row in range(len(gameboard[0])):
	    pass
	    items_in_rows = ''
	    for col in range(len(gameboard)):
	        items_in_rows += ('| '+str(gameboard[col][row])) + ' '
	    print(items_in_rows + '|')
	    print('+---' * (len(gameboard)) + '+')

#is the move valid based on column availability 
def is_move_valid(gameboard, move):
	# The column doesn't exist
    if move < 1 or move > (len(gameboard)):
        return False

    # The column is full
    if gameboard[move-1][0] != ' ':
        return False
    return True

def select_space(gameboard, column, player):
	# Check to see if the move is valid
    if not is_move_valid(gameboard, column):
        print("Placing " + player + " in column " + str(column))
        print("Make sure to pick a column between 1 and " + str(len(gameboard)) + " that isn't full\n")
        return False

    # Check to make sure the symbol is either an R or B
    if player != "R" and player != "B":
        print("Placing " + player + " in column " + str(column))
        print("Make sure to use either an 'R' for red, or an 'B' for blue, as your piece\n")
        return False

    # Places a piece at the bottom of the selected column
    for y in range(len(gameboard[0])-1, -1, -1):
        if gameboard[column-1][y] == ' ':
            gameboard[column-1][y] = player
            print("Placed an " + player + " in column " + str(column))
            print()
            return True
    return False

#check for winner
def available_moves(gameboard):
    # Returns the columns that are open
    moves = []
    for i in range(1, len(gameboard)+1):
        if is_move_valid(gameboard, i):
            moves.append(i)
    return moves

def has_won(gameboard, symbol):
    # check horizontal spaces
    for y in range(len(gameboard[0])):
        for x in range(len(gameboard) - 3):
            if gameboard[x][y] == symbol and gameboard[x+1][y] == symbol and gameboard[x+2][y] == symbol and gameboard[x+3][y] == symbol:
                return True

    # check vertical spaces
    for x in range(len(gameboard)):
        for y in range(len(gameboard[0]) - 3):
            if gameboard[x][y] == symbol and gameboard[x][y+1] == symbol and gameboard[x][y+2] == symbol and gameboard[x][y+3] == symbol:
                return True

    # check / diagonal spaces
    for x in range(len(gameboard) - 3):
        for y in range(3, len(gameboard[0])):
            if gameboard[x][y] == symbol and gameboard[x+1][y-1] == symbol and gameboard[x+2][y-2] == symbol and gameboard[x+3][y-3] == symbol:
                return True

    # check \ diagonal spaces
    for x in range(len(gameboard) - 3):
        for y in range(len(gameboard[0]) - 3):
            if gameboard[x][y] == symbol and gameboard[x+1][y+1] == symbol and gameboard[x+2][y+2] == symbol and gameboard[x+3][y+3] == symbol:
                return True

    return False

def game_is_over(gameboard):
  # Returns True if either player has won the game or if there are no open columns
  return has_won(gameboard, "R") or has_won(gameboard, "B") or len(available_moves(gameboard)) == 0

def play_game():
    # Creating an empty gameboard
    my_board = []
    for col in range(7):
        my_board.append([' '] * 6)

    # Starting the game with R going first    
    turn = "R"
    winner = False
    while(not game_is_over(my_board)):

        print_board(my_board)
        move = 0
        available = available_moves(my_board)
        # Continuing to ask for a valid move until the user gives one
        while (move not in available):
            move = int(input("It is " + turn + "'s turn. Please select a column. Your optionns are " + str(available)))
        select_space(my_board, move, turn)
        # Checking to see if this move wins the game for the player. If so, exiting the loop
        if has_won(my_board, turn):
            print(turn + " has won!")
            print_board(my_board)
            winner = True
            break

        # Switching the players turn
        if turn == 'R':
            turn = "B"
        else:
            turn = 'R'
    # If we exit the loop and haven't determined a winner, that means it was a tie
    if not winner:
        print("It was a tie!")
        print_board(my_board)

play_game()

print("Enter in the column number 1 through 7 as the first argument and R for red or B for blue as the second argument to place your piece in the board.\n")
#game moves
select_space(my_board, 0, 'R')
select_space(my_board, 5, 'B')
select_space(my_board, 5, 'W')
select_space(my_board, 1, 'R')
select_space(my_board, 5, 'B')
select_space(my_board, 2, 'R')
select_space(my_board, 5, 'B')
select_space(my_board, 5, 'R')
select_space(my_board, 6, 'B')
select_space(my_board, 2, 'R')
select_space(my_board, 6, 'B')
select_space(my_board, 2, 'R')
select_space(my_board, 6, 'B')
select_space(my_board, 6, 'R')
select_space(my_board, 3, 'B')
select_space(my_board, 4, 'R')
select_space(my_board, 4, 'B')
select_space(my_board, 3, 'R')
select_space(my_board, 3, 'B')
select_space(my_board, 4, 'R')
select_space(my_board, 4, 'B')
select_space(my_board, 6, 'R')
print_board(my_board)
