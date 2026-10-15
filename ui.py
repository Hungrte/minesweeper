import customtkinter as ctk
from Minesweeper import Mine

app = ctk.CTk()
app.title('Minesweeper')

size = 10
mines = 20
cells = {}

game = Mine()
game.setup(size, mines)

def on_click(r, c):
    game.Reveal(r, c)
    refresh_board()

def ui():
    for row in range(size):
        for column in range(size):
            cell = ctk.CTkButton(
                app,
                text=f'#',
                height=55,
                width=55,
                command=lambda r=row, c=column: on_click(r, c)
            )
            cell.grid(row=row, column=column, padx=2, pady=2)
            cells[(row, column)] = cell

def refresh_board():
    for (r, c), button in cells.items():
        button.configure(text=game.hgrid[r][c])

ui()

app.mainloop()



