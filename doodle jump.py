#lets make doodle jump!

import pygame

pygame.init()

#library of game contants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HIDGHT = 500

player = pygane.image.load('doodle.png')
fps = 60
font = pygame.font.Font('freesansbold.ttf',16)
timer = pygame.time.Clock()

#gane variables
player_x = 178
player_y = 488

#creare screen
screen = pygane.display.set_node([WIDTH, HEIGHT])
pygane.display.set_caption('Doodle Jumper')

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x,player_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.display.flip()
pygane.quit()


        
 

            
            
            
            
            
            

