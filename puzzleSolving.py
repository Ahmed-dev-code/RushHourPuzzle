from Classes.RushHourPuzzle import RushHourPuzzle
from Classes.Node import Node

import heapq

def astar(puzzle):
    
    # Define the heuristic function h1 that returns the distance from the target vehicle (the red car) to the goal position
    # the goal position is in (board_width - 2, board_height/2-1)
    board_width = puzzle.board_width
    board_height = puzzle.board_height
    
    def h1(vehicles):
        # Define the goal position
        goal_position = (board_width - 2, board_height // 2 - 1)

        # Find the position of the red car in the list of vehicles
        red_car = [v for v in vehicles if v[0] == 'X'][0]

        # Calculate the Manhattan distance from the red car to the goal position
        red_car_position = (red_car[1], red_car[2])
        distance = abs(red_car_position[0] - goal_position[0]) + abs(red_car_position[1] - goal_position[1])

        return distance
    
    start_node = Node(puzzle, None, None, 0, h1(puzzle.vehicles))
    open_list = [(start_node.f, start_node)]  # priority queue for the nodes to be expanded
    closed_set = set() # set of nodes that have already been expanded (we don't want to expand them again)
    
    # number of steps
    steps = 0
    while open_list:
        _, current_node = heapq.heappop(open_list)  # pop the node with the lowest f value
        if current_node.state.isGoal():
            path = current_node.getPath()
            solution = current_node.getSolution()
            print("Goal state reached!")
            return path, solution,steps
        
        closed_set.add(current_node.state)
        steps += 1

        successors = current_node.state.successorFunction()
        
        # print the successors
        print([action for action in successors])
        
        for action, successor_state in successors:
            g = current_node.g + 1  # Assuming a step cost of 1
            f = g + h1(successor_state.vehicles)
            
            print("Expanding node with action:", action)
            print("Current state:")
            for row in current_node.state.board:
                print(row)
            print("Action:", action)
            print("Successor state:")
            for row in successor_state.board:
                print(row)
            print("g:", g)
            print("f:", f)

            # Check if the successor is not in the open list or has a lower f value
            existing_node = None
            for _, node in open_list:
                if node.state == successor_state:
                    existing_node = node
                    break
            # if existing_node is None or g < existing_node.g:
            if existing_node is None or f < existing_node.f:
                new_node = Node(state=successor_state, parent=current_node, action=action, g=g, f=f)
                if existing_node:
                    open_list.remove((existing_node.f, existing_node))
                heapq.heappush(open_list, (f, new_node))
            
            print("Open list size:", len(open_list))
            print("Closed set size:", len(closed_set))
            print("--------")

    # No solution found
    print("No solution found.")
    return None


                    



    
# test it to see if it works

puzzle = RushHourPuzzle() 
puzzle.setVehicles('puzzles/test.csv')
puzzle.setBoard()
# print(puzzle.board) in a readable format
print("Initial state: \n")
for row in puzzle.board:
    print(row)
print()

print(puzzle.isGoal())
# print(puzzle.successorFunction()) 


path, solution,steps = astar(puzzle)
# print(path)
for node in path:
    print(node.action)
    for row in node.state.board:
        print(row)
    print()
    
print("your puzzle: \n")
for row in puzzle.board:
    print(row)
print()
 
print(solution)
print("steps: " ,steps)
