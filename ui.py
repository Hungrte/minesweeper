import customtkinter as ctk
from Minesweeper import Mine

app = ctk.CTk()
app.title('Minesweeper')
board_frame = ctk.CTkFrame(
    master=app
)
board_frame.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

size = 10
mines = 10
cells = {}

game = Mine()
game.setup(size, mines)

def on_click(r, c):
    game.Reveal(r, c)
    refresh_board()

def ui():
    title = ctk.CTkLabel(
        app,
        text='Minesweeper',
        font=('Arial', 24, 'bold')
    )
    title.grid(row=0, column=0)
    
    for row in range(size):
        for column in range(size):
            cell = ctk.CTkButton(
                board_frame,
                text=f'#',
                height=55,
                width=55,
                command=lambda r=row, c=column: on_click(r, c)
            )
            cell.grid(row=row, column=column, padx=2, pady=2)
            cells[(row, column)] = cell

def refresh_board():
    for (r, c), button in cells.items():
        # Turns 0 into an empty cell
        if game.hgrid[r][c] == 0:
            button.configure(text='')
            continue
        button.configure(text=game.hgrid[r][c])

ui()

app.mainloop()



