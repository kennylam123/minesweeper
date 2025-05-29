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