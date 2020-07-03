import os


class board:

    def __init__(self, N):
        self.N = N

        self.cells = [[" " for i in range(N)] for j in range(N)]

    def display(self):

        for i in reversed(range(self.N)):

            str_print = '|'
            for j in range(self.N):
                str_print += self.cells[i][j] + '  ' + '|'


            print(str_print)

            print(''.join(['-'] * 4 * self.N))


class game_connect4:
    def __init__(self, n):
        self.n = n
        self.B = board(self.n)
        self.B.display()
        self.current_row = None


    def reload_screen(self):
        os.system("clear")
        print("Game in progress")
        self.B.display()

    def match_win(self, player, col, row):
        check = player*4
        if check in ''.join(self.B.cells[row]):
            return True

        if check in "".join(list(zip(*self.B.cells))[col]):
            #print(check,"".join(list(zip(*self.B.cells))[col]))
            return True

        diags_1 = ''
        for i in range(3,0,-1):
            if self.B.N > row - i >= 0 and self.B.N > col - i >= 0:
                diags_1 += self.B.cells[row-i][col-i]
        for i in range(4):
            if self.B.N > row + i >= 0 and self.B.N > col + i >= 0:
                diags_1 += self.B.cells[row + i][col + i]

        if check in diags_1:

            return True

        diags_2 = ''
        for i in range(3, 0, -1):
            if self.B.N > row - i >= 0 and self.B.N > col + i >= 0:
                diags_2 += self.B.cells[row - i][col + i]
        for i in range(4):
            if self.B.N > row + i >= 0 and self.B.N > col - i >= 0:
                diags_2 += self.B.cells[row + i][col - i]

        if check in diags_2:
            return True



    def match_tie(self):
        sum_cell = 0
        for i in range(0, self.B.N):
            for j in range(0, self.B.N):
                if self.B.cells[i][j] != " ":
                    sum_cell += 1
        if sum_cell == self.B.N*self.B.N :
            print("Game tied")
            return True

    def rematch(self):
        print("Game over! Do you want to play again?")
        Ans = str(input("Answer Y for yes play again! or N for No don't want to play again\n")).upper()
        if (Ans == "N"):
            print("Bye")
            exit()
        if (Ans == "Y"):
            self.B. cells = [[" " for i in range(N)] for j in range(N)]
            self.B.display()

    def valid_move_update(self, pos, player):

        for i in range(self.B.N):

            if self.B.cells[i][pos] == " ":
                self.current_row = i #sets row value for current move

                self.B.cells[i][pos] = player


                break
            if i==self.B.N-1:
                if self.B.cells[i][pos] != " " :
                    print(player + " :Lost your move. illegal move! try another col")


    def play(self):
        self.reload_screen()

        X_pos = int(input("X player: input col number:"))
        print("\n")

        self.valid_move_update(X_pos, "X")
        self.reload_screen()
        if self.match_win("X", X_pos, self.current_row):
            print("Player X won")
            exit()

        O_pos = int(input("O player: input col number:"))
        print("\n")

        self.valid_move_update(O_pos, "O")
        self.reload_screen()
        if self.match_win("O", O_pos, self.current_row):
            print("Player O won")
            exit()



if __name__ == "__main__":
    size = int(input("Enter size S >= 4:  "))
    G = game_connect4(size)
    while True:
        G.play()