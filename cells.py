from buttons import create_button



class Cell:

    def __init__(self, parent_frame, x, y, board_ref):
        self.x=x
        self.y=y
        self.board_ref=board_ref
        self.is_mine=False
        self.is_flagged=False
        self.is_revealed=False
        self.neighbor_bomb_count=0
        
        self.button=create_button(
            parent=parent_frame,
            width=2,
            height=1,
            

    )
        
        self.button.bind("<Button-1>", self.on_left_click)
        self.button.bind("<Button-3>", self.on_right_click)


    def on_left_click(self,event=None): 
       if self.is_flagged or self.is_revealed:
           return
       if self.is_mine:
           self.button.config(text='💣')
           print('lost game')
           self.board_ref.game_over_popup
       else:
           self.reveal()

      
       print('leftclicked')

    def on_right_click(self, event=None): #fix being able to flag a revealed bomb
        if self.is_revealed:
            return
        if not self.is_revealed and self.is_mine:
            self.button.config(text='🚩', fg='red')


        
        self.is_flagged= not self.is_flagged
        
        if self.is_flagged:
            self.button.config(text='🚩', fg='red')
            print('flagged')
        else:
            self.button.config(text='', fg='lightgray')
            print('unflagged')

    def count_adjacent_mines(self):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = self.x + dx
                ny = self.y + dy
                if dx == 0 and dy == 0:
                    continue
                if 0 <= ny < len(self.board_ref.cells) and 0 <= nx < len(self.board_ref.cells[0]):
                    neighbor = self.board_ref.cells[ny][nx]
                    if neighbor.is_mine:
                        count += 1
        return count


    def reveal(self):
        self.is_revealed=True
        
        if self.neighbor_bomb_count > 0:
            self.button.config(
            text=str(self.neighbor_bomb_count),
            bg="lightgray"
        )
        else: 
            self.button.config(
                text=str(self.count_adjacent_mines()), 
                bg='lightgray'
                )
           

        
             
    
