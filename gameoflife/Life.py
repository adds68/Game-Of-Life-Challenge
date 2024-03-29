import time, sys

class Life(object):
    """A class that implements a basic Game of Life algorithm"""
    def __init__(self, state=None, size=None):
        self.SIZE = size

        if len(state) == size:
            self.board = state
        else:
            raise Exception('The size of the intial state {0} does not match the specified size {1}'.format(len(state), size))

    def get_alive_neighbours(self, pos):
        """A method to calculate the number of living neighbours for a given cell"""
        r, c = pos
        neighbour_locations = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                               (r, c - 1),                 (r, c + 1),
                               (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
        count = 0
        for r, c in neighbour_locations:
            #ensure we don't hit pythons negative indexing
            if r >= 0 and c >= 0:
                try:
                    count += self.board[r][c]
                except IndexError:
                    pass
        return count
    
    def evolve_cell(self, cell, neighbours):
        """A method used to check if a cell should live or die"""
        if cell and neighbours < 2:
            return 0
        elif cell and neighbours == 2 or neighbours == 3:
            return 1
        elif cell and neighbours > 3:
            return 0
        elif not cell and neighbours == 3:
            return 1
        else:
            return cell

    def evolve(self, steps):
        """An iterator method, to return each state of a simulation"""
        for _ in range(steps):
            new_state = [[0 for r in range(self.SIZE)] for c in range(self.SIZE)] 

            for r in range(len(self.board)):
                for c in range(len(self.board[0])):
                    neighbours = self.get_alive_neighbours( (r, c) )
                    new_state[r][c] = self.evolve_cell(self.board[r][c], neighbours)

            self.board = new_state
            yield new_state
    
    def visual_evolve(self, steps):
        """A method used to visually display each simulation step"""
        states = self.evolve(steps)
        for num, state in enumerate(states):
            print('Evolution {0}'.format(num + 1)) 
            for i in range(len(state[0])):
                print(state[i])
            time.sleep(1)
