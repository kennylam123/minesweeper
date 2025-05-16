from tkinter import *
import settings

root = Tk()
root.configure(bg="black")
root.title('Minesweeper')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
w = Label(root, text='MineSweeper')
w.pack()

root.resizable(False,False)



button=Button(root, text='Exit', width=25, command=root.destroy)
button.pack()
root.mainloop()