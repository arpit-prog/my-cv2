from tkinter import Frame,Label,CENTER


import constant2048 as c ##constant file2048.py
import Logic as L ###logic file2048.py

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.master.bind("<key>",self.key_down)
        self.commands={c.KEY_UP:L.move_up,c.KEY_DOWN:L.move_down,
                      c.KEY_LEFT:L.move_left,c.KEY_RIGHT:L.move_right
                      }

        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()
    def init_grid(self):
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,
                        width=c.SIZE,height=c.SIZE)

        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)


                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=
                         c.GRID_PADDING)

                t=Label(master=cell,text="",
                       bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=
                       CENTER,front=c.FONT,width=5,hieght=2)
                t.grid()
                grid_row.append(grid_row)


            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix=L.startgame()
        L.add_2(self.matrix)
        L.add_2(self.matrix)
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number ==0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY
                        )
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[
                        new_number],fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                L.add_2(self.matrix)
                self.update.grid_cells()
                changed=False
                if L.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="you",
                        bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text=
                        'win!',bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if L.get_current_state(self.matrix)=="LOST":
                    self.grid.cells[1][1].configure(
                        text="you",bg=c.BACKGROUND_COLOR_CELL_EMPTY
                    )
                    self.grid.cells[1][2].configure(
                        text="lose!!",bg=c.BACKGROUND_COLOR_CELL_EMPTY
                        )
h=Game2048()










