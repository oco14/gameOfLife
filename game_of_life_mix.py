import random as rnd
import pyglet


class Cell:
        def __init__(self,live,old=0,colorL=[0,0,0]):
            self.alive = live
            self.age = old
            self.color = colorL

        
   
#a simulation of conways game a life with a few added
#rules. The longer a cell is active the older it becomes
#after a certain age the cell will "bloom" causing all 
#surronding cells to become active
#The difference between this and aging rules is that a 
#new cell is created it inherites the colors of its parents
#also when a cell blooms the new surronding cells will 
#have the same color but with 50 added to the green value
#when a cell would obtain a green color value of over 255
#the green color is cleared and 50 is added to blue
#the same is true for blue to red
class GameOfLife:
    
    def __init__ (self,window_width,window_height,cell_size):
        self.grid_width = int(window_width/cell_size)
        self.grid_height = int(window_height/cell_size)
        self.cell_size = cell_size
        self.cells = []
        self.generate_cells()

    #randomily starts the board with blooming cells
    def generate_cells(self):
        for row in range(0,self.grid_height):
            self.cells.append([])
            for col in range(0,self.grid_width):
               
                if rnd.random() < 0.001:
                   a=10
                   b=0
                   c=0
                   cl = [a,b,c]
                   self.cells[row].append(Cell(1,1000,cl))
                 
                else:                 
                     self.cells[row].append(Cell(0,0))
        

    #generates the next generation
    def run_rules(self):
        temp = []
        for row in range(0,self.grid_height):
            temp.append([])
            for col in range(0,self.grid_width):
                
                cell_sum =self.get_sum(row,col)
                
                bloom = self.get_bloom(row,col)
                               
                if bloom[0] == 1:
                    color = bloom[1]
                    color[0] += 50
                    #color[0] += 50
                    #color[1] += 50
                    #color[2] += 50
                    if color[2] > 255:
                        color[2] = 255
                        color[1] = 255
                        color[0] = 255
                    elif color[0] > 255:
                        color[0] %= 255
                        color[1] += 50
                    elif color[1] > 255:
                        color[1] %= 255
                        color[2] += 50
                   
                    temp[row].append(Cell(1,0,bloom[1]))
                elif self.cells[row][col].alive == 0 and cell_sum ==3:
                    color = self.get_ave_color(row,col)
                    temp[row].append(Cell(1,0,color))
                elif self.cells[row][col].alive == 1 and (cell_sum == 3 or cell_sum == 2) and self.cells[row][col].age < 770:
                    color = self.get_ave_color(row,col)
                    temp[row].append(Cell(1,self.cells[row][col].age+25,color))
                else:
                    temp[row].append(Cell(0))
        self.cells = temp
    

    def get_cell_value(self,row,col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
           return self.cells[row][col].alive
        return 0

    #find the amount of alive cells in a cells surroundings
    def get_sum(self,row,col):
        lis = self.get_list(row,col)
        x = sum(self.get_cell_value(item[0], item[1]) for item in lis)
        # x = sum(lis, key = lambda item: self.get_cell_value(item[0], item[1]))
        return x
   

    def get_cell_age(self,row,col):
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
           return self.cells[row][col].age
        return 0

    #returns a list of surrounding cells
    def get_list(self,row,col):
        lis = [(row + 1,   col - 1),
                 (row + 1, col),
                 (row + 1, col + 1),
                 (row,     col - 1),
                 (row,     col + 1),
                 (row - 1, col - 1),
                 (row - 1, col),
                 (row - 1, col + 1)]
        return lis

    #determines if a near by cell is blooming and its color if it does
    def get_bloom(self,row,col):
        rt = [0,0]
        lis = self.get_list(row,col)
        ageCol = [(self.get_cell_age(x[0],x[1]),self.get_color(x[0],x[1])) for x in lis]
        trip = max(ageCol, key = lambda item: item[0])
        if trip[0] > 755:
            rt[0] = 1
            rt[1] = trip[1]
        return rt

    #returns a cells color
    def get_color(self,row,col):
        rt = [0,0,0]
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:         
           rt = self.cells[row][col].color
        return rt

    #returns the average of multiple colors
    def get_ave_color(self,row,col):
        rt = [0,0]
        lis = self.get_list(row,col)
        colList = [self.get_color(x[0],x[1]) for x in lis if self.get_cell_value(x[0],x[1]) == 1]
        #print(colList)
        color = [0,0,0]
        if len(colList) == 2:
            div = 2
        else:
            div = 3

        for x in colList:
            color[0] = int(color[0] + x[0]/div)%255
            color[1] = int(color[1] + x[1]/div)%255
            color[2] = int(color[2] + x[2]/div)%255
        return color




    def draw(self):
        for row in range(0,self.grid_height):
            for col in range(0,self.grid_width):
                if self.cells[row][col].alive == 1:
                    #(0,0) (0,20) (20,0) (20,20)
                    sqaure_coords = (row * self.cell_size,                  col * self.cell_size,
                                     row * self.cell_size,                  col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    
                    color = self.cells[row][col].color
                    a,b,c = color[0],color[1],color[2]
                    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_TRIANGLES,
                                                [0,1,2,1,2,3],
                                                ('v2i',(sqaure_coords)),
                                                ('c3B', (a,b,c,
                                                         a,b,c,
                                                         a,b,c,
                                                         a,b,c))) 
                