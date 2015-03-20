from maze_runner import MazeRunner

def maze_controller(mr):

    class MazeController(object):

        vectors = {
            'down': 0,
            'right': 1,
            'up': 2,
            'left': 3
        }

        opposite_vectors = {
            'down': 'up',
            'right': 'left',
            'up': 'down',
            'left': 'right'
        }

        cell_states = {
            'not_exists': 3,
            'last_visited': 2,
            'visited': 1,
            'new': 0
        }

        mr = None
        visited_cells = None
        last_visited_cell = (0, 0)
        current_cell = (0, 0)
        vector = 0

        def __init__(self, mr):
            self.mr = mr
            self.visited_cells = set()
            self.visited_cells.add(self.last_visited_cell)

        def turn_to(self, vector):

            # anticlockwise
            for i in range(self.vector):
                self.mr.turn_left()

            # clockwise
            for i in range(self.vectors[vector]):
                self.mr.turn_right()

            self.vector = self.vectors[vector]

        def get_cell_coordinates(self, vector):
            x = self.current_cell[0]
            y = self.current_cell[1]

            coordinates = {
                'down' : (x, y + 1),
                'up' : (x, y - 1),
                'right': (x + 1, y),
                'left': (x - 1, y)
            }

            return coordinates[vector]

        def get_cell_state(self, vector):

            # try go to cell
            self.turn_to(vector)
            result = self.mr.go()

            # if cell not exists
            if not result:
                return 'not_exists'

            # returning back
            opposite_vector = self.opposite_vectors[vector]
            self.turn_to(opposite_vector)
            self.mr.go()

            # other states
            coordinates = self.get_cell_coordinates(vector)

            if coordinates == self.last_visited_cell:
                return 'last_visited'
            elif coordinates in self.visited_cells:
                return 'visited'
            else:
                return 'new'

        def choose_vector(self):
            import random
            prior_list = [[],[],[],[]]
            vector = None

            for cur_vector in ['up', 'left', 'down', 'right']:
                state = self.get_cell_state(cur_vector)
                cur_priority = self.cell_states[state]
                prior_list[cur_priority].append(cur_vector)

            for i in range(3):
                sub_list = prior_list[i]

                if len(sub_list) > 0:
                    vector = random.choice(sub_list)
                    break

            return vector

        def go_to_next(self):
            vector = self.choose_vector()

            if vector is not None:
                self.turn_to(vector)
                self.mr.go()
                self.last_visited_cell = self.current_cell
                self.visited_cells.add(self.current_cell)
                self.current_cell = self.get_cell_coordinates(vector)
            else:
                return False

            if not self.mr.found():
                return True
            else:
                return False

        def get_current_cell(self):
            return self.current_cell

    mc = MazeController(mr)
    counter = 0

    while (mc.go_to_next()):
        counter += 1

    #print(counter)
    #print(mc.get_current_cell())

maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}

mr = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(mr)

