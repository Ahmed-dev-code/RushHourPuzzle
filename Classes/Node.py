class Node:
    def __init__(self, state, parent, action, g=0, f=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g # The cost of the path from the start node to n;
        self.f = f #  The fitness function used in the A* algorithm;
    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state
    
    def getPath(self):
        # Return the path from the root to this node
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]
    
    def getSolution(self):
        # Return the list of actions from the root to this node
        # return [node.action for node in self.getPath()[1:]]
        actions = []
        node = self
        while node != None:
            actions.append(node.action)
            node = node.parent
        return actions[::-1]
    
    def setF(self, heuristic):
        #This function calculates the fitness function f based on a heuristic function h
        self.f = self.g + heuristic(self.state)
