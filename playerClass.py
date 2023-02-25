class player:
    x = None
    y  = None
    #player_object = pygame.image.load('Player_image.png')
    
    
    def __init__(self) :
        self.x = 0
        self.y = 0


    def moveLeft(x):
        self.x = x - 1

    def moveRight(x): 
        self.x = x + 1

    def moveDown(x, y):
        self.y = y + 1
        
    def moveUp(y):
        self.y = y - 1

    def updatePos(player, direction):
        if direction == "w":
            moveUp(player.y)
        if direction == "a":
            moveLeft(player.x)
        if direction == "s":
            moveDown(player.y)
        if direction == "d":
            moveRight(player.x)    

