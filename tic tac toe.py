# Global Variables 
symbol = 'X'
Player1_list = []
Player1_sum = []
Player2_list = []
Player2_sum = []
GameBoard = []


def CreateBoard():
    # creates the board, and places number for future usage
    global GameBoard
    list_1 = []
    list_1.append([8, 1, 6])
    list_1.append([3, 5, 7])
    list_1.append([4, 9, 2])
    GameBoard = list_1
    DisplayBoard()


def Player_action():
    # For each player, it takes the number from the index and assigns the letter, and then switches the sign for the next player
    global symbol
    global Player1_list
    global Player2_list
    global GameBoard
    global Player2_sum
    global Player1_sum
    num_board = int(input("Select number on the board\n"))
    for i in range(len(GameBoard)):
        for j in range(len(GameBoard[i])):
            if (GameBoard[i][j] == num_board) and (symbol == 'X'):
                # Player 1
                GameBoard[i][j] = symbol
                Player1_list.append(num_board)
                DisplayBoard()
                AddingNums(Player1_list, symbol)
                WinningCondition(Player1_sum)
            elif (GameBoard[i][j] == num_board) and (symbol == 'O'):
                # Player 2
                GameBoard[i][j] = symbol
                Player2_list.append(num_board)
                DisplayBoard()
                AddingNums(Player2_list, symbol)
                WinningCondition(Player2_sum)


def AddingNums(list_nums, symbol):
    # Creates all possible sums from a list of numbers and appends it to the new list
    global Player1_sum 
    global Player2_sum
    n = len(list_nums)
    AddedNumber = 0
    while n != 1:
        for i in range(len(list_nums)):
            if i == 0 and symbol == 'X':
                Player1_sum.append(list_nums[i])
            elif i == 0 and symbol == 'O':
                Player2_sum.append(list_nums[i])
            elif symbol == 'X':
                Player1_sum.append(list_nums[0] + list_nums[i])
            elif symbol == 'O':
                Player2_sum.append(list_nums[0] + list_nums[i])
        AddedNumber = list_nums[0]
        list_nums = list_nums[1:n]
        list_nums[0] += AddedNumber
        n = len(list_nums)
    if n == 1:
        if symbol == 'X':
            Player1_sum.append(list_nums[0])
        elif symbol == 'O':
            Player2_sum.append(list_nums[0])


def WinningCondition(Player_sum):
    # Looks into all sums and check if any of them is equal to 15. 
    global symbol
    if 15 in Player_sum and symbol == 'X':
        print('Player 1 wins')
    elif 15 in Player_sum and symbol == 'O':
        print('Player 2 wins')
    elif symbol == 'X':
        symbol = 'O'
        Player_action()
    elif symbol == 'O':
        symbol = 'X'
        Player_action()
            

def DisplayBoard():
    # For every line in the list, it will display them one by one to create a tic tac toe board
    for i in range(len(GameBoard)):
        for j in range(len(GameBoard[i])):
            print('[', GameBoard[i][j], ']', end='')
        print()



if __name__ == "__main__":
    CreateBoard()
    Player_action()
    
    



