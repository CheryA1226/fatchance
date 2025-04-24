
import random
import pgzrun
import sys
from pgzhelper import *


#####COLORS 

pink = (213, 3, 178)
black = (0, 0, 0)
white = (255,255,255)
purple = (98, 5, 213)
blue = (4, 0, 127)



HEIGHT = 500
WIDTH = 1000

#####BACK_GROUND

sky = Actor('blue_sky')
sky.x = 500
sky.y = 250
sky.scale = 10 

##COwBOI
cow = Actor('cow1')
cow.scale = 4
cow.x = 200
cow.y = 300
cow.fps = 7
cow.images = ['cow1','cow2']

#####SHAKR
shr = Actor('shark1')
shr.y = 100
shr.x = 270
shr.images = ['shark1','shark2','shark3']

######IMPORTANT STUFFF

velocity = 0 #jump speed

gravity = 0.8 #change velocity


####INTERFACE BG
this_is_not_offincive = {'cow', 
                         'raindow_sky',
                         }
start = random.choice(list(this_is_not_offincive))
random_start = Actor(start)
random_start.x = 500
random_start.y = 250
random_start.scale = 10

###########################Start 
start_game = False


######GAME_OVER 
game_over = False
def update():
    global gravity 
    global velocity 
    global start_game
    if keyboard.x and start_game == False:
        start_game = True
    
    ###########COWBOI
    cow.animate()

    #jump in air

    if keyboard.up and cow.y == 300:
        velocity = -18
    cow.y += velocity  
    velocity += gravity

    ## voide death 
    if cow.y > 300:
        velocity = 0 
        cow.y = 300



##########SHARK

### SHARK
    shr.animate()
    shr.scale = 3
    if cow.colliderect(shr):
        shr.x = random.randint(600, 3000)
        shr.y = random.randint(300, 2000)
        game_over == False 
## MOVE SHARK
    if game_over == False:
        shr.x -= 6
    ## VOID SHARK
    if shr.x < -50:
        shr.x = random.randint(900, 5000)
        shr.y = random.randint(250, 350)



def draw():
    global start_game
    if start_game == False: 
        random_start.draw()
        ####start Text
        screen.draw.filled_rect(Rect(180, 150, 600, 200), (black))
        screen.draw.text("Fat Chance", centerx = 500, centery = 250, color =(pink), fontname='snow', fontsize= 80)
        screen.draw.text('Press x To Start', centerx = 500, centery = 300, color =(pink), fontname ='snow', fontsize = 40 ) 
    elif start_game == True:
        sky.draw()
        cow.draw()
        shr.draw()
    elif game_over == True:
        
        
    

pgzrun.go()