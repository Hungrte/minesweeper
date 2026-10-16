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

app.grid_columnconfigure(0, weight=1)

size = 10
mines = 10
cells = {}

game = Mine()
game.setup(size, mines)

def on_click(r, c):
    game.Reveal(r, c)
    refresh_board()

def restart_game():
    global game
    game = Mine()
    game.setup(size, mines)
    refresh_board()

def ui():
    title = ctk.CTkLabel(
        app,
        text='Minesweeper',
        font=('Arial', 24, 'bold')
    )
    title.grid(row=0, column=0)
    
    restart = ctk.CTkButton(
        app,
        text='Restart',
        command=restart_game
    )
    restart.grid(row=2, column=0, pady=10)
    
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
    for (r, c), cell in cells.items():
        # Turns 0 into an empty cell
        if game.hgrid[r][c] == 0:
            cell.configure(text='')
            continue
        cell.configure(text=game.hgrid[r][c])
        if not game.status == 'running':
            cell.configure(state='disabled')
            continue
        cell.configure(state='normal')

ui()

app.mainloop()



