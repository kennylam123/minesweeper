from tkinter import *
from buttons import create_button
from cells import Cell
from board import Board
import settings
import utils


root = Tk()
root.configure(bg="black")

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
w = Label(root, text='MineSweeper')
w.pack()

root.resizable(False,False)



top_frame = Frame(
    root,
    bg='black',
    width=utils.width_perc(100),
    height=utils.height_perc(15)
)
top_frame.place(x=0, y=0)

title_label=Label(
    top_frame,
    text=('Minesweeper Game'),
    bg='black',
    fg='white',
    font=('Helvetica', 20, 'bold')
)

title_label.place(relx=0.5, rely=0.5, anchor='center')

exit_button=create_button(
    root, 
    text='Exit', 
    width=25, 
    command=root.destroy
    )
exit_button.place(
    relx=0.5,
    rely=1.0,
    anchor='s',
    y=-30
)

grid_frame=Frame (root)
grid_frame.place(relx=0.5, rely=0.5, anchor='center')
game_board = Board(grid_frame, settings.rows, settings.rows,50)

play_button=create_button(
    top_frame,
    text='Play',
    width=25,
    command=game_board.start_game

)
play_button.place(relx=0.5, rely=0.8, anchor='center')


root.mainloop()