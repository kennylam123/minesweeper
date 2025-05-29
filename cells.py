from buttons import create_button

class Cell:

    def __init__(self, parent_frame, is_mine=False):
        self.is_mine=is_mine
        self.is_flagged=False
        self.is_revealed=False
        
        self.button=create_button(
            parent=parent_frame,
            width=4,
            height=2,
            command=self.on_click

    )
    

    def on_click(self): 
        if self.is_flagged or self.is_revealed:
            return
        if self.is_mine: #lost game
            print('game over')


    def reveal(self):
        self.is_revealed=True
        self.button.config(
            text='',
            bg='gray'
        )



        