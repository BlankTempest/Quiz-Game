import pygame

pygame.init()                                             #initializes pygame

display = pygame.display.set_mode((800,600))
pygame.display.update()                                   #updates the window with new dimensions

pygame.display.set_caption('Game window xxx')             #set the window name  

open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
#we use the above loop so that the window doesn't close immediately. Hitting the X will close the window.


pygame.quit()
quit()