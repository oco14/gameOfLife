# gameOfLife
Conways game of life with some added rules

There are three different pyglet window classes that will each run a different 
cellular automatta simulation. 

1)- states.py will run a 1-dim cellular automatta that is set a rule 30. the rules/class is in Alpha.py

2)- aging.py will run a version of conways game of life with some modified rules.
         the longer a cell is active the "older" it gets. after a certain age the cell dies and "blooms"
         where all the surronding cells become active. the rules/class is game_of_life_aging.py
         
3)- mixRun.py will run a simulation of conways game a life with a few added rules.
         The longer a cell is active the older it becomes after a certain age the cell will "bloom" 
         causing all surronding cells to become active
         The difference between this and aging rules is that a new cell is created it 
         inherites the colors of its parents. also when a cell blooms the new surronding cells will 
         have the same color but with 50 added to the green value
         when a cell would obtain a green color value of over 255 the green color is cleared and 50 is added to blue
         the same is true for blue to red
