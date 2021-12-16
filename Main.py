import pygame,time,sys,random


pygame.init()                                            
mainclock = pygame.time.Clock()

#window creation
width = 1024
height = 768
screen = pygame.display.set_mode([width,height])                                 

#window name, change it later
pygame.display.set_caption('Quiz Game')   

#window icon, change it later
image_icon = pygame.image.load('images/icon.jpg')    # make sure icon res is 512x512
pygame.display.set_icon(image_icon)

#background
green = (0,255,0) 
red = (255,0,0)
#screen.fill(green)  
background = pygame.image.load("images/background_boxed.png").convert()
background_poistion = [0,0]
screen.blit(background,background_poistion)

score = 0

#exit loop
open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update() 


pygame.display.flip()       #idk if this is needed here

pygame.quit()
quit()