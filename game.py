import pygame
import random

# from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

###############################################333 title
pygame.display.set_caption('Space inveder')

#################################################icon
image=pygame.image.load('alian.png')
pygame.display.set_icon(image)

################################################background

image=pygame.image.load('abc.jpg')
back_image=pygame.transform.scale(image,(800,600))


###sound

# mixer.music.load('background.wav')
# mixer.music.play(-1)

###########################################3player

player_image=pygame.image.load('jet.png')
playerX=300
playerY=480
playerX_change=0

##########inveder
invader_image=pygame.image.load('alian.png')
invaderX=random.randint(0,800)
invaderY=random.randint(50,150)
invaderX_change=0.5
invaderY_change=40


######bullet
bullet_image=pygame.image.load('alian.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.5
bullet_state='ready'


########3#function
def player(x,y):
    screen.blit(player_image,(playerX,playerY))

def invader(x,y):
    screen.blit(invader_image,(invaderX,invaderY))    


def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet_image,(x+16,y+16))

running=True

while running:

#background color
    screen.fill((0,0,0))
    screen.blit(back_image,(0,0))
    

###key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quite key is pressed')
            running=False

        if event.type==pygame.KEYDOWN:
            print('key is pressed')
            if event.key== pygame.K_LEFT:
                # print('left key is pressed')
                playerX_change= -0.8

            elif event.key==pygame.K_RIGHT:
                # print('right key is pressed')
                playerX_change=0.8

            elif event.key==pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)    

        if event.type==pygame.KEYUP:
            # print('key is released')
            playerX_change=0
        
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                print('key is left is released or right key is released')
    
    
    ###############################boundary
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
        
    playerX += playerX_change # playerX = playerX + playerX_change
    invaderX += invaderX_change

    if invaderX<=0:
        invaderX_change=0.5
        invaderY += invaderY_change
    elif invaderX>=736:
        invaderX_change=-0.5
        invaderY += invaderY_change
        
    if bulletY <=0:
        bulletY=480
        bullet_state='ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change    

    
    
    ################################calling
    player(playerX,playerY)
    invader(invaderX,invaderY)
    
    pygame.display.update()        