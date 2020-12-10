from constants import *

class Wire:
    def __init__(self, start):
        self.cells = []
        self.forks = []
        self.start = start
        self.currentDirection = self.find_open_direction()
        self.cells.append(start)
        self.isFork = False

    def find_next_cell(self):
        if self.currentDirection is None:  return None
        current_cell = self.cells[len(self.cells)-1]
        possible_directions = [self.currentDirection,
                               directions[(directions.index(self.currentDirection) - 1) % len(directions)],
                               directions[(directions.index(self.currentDirection) + 1) % len(directions)]]
        if random.uniform(0,1) == 1:
            possible_directions = [self.currentDirection,
                                   directions[(directions.index(self.currentDirection) + 1) % len(directions)],
                                directions[(directions.index(self.currentDirection) - 1) % len(directions)]]
        if random.uniform(0.0,1.0) > 0.5:
            random.shuffle(possible_directions)

        for d in possible_directions:
            next_cell = get_cell(current_cell.x+d[0],current_cell.y+d[1])
            adj_cells = (get_cell(current_cell.x+d[0],current_cell.y),get_cell(current_cell.x,current_cell.y+d[1]))
            if next_cell is not None and next_cell.open and (adj_cells[0].open or adj_cells[1].open):
                self.currentDirection = d
                return next_cell
        return None

    def find_open_direction(self):
        dir_list = list(directions)
        random.shuffle(dir_list)
        for d in dir_list:
            c = get_cell(d[0],d[1])
            if c is not None and c.open:
                return d
        return None

    def create_wire(self):
        length = lineLength
        if self.isFork:
            length = forkLength
        while len(self.cells) < length:
            next_cell = self.find_next_cell()
            if next_cell is None: break
            self.cells.append(next_cell)
            next_cell.open = False

            if len(self.cells) > 2 and random.uniform(0, 20) > 12:
                self.create_fork()
        return

    def create_fork(self):
        back = (self.currentDirection[0]*-1,self.currentDirection[1]*-1)
        possible_directions = [directions[(directions.index(self.currentDirection) - 1) % len(directions)],
                               directions[(directions.index(self.currentDirection) + 1) % len(directions)],
                               directions[(directions.index(back) + 1) % len(directions)],
                               directions[(directions.index(back) + 1) % len(directions)]
                               ]
        random.shuffle(possible_directions)
        fork = Wire(self.cells[len(self.cells)-1])
        fork.currentDirection = possible_directions[0]
        fork.isFork = True

        self.forks.append(fork)

        pass

    def draw_vias(self):
        start = self.cells[0]
        end = self.cells[len(self.cells)-1]

        rad = cellSize/3
        if self.isFork:
            rad = rad/1.5
        ctx.set_source_rgb(WIRE_COL[0], WIRE_COL[1], WIRE_COL[2])
        if not self.isFork:
            ctx.arc(start.x * cellSize + cellSize/2, start.y * cellSize + cellSize/2, rad, 0, 2*np.pi)
        ctx.arc(end.x * cellSize + cellSize/2, end.y * cellSize + cellSize/2, rad, 0, 2*np.pi)
        ctx.fill()

        ctx.set_source_rgb(HOLE_COL[0],HOLE_COL[1],HOLE_COL[2])
        if not self.isFork:
            ctx.arc(start.x * cellSize + cellSize/2, start.y * cellSize + cellSize/2, rad/2, 0, 2*np.pi)
        ctx.arc(end.x * cellSize + cellSize/2, end.y * cellSize + cellSize/2, rad/2, 0, 2*np.pi)
        ctx.fill()

    def draw_wire(self):
        ctx.set_source_rgb(WIRE_COL[0], WIRE_COL[1], WIRE_COL[2])
        ctx.set_line_width(lineWidth)
        if self.isFork:
            ctx.set_line_width(lineWidth/1.5)

        ctx.move_to(self.start.x*cellSize+cellSize/2,self.start.y*cellSize+cellSize/2)
        for i in range(0,len(self.cells)-1):
            cell = self.cells[i]
            next_cell = self.cells[i+1]
            ctx.line_to(next_cell.x*cellSize+cellSize/2,next_cell.y*cellSize+cellSize/2)
        ctx.stroke()

        self.draw_vias()
