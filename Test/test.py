import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "♣"
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game_over = False
        self.draw_board()
        
    def draw_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Helvetica", 20), width=3, height=1, command=lambda row=i, col=j: self.play_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def play_move(self, row, col):
        if self.game_over or self.board[row][col] != ' ':
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        if self.check_win(row, col):
            self.game_over = True
            self.show_message(f"Le joueur {self.current_player} a gagné!")
        elif self.check_draw():
            self.game_over = True
            self.show_message("Match nul!")
        else:
            self.current_player = '♠️'
            self.play_random_move()
            if self.check_win(row, col):
                self.game_over = True
                self.show_message(f"Le joueur {self.current_player} a gagné!")
            elif self.check_draw():
                self.game_over = True
                self.show_message("Match nul!")
            else:
                self.current_player = '♣'
    
    def play_random_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        row, col = random.choice(empty_cells)
        self.board[row][col] = '♠️'
        self.buttons[row][col].config(text='♠️')
        
    def check_win(self, row, col):
        return self.check_row(row) or self.check_column(col) or self.check_diagonal() or self.check_antidiagonal()
    
    def check_row(self, row):
        return self.board[row][0] == self.board[row][1] == self.board[row][2] != ' '
    
    def check_column(self, col):
        return self.board[0][col] == self.board[1][col] == self.board[2][col] != ' '
    
    def check_diagonal(self):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '
    
    def check_antidiagonal(self):
        return self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '
    
    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True
    
    def show_message(self, message):
        popup = tk.Toplevel()
        label = tk.Label(popup, text=message, font=("Helvetica", 20))
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(popup, text="Rejouer", command=self.reset)
        button.pack()
        
    def reset(self):
        self.current_player = '♣'
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game_over = False
    
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        
        self.master.destroy()
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()