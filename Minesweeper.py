import random 

# the coords work like (row index, cell index) its so dumb omg kill me rn

class Mine:
    def __init__(self):
        self.grid = []
        self.size = 0
        self.hgrid = []
        self.opencells = 0
        self.totalcells = 0
        self.mines = 0
        self.keep_going = True
        self.lose = False

    def calculatetotal(self):
        self.totalcells = (self.size ** 2) - self.mines # because like square we subtract mines so it doesn count mines

    def Createspace(self, size: int):
        # this creates the thing the area
        self.size = size
        if self.grid:
            raise ValueError('Space is already made!')
        
        for _ in range(0, size):
            row = []
            for _ in range(0, size):
                row.append(0)
            self.grid.append(row)
        
        for _ in range(0, size):
            row = []
            for _ in range(0, size):
                row.append('#')
            self.hgrid.append(row)

    def Displayspace(self):
        # DISPLAYS THE GRID ITSELF 
        # if not self.grid:
        #     raise ValueError('Space is empty!')
        # for row in self.grid:
        #     new_row = ' '.join([str(x) for x in row])
        
        if not self.hgrid:
            raise ValueError('Space is empty!')
        
        print('---------------------')

        for row in self.hgrid:
            new_row = ' '.join([str(x) for x in row ])
            print(new_row)
    
    def Placemines(self, num: int):
        self.mines = num
        coords = self.Getcoordinates(self.grid)
        if not coords:
            raise ValueError('Coordinates empty!')
        random_sample = random.sample(coords, num)

        for row_index, cell_index in random_sample:
            self.grid[row_index][cell_index] = 9

        print(random_sample, 'Picked')

    def Getcoordinates(self, grid):
        final_coords = []
        for row_index, row in enumerate(grid):
            for cell_index, cell in enumerate(row):
                coords = (row_index, cell_index)
                final_coords.append(coords)
        
        return final_coords
    
    def Checkmines(self):
        coords = self.Getcoordinates(self.grid)
        for coord in coords:
            mines = 0
            row, cell = coord
            neighbours = self.Getneighbours(row, cell, self.grid)
            # print(neighbours)
            if not self.grid[row][cell] == 9:
                for n_row, n_cell in neighbours:
                    cell_info = self.grid[n_row][n_cell]
                    if cell_info == 9:
                        mines += 1
                self.grid[row][cell] = mines
    
    def Getneighbours(self, r, c, grid):
        rows, cols = len(grid), len(grid[0])
        # WTH IS HAPPENING??? IDK HOW THIS WORKS LOL
        return [
            (nr, nc) for nr in range(max(0, r - 1), min(rows, r + 2))
            for nc in range(max(0, c - 1), min(cols, c + 2))
            if (nr, nc) != (r, c)
        ]
    
    def Reveal(self, r, c):
        # yoo this reveals the cells omgg
        if not self.keep_going:
            return
        
        r -= 1
        c -= 1
        
        neighbours = self.Getneighbours(r, c, self.hgrid)
        pile = [(r, c)]
        
        if not pile:
            return
        
        i = 0

        while i < len(pile):
            row, cell = pile[i]
            i += 1

            if self.hgrid[row][cell] != '#':
                continue

            self.hgrid[row][cell] = self.grid[row][cell]

            if self.hgrid[row][cell] == 0:
                neighbours = self.Getneighbours(row, cell, self.hgrid)

                for nlist in neighbours:
                    pile.append(nlist)

        self.Condition(r, c)

        self.count()
    
    def Condition(self, r, c):
        # checks if theres a mine
        if not self.hgrid[r][c] == 9:
            return
        self.lose = True
        self.Showmines()
    
    def Showmines(self):
        self.keep_going = False
        coords = self.Getcoordinates(self.hgrid)
        for row, cell in coords:
            if self.grid[row][cell] == 9:
                self.hgrid[row][cell] = self.grid[row][cell]
    
    def count(self):
        self.opencells = 0

        hcoords = self.Getcoordinates(self.hgrid)
        for row, cell in hcoords:
            if not self.hgrid[row][cell] == '#':
                self.opencells += 1
    
    def setup(self, size, mines):
        self.Createspace(int(size))
        self.Placemines(int(mines))
        self.Checkmines()
        self.count()
        self.calculatetotal()
        self.Displayspace()
    
def get_integer(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f'Enter a number from {minimum} to {maximum}.')

        except ValueError:
            print('Please enter a valid whole number!')

if __name__ == '__main__':
    size = get_integer('What size: ', 2, 1000)
    mines = get_integer('Amount of mines: ', 1, size ** 2 - 1)
    game = Mine()
    game.setup(size, mines)

    while game.opencells < game.totalcells and game.keep_going:
        print('Print a coordinate! (x, y)')
        x = get_integer('X = ', 1, game.size)
        y = get_integer('Y = ', 1, game.size)
        game.Reveal(int(y), int(x))
        game.Displayspace()
        print('Total cells', game.totalcells)
        print('Open cells', game.opencells)
    
    if game.lose:
        print('Game Over')
    else:
        print('You won!')
    
    game.Showmines()
    game.Displayspace()
