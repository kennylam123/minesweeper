from cells import Cell
import settings
import utils
import random

class Board:

    def __init__ (self,parent, rows, cols, num_bombs):
      self.parent=parent
      self.rows=rows
      self.cols=cols
      self.grid= []
      self.num_bombs=num_bombs

    def create_cells(self):
        self.cells=[]
        for y in range(self.rows):
            row = []
            for x in range(self.cols):
                cell = Cell(self.parent,x,y,self)
                cell.button.grid(row=y, column=x)  # place button in grid
                row.append(cell)
            self.cells.append(row)
    
    
            

    def place_bombs(self):
      all_cells=[cell for row in self.cells for cell in row]
      bombs= random.sample(all_cells,self.num_bombs)
      for bomb_cell in bombs:
         bomb_cell.is_mine=True

    def count_neighbor_bombs(self):
      for row in self.cells:
         for cell in row:
            if not cell.is_mine:
               neighbors=self.get_neighbors(cell)
               cell.neighbor_bomb_count=sum(1 for n in neighbors if n.is_mine)
    
    def get_neighbors(self,cell):
      neighbors = []
      for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                neighbors.append(self.cells[ny][nx])
      return neighbors

    def start_game(self):
      self.create_cells()
      self.place_bombs()
      self.count_neighbor_bombs


    

    
             