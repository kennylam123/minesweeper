from cells import Cell
import settings
import utils

class Board:

    def __init__ (self,parent, rows, cols):
      self.parent=parent
      self.rows=rows
      self.cols=cols
      self.grid= []

    def start_game(self):
          for y in range(settings.rows):
            row = []
            for x in range(settings.cols):
                cell = Cell(self.parent)
                cell.button.grid(row=y, column=x)  # place button in grid
                row.append(cell)
            self.grid.append(row)

    def setAdjMines(self):
        for row in self.grid:
          for cell in row:
             if cell.is_mine:
                continue
             count=0
             for neighbor in self.get_neighbors(cell):
                if neighbor.is_mine:
                   count+=1
                   cell.neighborMines=count

    
             