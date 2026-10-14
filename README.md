# Minesweeper

A Minesweeper game written in Python that runs in the terminal. Choose a board size and a number of mines, then open every safe cell without hitting a mine.

> **Status:** playable in the terminal. A graphical interface is in development on the `ui` branch.

## Features

- Custom board size and mine count
- Random mine placement, with every other cell showing how many of its 8 neighbours are mines
- Opening an empty cell automatically opens the connected empty region and its numbered border (flood fill)
- Flood fill uses a loop instead of recursion, so large boards don't hit Python's recursion limit
- A single game status (`running`, `won` or `lost`); moves are ignored once the game is over
- All mines are revealed when the game ends
- Input validation: invalid or out-of-range input asks again instead of crashing

## Requirements

- Python 3.6 or newer
- No third-party packages, only the standard library

## Run

```bash
python minesweeper.py
```

## How to play

1. Enter a board size (at least 2) and a number of mines (at least 1, leaving at least one safe cell).
2. Each turn, enter an **X** (column) and a **Y** (row) coordinate. Both count from 0, so `0, 0` is the top-left cell.
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

Safe cells are counted as they open and compared with the total number of safe cells to decide whether the player has won. The game logic lives in the `Mine` class, which keeps its state separate from the terminal loop so a graphical interface can reuse it.

## Roadmap

- [ ] Flags
- [ ] Graphical interface (pygame), in progress on the `ui` branch
- [ ] First click is always safe
- [ ] Restart and timer
- [ ] Tests and code cleanup

## Author

Made by [Hungrte](https://github.com/Hungrte).
