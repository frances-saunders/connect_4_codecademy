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

my_board = make_board()
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
