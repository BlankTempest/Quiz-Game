import pygame,random


pygame.init()                                            
mainclock = pygame.time.Clock()

#window creation
size = [1024, 768]
screen = pygame.display.set_mode(size)                                 

#window icon, change it later
image_icon = pygame.image.load('images\icon.jpg')    # make sure icon res is smol
pygame.display.set_icon(image_icon)

#tabs
score = 0
lives = 3


#---------------------------------menu--------------------------------------
pygame.display.set_caption("Menu Screen")

show_menu = True
done = False

#music
pygame.mixer.music.load('music/theme/menu_mha2.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

#menu loop
while not done and  show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:         
                done = False
                pygame.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                show_menu = False
        if event.type == pygame.constants.USEREVENT:
            #triggered when song ends
            pygame.mixer.music.play()



    #background, change this, it looks like crap
    ibackground = pygame.image.load("images\instructions_background.png").convert()
    ibackground_position = [0,0]
    screen.blit(ibackground,ibackground_position)
    black = [0,0,0]
    
    font = pygame.font.Font(None, 80)

    text = font.render("Quiz Game", True, black)
    screen.blit(text, [300, 280])

    font = pygame.font.Font(None, 30)

    text = font.render("Click anywhere to start", True, black)
    screen.blit(text, [300, 350])

    pygame.display.flip()
    mainclock.tick(60)
#----------------------------------------------------------------------------


#window name, change it later
pygame.display.set_caption('Quiz Game')   

#background
background = pygame.image.load("images/background_boxed.png").convert()
background_position = [0,0]
screen.blit(background,background_position)

#importing the questions
def question_import(filename):  
    questions_file = open(filename, "r" , encoding='cp1252')
    #we'll use these outside
    global question,option_1,option_2,option_3,option_4,right_answer

    question = questions_file.readline()
    option_1 = questions_file.readline()
    option_2 = questions_file.readline()
    option_3 = questions_file.readline()
    option_4 = questions_file.readline()
    right_answer = questions_file.readline()

    questions_file.close()

l=["text\q&a1.txt","text\q&a2.txt","text\q&a3.txt","text\q&a4.txt","text\q&a5.txt","text\q&a6.txt","text\q&a6.txt","text\q&a7.txt","text\q&a8.txt","text\q&a9.txt","text\q&a10.txt"
    ,"text\q&a11.txt","text\q&a12.txt","text\q&a13.txt","text\q&a14.txt","text\q&a15.txt"]

random.shuffle(l)

def question_selecter():
    
    fname = l[0]
    l.pop(0)
    question_import(fname)


#----------------------------gamu start----------------------------------

def question_1():
    question_selecter()
    option1 = pygame.Rect((110,325), (150,101))
    option2 = pygame.Rect((325,325),(150,101))
    option3 = pygame.Rect((110,450), (150,101))
    option4 = pygame.Rect((325,450),(150,101))
    question1 = pygame.Surface([150,101])
    screen.blit(option2, (option2.x, option2.y))
    screen.blit(option1, (option1.x, option1.y))
    screen.blit(option3, (option3.x, option3.y))
    screen.blit(option4, (option4.x, option4.y))   
    pygame.display.flip()







#------------------------------------------------------------------------

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

