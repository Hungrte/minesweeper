from typing import Tuple
import customtkinter as ctk
from Minesweeper import Mine
class MinesweeperApp(ctk.CTk):
    def __init__(self, board_size, mine_count, **kwargs):
        super().__init__(**kwargs)
        
        self.title('Minesweeper')
        
        self.size = board_size
        self.mines = mine_count
        self.cells = {}
        
        self.game = Mine()
        self.game.setup(self.size, self.mines)
        
        self.board_frame = ctk.CTkFrame(master=self)
        self.board_frame.grid(row=1, column=0, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        
        self.create_ui()
    
    def create_ui(self):
        title = ctk.CTkLabel(
            self,
            text='Minesweeper',
            font=('Arial', 24, 'bold')
        )
        title.grid(row=0, column=0)
            
        restart = ctk.CTkButton(
            self,
            text='Restart',
            command=self.restart_game
        )
        restart.grid(row=2, column=0, pady=10)
            
        for row in range(self.size):
            for column in range(self.size):
                cell = ctk.CTkButton(
                    self.board_frame,
                    text='#',
                    height=55,
                    width=55,
                    command=lambda r=row, c=column: self.on_click(r, c)
                )
                cell.grid(row=row, column=column, padx=2, pady=2)
                self.cells[(row, column)] = cell
    
    def update_cells(self, coords=None):
        if coords is None:
            coords = self.cells.keys()

        for r, c in coords:
            value = self.game.hgrid[r][c]
            text = '' if value == 0 else value
            self.cells[(r, c)].configure(text=text)

    def set_board_enabled(self, enabled):
        state = 'normal' if enabled else 'disabled'

        for cell in self.cells.values():
            cell.configure(state=state)
    
    def on_click(self, r, c):
        revealed = self.game.Reveal(r, c)

        if revealed:
            self.update_cells(revealed)

        if self.game.status != 'running':
            self.set_board_enabled(False)

    def restart_game(self):
        self.game = Mine()
        self.game.setup(self.size, self.mines)

        self.update_cells()
        self.set_board_enabled(True)

if __name__ == '__main__':
    app = MinesweeperApp(10, 3)
    app.mainloop()
