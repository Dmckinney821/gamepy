import pygame
from background import Background
import time
import random
from bullet import Bullet
from guy import Guy
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0,0,255)
bright_blue = (0, 135, 255)
yellow = (255,242,0)
green = (0,255,0)

all_sprites = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
guy_width = 45


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Party')
clock = pygame.time.Clock()

guy = Guy(450, 500)

def duck_missed(count):
    font = pygame.font.SysFont(None, 75)
    text = font.render('Missed' + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def ducks(duckx, ducky, duckw, duckh, color):
    pygame.draw.rect(gameDisplay, color, [duckx, ducky, duckh, duckw,])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def playNotificationSount():
    pygame.mixer.music.load("haha.wav")
    pygame.mixer.music.play()

def message_display(text):
    endText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(text, endText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update() 
    
    
    time.sleep(5)

    game_loop()

def crash():
    message_display('Ha Ha')
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
        gameDisplay.fill(white)
        endText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('Yee Haw', endText)
        textRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(2)

def game_loop():
    x = (display_width * 0.35)
    y = (display_height * 0.8)
    x_change = 0

    duck_startx = random.randrange(0, display_width)
    duck_starty = random.randrange(450, 0, -450)
    duck_speed = -5
    duck_width = 25
    duck_height = 25
    gameExit = False
    missed = 0
    background = Background('woods.png')
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    guy.move(-5)
                elif event.key == pygame.K_RIGHT:
                    guy.move(5)
                elif event.key == pygame.K_SPACE:
                    guy.shoot()

                    print('we\re shooting')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    guy.move(0)
            
                

            
            

      
        gameDisplay.fill(white) 
        gameDisplay.fill([255, 255, 255])
        gameDisplay.blit(background.image, background.rect) 

        ducks(duck_startx, duck_starty, duck_width, duck_height, black)
        duck_starty += duck_speed

        #guy(x, y)
        guy.render(gameDisplay)
        for bullet in guy.bullets:
            bullet.update()
            bullet.render(gameDisplay)

    

        duck_missed(missed)


        if x > display_width - guy_width or x < 0:
            crash()
        #print(duck_starty)
        if duck_starty < 0:
            duck_height = duck_starty
            duck_startx = random.randrange(0, display_width)
            duck_starty = random.randrange(450, 0, -450, )
            missed += 1
            duck_speed += -1
            duck_height += (missed * 1.5)
        if y < duck_starty + duck_height:
            print('height cross')
            if x > duck_startx and x < duck_startx + duck_width or x + duck_width > duck_startx and x + duck_width < duck_startx +duck_width:
                print( 'x cross')
                crash()


        pygame.display.update() 
        clock.tick(200)


print('intro')


game_loop()

pygame.quit()

quit()