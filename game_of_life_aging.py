import random as rnd
import pyglet

class Cell:
        def __init__(self,live,old=0):
            self.alive = live
            self.age = old
        
   
#conways game of life with some modified rules
#the longer a cell is active the "older" it gets
#after a certain age the cell dies and "blooms"
#where all the surronding cells become active
class GameOfLife:
    
    def __init__ (self,window_width,window_height,cell_size):
        self.grid_width = int(window_width/cell_size)
        self.grid_height = int(window_height/cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.generate_cells()

    #randomily selects cells to start the simulation as active
    def generate_cells(self):
        for row in range(0,self.grid_height):
            self.cells.append([])
            for col in range(0,self.grid_width):
               
                if rnd.random() < 0.4:
                    self.cells[row].append(Cell(1,0))
                 
                else:
                  
                     self.cells[row].append(Cell(0,0))
        
    #determins the next generation
    def run_rules(self):
        temp = []
        for row in range(0,self.grid_height):
            temp.append([])
            for col in range(0,self.grid_width):
                cell_sum = sum([self.get_cell_value(row - 1, col),
                                self.get_cell_value(row - 1, col - 1),
                                self.get_cell_value(row,     col - 1),
                                self.get_cell_value(row + 1, col - 1),
                                self.get_cell_value(row + 1, col),
                                self.get_cell_value(row + 1, col + 1),
                                self.get_cell_value(row,     col + 1),
                                self.get_cell_value(row - 1, col + 1)])
                if self.get_bloom(row - 1, col)     == 1  or self.get_bloom(row - 1, col - 1) == 1 or self.get_bloom(row,     col - 1) == 1 or self.get_bloom(row + 1, col - 1) == 1 or self.get_bloom(row + 1, col)     == 1 or self.get_bloom(row + 1, col + 1) == 1 or  self.get_bloom(row,     col + 1) == 1 or  self.get_bloom(row - 1, col + 1) == 1:
                    bloom = 1
                else:
                    bloom = 0
                
                if bloom == 1:
                     temp[row].append(Cell(1))
                elif self.cells[row][col].alive == 0 and cell_sum ==3:
                    temp[row].append(Cell(1))
                elif self.cells[row][col].alive == 1 and (cell_sum == 3 or cell_sum == 2) and self.cells[row][col].age < 770:
                    temp[row].append(Cell(1,self.cells[row][col].age+25))
                else:
                    temp[row].append(Cell(0))
        self.cells = temp
    
    
    def get_cell_value(self,row,col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
           return self.cells[row][col].alive
        return 0

    #determines if a near by cell has bloomed
    def get_bloom(self,row,col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
            if self.cells[row][col].age > 765:
                return 1
            else:
                return 0
        return 0

    def draw(self):
        for row in range(0,self.grid_height):
            for col in range(0,self.grid_width):
                if self.cells[row][col].alive == 1:
                    #(0,0) (0,20) (20,0) (20,20)
                    sqaure_coords = (row * self.cell_size,                  col * self.cell_size,
                                     row * self.cell_size,                  col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    a=255-self.cells[row][col].age
                    b=0
                    if a < 0:
                        b = 255+a
                        a=0
                    c=0
                    if b < 0:
                        c = 255 +b
                        b=0
                    if c < 0:
                        c=255
                        b=255
                        a=255
                    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_TRIANGLES,
                                                [0,1,2,1,2,3],
                                                ('v2i',(sqaure_coords)),
                                                ('c3B', (a,b,c,
                                                         a,b,c,
                                                         a,b,c,
                                                         a,b,c))) 
                