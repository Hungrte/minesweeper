# Minesweeper

A terminal-based Minesweeper game written in Python. Choose your board size and number of mines, then clear every safe cell without hitting a mine.

> **Status:** playable prototype. A graphical interface is being planned.

## Features

- Custom board size and mine count
- Random mine placement, with every other cell showing how many of its 8 neighbours are mines
- Opening an empty cell automatically opens the connected empty region and its numbered border (flood fill)
- Flood fill uses a loop instead of recursion, so large boards don't hit Python's recursion limit
- Win and lose detection; all mines are revealed when the game ends
- Input validation: invalid or out-of-range input asks again instead of crashing

## Requirements

- Python 3.6 or newer
- No third-party packages, only the standard library

## Run

```bash
python minesweeper.py
```

## How to play

1. Enter a board size and the number of mines (at least 1, and at least one cell must stay safe).
2. Each turn, enter an **X** (column) and a **Y** (row) coordinate, counting from 1.
3. Read the board:
   - `#` is a hidden cell
   - a number is how many of the 8 surrounding cells are mines
   - `9` is a mine, shown when the game ends
4. Open every safe cell to win. Open a mine and you lose.

Example board mid-game:

```
---------------------
# # # # #
# 1 1 1 #
# 1 0 1 #
# 1 1 1 #
# # # # #
```

## How it works

The game keeps two grids of the same size:

- the **answer grid** holds `9` for mines and a neighbour count for every other cell, calculated once after the mines are placed
- the **player grid** starts as all `#`, and cells are copied across from the answer grid as they are revealed

Keeping them separate keeps the game logic apart from how the board is displayed, which will make adding a graphical interface easier.

## Roadmap

- [ ] Flags
- [ ] Graphical interface (pygame)
- [ ] First click is always safe
- [ ] Restart and timer
- [ ] Code cleanup and tests

## Author

Made by [Hungrte](https://github.com/Hungrte).
