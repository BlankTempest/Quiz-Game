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
background = pygame.image.load("images/background_boxed.png").convert()
background_poistion = [0,0]
screen.blit(background,background_poistion)

#tabs
score = 0
lives = 3

#assigning the questions' file
def question_assign():
    global filename
    if question_no == 1:
        filename = "text\q&a1.txt"
    elif question_no == 2:
        filename = "text\q&a2.txt"
    elif question_no == 3:
        filename = "text\q&a3.txt"
    elif question_no == 4:
        filename = "text\q&a4.txt"
    elif question_no == 5:
        filename = "text\q&a5.txt"
    elif question_no == 6:
        filename = "text\q&a6.txt"
    elif question_no == 7:
        filename = "text\q&a7.txt"
    elif question_no == 8:
        filename = "text\q&a8.txt"
    elif question_no == 9:
        filename = "text\q&a9.txt"
    elif question_no == 10:
        filename = "text\q&a10.txt"
    elif question_no == 11:
        filename = "text\q&a11.txt"
    elif question_no == 12:
        filename = "text\q&a12.txt"
    elif question_no == 13:
        filename = "text\q&a13.txt"
    elif question_no == 14:
        filename = "text\q&a14.txt"
    elif question_no == 15:
        filename = "text\q&a15.txt"


#importing the questions
def question_import():  
    questions_file = open(filename, "r" , encoding='cp1252')
    #we'll use this outside
    global question,option_1,option_2,option_3,option_4,right_answer

    question = questions_file.readline()
    option_1 = questions_file.readline()
    option_2 = questions_file.readline()
    option_3 = questions_file.readline()
    option_4 = questions_file.readline()
    right_answer = questions_file.readline()

    questions_file.close()


#gamu start
question_no=1
question_assign()
question_import()








#exit loop
open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:          #turn this into a pasue menu later on
                open = False
                pygame.quit()
                quit()
    pygame.display.update()                           #idk if this is needed here
    pygame.display.flip()       

    #framerate limiter/vsync
    mainclock.tick(60)

