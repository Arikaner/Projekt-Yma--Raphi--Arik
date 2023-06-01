#lets make doodle jump!

import pygame

pygame.init()

#library of game contants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HIDGHT = 500

player = pygane.transform.scale(pygane.inage.load('doodle.png'),(90, 70))
fps = 60
font = pygame.font.Font('freesansbold.ttf',16)
timer = pygame.time.Clock()

#gane variables
player_x = 170
player_y = 400
platforms = [[175, 480, 70, 10]]
jump = False
y_change = 0

#creare screen
screen = pygane.display.set_node([WIDTH, HEIGHT])
pygane.display.set_caption('Doodle Jumper')

#check for collisions with blocks
def check_collisions(rect, list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list{1}.colliderect([player_x, player_y + 60, 90, 10]) and jump == False and y_change > 0:
            j = True
    return jump


#update player y position every loop
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = 1
    if jump:
        y_change -= jump_height
        jump = False
    y_pos = y_change
    y_change = gravity
    return y_position

running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x,player_y))
    blocks = []
    
    for i in range(len(platforms)):
        block = pygame.dran.rect(screen, black, platforms[1], 0, 3)
        blocks.append(block)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player_y = update_player(player_y)
    jump = check_collisions(blocks, jump) 
            
            
    pygame.display.flip()
pygane.quit()


    

        
 

            
            
            
            
            
            

