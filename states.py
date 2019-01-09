import pyglet
from alpha import Alpha

#runs alpha.py which is a 1-dim cellular automatta
class Window(pyglet.window.Window):
    
    def __init__(self):
      
        super(Window,self).__init__()
        self.set_size(600,600)
        self.alpha = Alpha(self.get_size()[0],
                                     self.get_size()[1],
                                     10)
        pyglet.clock.schedule_interval(self.update,1.0/30.0)

    def on_draw(self):
       
        self.clear()
        self.alpha.draw()
       
    def update(self,dt):
        self.alpha.run_rules()

if __name__ == '__main__':
    window = Window()
    pyglet.app.run() 