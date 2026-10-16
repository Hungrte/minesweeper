# Minesweeper

A Minesweeper game built with Python, featuring a reusable game-logic class and a graphical interface made with CustomTkinter.

The project started as a terminal-based game and is now being developed into a GUI version with clickable cells, a restart button, and a class-based interface.

**Status:** Playable GUI in development on the `ui` branch.

## Features

### Game Logic
- Custom board size and mine count
- Random mine placement
- Neighbor counting for all eight surrounding cells
- Automatic revealing of connected empty cells using iterative flood fill
- Separate answer and player grids
- Win and loss detection
- All mines revealed when the game ends
- Moves ignored after the game is over

### Graphical Interface
- Clickable cells
- Restart button
- Class-based GUI structure using `MinesweeperApp`
- Game logic kept separate from the interface through the `Mine` class
- Targeted cell updates to avoid refreshing the entire board after every move

## Requirements

- Python 3.10 or newer
- CustomTkinter

Install the GUI dependency with:

```bash
python -m pip install customtkinter
```

## Run

From the project directory, run:

```bash
python ui.py
```

Make sure `ui.py` and `Minesweeper.py` are in the same directory.

## How to Play

1. Launch the game.
2. Click a hidden cell to reveal it.
3. Numbers indicate how many of the eight neighboring cells contain mines.
4. Revealing a mine ends the game.
5. Reveal every safe cell to win.
6. Use the **Restart** button to start a new game.

## How It Works

The project separates game logic from the graphical interface.

- **`Minesweeper.py`** contains the `Mine` class, which manages the board, mine placement, neighbor counts, cell revealing, and win/loss conditions.
- **`ui.py`** contains the `MinesweeperApp` class, which manages the window, widgets, click events, board updates, and restarting the game.

The game maintains two grids:

- **Answer grid:** Stores mines as `9` and the number of neighboring mines for every safe cell.
- **Player grid:** Starts with hidden cells represented by `#` and updates as cells are revealed.

The interface uses the game logic's state to determine which cells to display. Keeping these responsibilities separate makes it easier to improve the GUI without rewriting the underlying game.

## Roadmap

- [x] Core Minesweeper game logic
- [x] Basic CustomTkinter GUI
- [x] Class-based GUI structure
- [x] Clickable cells and restart button
- [ ] Refactor the board rendering to use Tkinter Canvas
- [ ] Add mine flags
- [ ] Add a timer
- [ ] Make the first click safe
- [ ] Add tests and further code cleanup

## Author

Made by [Hungrte](https://github.com/Hungrte).
