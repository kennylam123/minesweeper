from buttons import create_button

class Cell:

    def __init__(self, parent_frame, x, y):
        self.x=x
        self.y=y
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
       else:
           self.reveal()

      
       print('leftclicked')

    def on_right_click(self, event=None): #fix being able to flag a revealed bomb
        if self.is_revealed:
            return
        
        
        self.is_flagged= not self.is_flagged
        if self.is_mine:
            return
        if self.is_flagged:
            self.button.config(text='🚩', fg='red')
            print('flagged')
        else:
            self.button.config(text='', fg='lightgray')
            print('unflagged')



    def reveal(self):
        self.is_revealed=True
        if self.neighbor_bomb_count > 0:
            self.button.config(
            text=str(self.neighbor_bomb_count),
            bg="lightgray"
        )
        else: 
            self.button.config(
            text='',
            bg="lightgray"
        )
             
        
             
    
