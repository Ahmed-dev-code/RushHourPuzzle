class RushHourPuzzle:
    def __init__(self):
        self.board_height = 0
        self.board_width = 0
        self.vehicles = []
        self.walls = []
        self.board = []

    def setVehicles(self, csv_file):
        # Read the CSV file to set board_height, board_width, vehicles, and walls
        with open(csv_file, 'r') as file:
            lines = file.readlines()
            self.board_height, self.board_width = map(int, lines[0].strip().split(','))
            for line in lines[1:]:
                parts = line.strip().split(',')
                if parts[0] == '#':
                    self.walls.append((int(parts[1]), int(parts[2])))
                else:
                    self.vehicles.append((parts[0], int(parts[1]), int(parts[2]), parts[3], int(parts[4])))

    def setBoard(self):
        # Initialize the board with empty squares
        self.board = [[' ' for _ in range(self.board_width)] for _ in range(self.board_height)]

        # Place walls on the board
        for wall in self.walls:
            x, y = wall
            self.board[y][x] = '#'

        # Place vehicles on the board
        for vehicle in self.vehicles:
            id, x, y, orientation, length = vehicle
            if orientation == 'H':
                for i in range(length):
                    self.board[y][x + i] = id
            else:
                for i in range(length):
                    self.board[y + i][x] = id

    def isGoal(self):
        # Check if the red car is in the goal position
        return self.board[self.board_height // 2 - 1][self.board_width - 2] == 'X'

    # def successorFunction(self):
    #     successors = []

    #     for vehicle in self.vehicles:
    #         id, x, y, orientation, length = vehicle

    #         # Generate possible moves for the vehicle
    #         if orientation == 'H':
    #             for dx in [-1, 1]:
    #                 if 0 <= x + dx < self.board_width and self.board[y][x + dx] == ' ':
    #                     new_vehicles = [v for v in self.vehicles if v != vehicle]
    #                     new_vehicles.append((id, x + dx, y, orientation, length))
    #                     successors.append((f"Move {id} {'Left' if dx == -1 else 'Right'}", new_vehicles))
    #         else:
    #             for dy in [-1, 1]:
    #                 if 0 <= y + dy < self.board_height and self.board[y + dy][x] == ' ':
    #                     new_vehicles = [v for v in self.vehicles if v != vehicle]
    #                     new_vehicles.append((id, x, y + dy, orientation, length))
    #                     successors.append((f"Move {id} {'Up' if dy == -1 else 'Down'}", new_vehicles))

    #     return successors
    
    # def successorFunction(self): so it returns an instance of the RushHourPuzzle class
    
    def successorFunction(self):
        successors = []

        for vehicle in self.vehicles:
            id, x, y, orientation, length = vehicle
            
            successor_state = RushHourPuzzle()
            successor_state.board_height = self.board_height
            successor_state.board_width = self.board_width
            successor_state.walls = self.walls
            # Generate possible moves for the vehicle
            if orientation == 'H':
                for dx in [-1, 1]:
                    if dx == -1 and 0 <= x + dx <= self.board_width and self.board[y][x + dx] == ' ':
                        new_vehicles = [v for v in self.vehicles if v != vehicle]
                        new_vehicles.append((id, x + dx, y, orientation, length))
                        successor_state.vehicles = new_vehicles
                        successor_state.setBoard()
                        successors.append((f"Move {id} {'Left' if dx == -1 else 'Right'}", successor_state))
                    elif dx == 1 and 0 <= (x + length)  < self.board_width and self.board[y][x + dx + length - 1] == ' ':
                        new_vehicles = [v for v in self.vehicles if v != vehicle]
                        new_vehicles.append((id, x + dx, y, orientation, length))
                        successor_state.vehicles = new_vehicles
                        successor_state.setBoard()
                        successors.append((f"Move {id} {'Left' if dx == -1 else 'Right'}", successor_state))
            else:
                for dy in [-1, 1]:
                    if dy == -1 and 0 <= y + dy <= self.board_height and self.board[y + dy][x] == ' ':
                        new_vehicles = [v for v in self.vehicles if v != vehicle]
                        new_vehicles.append((id, x, y + dy, orientation, length))
                        successors.append((f"Move {id} {'Up' if dy == -1 else 'Down'}", successor_state))
                    elif dy == 1 and 0 <= y +length  < self.board_height and self.board[y + dy + length - 1][x] == ' ':
                        new_vehicles = [v for v in self.vehicles if v != vehicle]
                        new_vehicles.append((id, x, y + dy, orientation, length))
                        successors.append((f"Move {id} {'Up' if dy == -1 else 'Down'}", successor_state))

        return successors
    
