import pygame
import playerClass as pc
  
# Define the background colour
# using RGB color coding.
background_colour = (0, 0, 0)
curplayer = pc.player()


  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 100))
  
# Set the caption of the screen
pygame.display.set_caption('Stick Game !')
  
# Fill the background colour to the screen
screen.fill(background_colour)
  
# Update the display using flip
pygame.display.flip()


  
# Variable to keep our game loop running
running = True
  
# game loop
while running:
    
# for loop through the event queue 
    screen.blit(curplayer.player_object, (curplayer.x, curplayer.y))
 
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
            
            
            
"""
class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#FF0000"))
        self.rect = Rect(x, y, 32, 32)

        self.reset(150, 400) 
        """        