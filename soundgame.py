
import pygame

def playNotificationSount():
    
    pygame.mixer.music.load("haha.wav")
    pygame.mixer.music.play()
   

playNotificationSount()


while loop that calls gameloop at the top to call it 

gameDisplay(playNotificationSount())