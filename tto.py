import os

# class contains all the positions for inputs
class Board():
    def __init__(self):
        # 1 dummy position for user ease to iput positions between 1 and 9
        self.cells = [" " for i in range(10)]

    # display board
    def print_board(self):
        print("\n")

        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    # updating board with 'X' and 'O' after each player moves
    def update_board(self, cellno, player):
        if self.cells[cellno] == " ":

            self.cells[cellno] = player
        else:
            print("Spot is taken\n")

    # rematch if tied or won game
    def regame(self):
        print("Game over! Do you want to play again?")
        Ans = str(input("Answer Y for yes play again! or N for No don't want to play again\n")).upper()
        if (Ans == "N"):
            print("Bye")
            exit()
        if (Ans == "Y"):
            self.cells = [" " for i in range(10)]
            board.print_board()

    # 8 ways to win the game 3 across 3 vertical 2 diagonal. Checks all 8 options
    def did_win(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True

        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True

        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

    def did_game_tie(self):
        sum_cell = 0
        for i in range(1, 10):
            if self.cells[i] != " ":
                sum_cell += 1
        if sum_cell == 9:
            print("Game tied")
            return True


board = Board()


# clears the screen and prints an updated board after each player inputs cell moves
def screen_update():
    os.system("clear")
    print("Tic Tac Toe: Game in progress")
    board.print_board()


# Game continues until win or tie and asks players if they want to proceed
# At present its asking for regame whiever player won or tied, have to make this universal
if __name__ == "__main__":
    board = Board()
    while True:
        screen_update()

        X_pos = int(input("Turn of player X: input cell number between 0-9 to place X:- "))
        print("\n")
        board.update_board(X_pos, "X")
        screen_update()

        if board.did_win("X"):
            print("Player X won")
            board.regame()

        if board.did_game_tie():
            board.regame()

        O_pos = int(input("Turn of player O: input cell number between 0-9 to place O:- "))
        print("\n")
        board.update_board(O_pos, "O")
        screen_update()
        if board.did_win("O"):
            print("Player O won")
            board.regame()

        if board.did_game_tie():
            board.regame()