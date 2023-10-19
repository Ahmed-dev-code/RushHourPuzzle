# RushHourPuzzle

Solving the Rush Hour puzzle using research algorithms (A*) and implementing an interface using Pygame.

### Project Structure

The project structure includes the following components:

- `puzzles/`: Contains puzzle CSV files with different configurations.
- `Classes/`: Contains the core classes of the project.
  - `RushHourPuzzle.py`: Defines the RushHourPuzzle class and core logic.
  - `Node.py`: Defines the Node class for A* search.
- `puzzleInterface.py`: The script for running the game interface using Pygame.
- `puzzleSolver.py`: The A* algorithm implementation for solving the Rush Hour puzzle.
- `ReadMe.md`: This file.

## Installation

1. Clone or download this repository to your local machine.
2. Move to your folder
3. Create a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

  
## How to Use It

### Puzzle File Format

The puzzle is defined in a CSV format using the following structure:

- The first row contains two integers, separated by a comma, representing the board's width and height, respectively.
- Subsequent rows represent vehicles on the board. Each row contains:
  - The vehicle's identifier (Id), usually a single character.
  - The vehicle's x-coordinate on the board.
  - The vehicle's y-coordinate on the board.
  - The vehicle's orientation, either 'H' for horizontal or 'V' for vertical.
  - The length of the vehicle (number of cells it occupies).

Walls are defined using rows that start with `#`. These rows have the following format:
- `#,x,y` where `x` and `y` are the coordinates of a wall.

  Here's an example of a puzzle file including walls:
```
6,6         # the board width and height
#,0,0       # example of a wall in the cell (0,0)
#,4,1
#,2,3
#,5,3
#,3,4
X,0,2,H,2   # the car goal (always represented by 'X') in the cell (1,0) has 2 cells length placed Horizantally.
A,1,0,H,2
B,3,0,H,3
C,1,1,H,2
E,4,1,H,2
H,0,3,H,2
I,3,3,H,2
J,0,4,V,2
K,2,4,V,2
L,4,4,H,2

```

### Game Interface

1. **Select a Puzzle**:
   - Use a puzzle file from the "puzzles" folder, or add your own puzzle using a CSV file with the same structure.
   - Modify the variable `puzzle_file` in the "puzzleInterface.py" file and set it to your desired puzzle CSV file.


2. **Run the Game**:
   - Execute the "puzzleInterface.py" script to start the game interface.

3. **Modify and Experiment**:
   - Feel free to modify the game, add new puzzles, or experiment with different settings to challenge yourself.


## Game Rules

The Rush Hour puzzle is a classic sliding block puzzle. The objective is to move the target vehicle (usually the red car) to the exit by shifting other vehicles horizontally or vertically.
