import pyglet
from game_of_life_aging import GameOfLife

#runs aging.py in a visual pyglet window
class Window(pyglet.window.Window):

    def __init__(self):
        super(Window,self).__init__()
        self.set_size(1000,1000)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10)
        pyglet.clock.schedule_interval(self.update,1.0/25.0)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()
       
    def update(self,dt):
        self.gameOfLife.run_rules()

if __name__ == '__main__':
    window = Window()
    pyglet.app.run() 