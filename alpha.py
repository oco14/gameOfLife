import random as rnd
import pyglet

#creates a one dimentional cellular automata 
#currently set to rule 30
class Alpha:
    def __init__ (self,window_width,window_height,cell_size):
        self.grid_width = int(window_width/cell_size)
        self.grid_height = int(window_height/cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.generate_cells()

    #randomly generates the original line of cells
    def generate_cells(self):
      for row in range(0,self.grid_height):
        self.cells.append([])
        for col in range(0,self.grid_width):
               
            if rnd.random() < 0.4 and row == 0:
                self.cells[row].append(1)
            else:
                    self.cells[row].append(0)
    

    #generating the next generation
    def run_rules(self):
        
        #deleting cells no longer on the screen
        if len(self.cells) > 60:
            del self.cells[60]
            
        newRow = []
        for col in range(0,self.grid_width):
            if col == 0:
                 x= self.get_cell_value(0,self.grid_width-1)
                 y= self.get_cell_value(0,col)
                 z= self.get_cell_value(0,col+1)
            elif col == self.grid_width:
                 x= self.get_cell_value(0,self.grid_width-2)
                 y= self.get_cell_value(0,self.grid_width-1)
                 z= self.get_cell_value(0,0)
            else:
                x= self.get_cell_value(0,col-1)
                y= self.get_cell_value(0,col)
                z= self.get_cell_value(0,col+1)

            if x is 0:
                if y is 0:
                    if z is 0:
                        newRow.append(0)
                    elif z is not 0:
                        newRow.append(1)
                elif y is not 0:
                    if z is 0:
                        newRow.append(1)
                    elif z is not 0:
                        newRow.append(1)
            elif x is not 0:
                if y is 0:
                    if z is 0:
                        newRow.append(1)
                    elif z is not 0:
                        newRow.append(0)
                elif y is not 0:
                    if z is 0:
                        newRow.append(0)
                    elif z is not 0:
                        newRow.append(0)
        self.cells.insert(0,newRow)
    
    #determining if a cell is active 
    def get_cell_value(self,row,col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
           return self.cells[row][col]
        return 0

    
    def draw(self):
        for row in range(0,self.grid_height):
            for col in range(0,self.grid_width):
                if self.cells[row][col] == 1:
                    #(0,0) (0,20) (20,0) (20,20)
                    sqaure_coords = (row * self.cell_size,                  col * self.cell_size,
                                     row * self.cell_size,                  col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                   
                   
                    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_TRIANGLES,
                                                [0,1,2,1,2,3],
                                                ('v2i',(sqaure_coords))) 