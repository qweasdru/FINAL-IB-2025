import random
import sys

class Game:
    def __init__(self, conn):
        self.conn = conn
        self.board = [' '] * 9
        self.score = 0

    def send(self, msg):
        self.conn.sendall(msg.encode())

    def recv(self, size=1024):
        return self.conn.recv(size).decode().strip()

    def print_board(self):
        b = self.board
        self.send(
            f"\n"
            f" {b[0]} | {b[1]} | {b[2]}\n"
            f"---+---+---\n"
            f" {b[3]} | {b[4]} | {b[5]}\n"
            f"---+---+---\n"
            f" {b[6]} | {b[7]} | {b[8]}\n"
        )

    def check_win(self, sym):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        return any(all(self.board[i] == sym for i in line) for line in wins)

    def check_flag(self):
        if self.score == 1337:
            with open("/home/flag.txt") as f:
                flag = f.read()
            self.send(f"Congrats! Your flag is: {flag}\n")
            raise SystemExit
        return False

    def user_move(self):
        self.send("Enter your move (0-8): ")
        move = self.recv()

        try:
            scope = {"self": self}
            exec(move, scope)
            self.send("[+] Executed.\n")
        except Exception as e:
            self.send(f"[!] Exec error: {e}\n")

        self.check_flag()

        try:
            idx = int(move)
            if self.board[idx] == ' ':
                self.board[idx] = 'X'
            else:
                self.send("Invalid move.\n")
        except:
            self.send("Invalid input.\n")

    def ai_move(self):
        # AI tries to win, block, else pick center/corner/random
        def find_winning_move(sym):
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = sym
                    if self.check_win(sym):
                        self.board[i] = ' '
                        return i
                    self.board[i] = ' '
            return None

        move = find_winning_move('O')  # Try to win
        if move is None:
            move = find_winning_move('X')  # Try to block
        if move is None and self.board[4] == ' ':
            move = 4  # Take center
        if move is None:
            for i in [0, 2, 6, 8]:
                if self.board[i] == ' ':
                    move = i
                    break
        if move is None:
            empty = [i for i in range(9) if self.board[i] == ' ']
            if empty:
                move = random.choice(empty)

        if move is not None:
            self.board[move] = 'O'

    def play(self):
        self.send("Welcome to Tic Tac Toe! Beat the AI!\n")
        while True:
            self.print_board()
            self.user_move()
            self.check_flag()

            if self.check_win('X'):
                self.score += 100
                self.send(f"You win! Score: {self.score}\n")
                self.board = [' '] * 9
            elif ' ' not in self.board:
                self.send("It's a draw.\n")
                self.board = [' '] * 9
            else:
                self.ai_move()
                if self.check_win('O'):
                    self.send("AI wins!\n")
                    self.board = [' '] * 9

            self.check_flag()
