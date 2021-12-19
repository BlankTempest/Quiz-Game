import pygame,random

pygame.init()                                            
mainclock = pygame.time.Clock()

#window creation
size = [1024, 768]
screen = pygame.display.set_mode(size)                                 

#window icon, change it later
image_icon = pygame.image.load('images\icon.jpg')    # make sure icon res is smol
pygame.display.set_icon(image_icon)


#we're using the main function to loop the game after the game over screen
def main():


    #---------------------------------menu--------------------------------------

    def menu_function():
        #quit button
        quit = (255,255,255)
        quit_dark = (100,100,100)
        quit_light = (170,170,170)
        smallfont = pygame.font.SysFont('Raleway',35)
        quit_text = smallfont.render('QUIT' , True , quit)
        
        #title
        pygame.display.set_caption("Menu Screen")



        done = False
        show_menu = True

        #music
        menu_theme = pygame.mixer.Sound('music/theme/menu_mha2.mp3')
        menu_theme.play(-1)            #-1 loops music indefinitely

        #menu loop
        while not done and  show_menu:

            mouse = pygame.mouse.get_pos()
            x=870
            y=665

            #exit loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:         
                        done = False
                        pygame.quit()
                        quit()

            #checks if the button is clicked within the constraints
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                            pygame.quit()
                        else:
                            #'click anywhere'
                            menu_theme.stop()
                            show_menu = False

            #changes the color of the button when mouse is hovered over it
            if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                pygame.draw.rect(screen,quit_light,[x,y,140,40])   
            else:
                pygame.draw.rect(screen,quit_dark,[x,y,140,40])
        
            screen.blit(quit_text , (x+40,y+10))
            pygame.display.flip()


            #background, change this, it looks like crap
            mbackground = pygame.image.load("images\instructions_background.png").convert()
            mbackground_position = [0,0]
            screen.blit(mbackground,mbackground_position)
            black = [0,0,0]
        
            font = pygame.font.Font(None, 80)

            #you could get rid of these text blits 
            # and edit the background directly and write on it through paint
            text = font.render("Quiz Game", True, black)
            screen.blit(text, [300, 280])

            font = pygame.font.Font(None, 30)

            text = font.render("Click anywhere to start", True, black)
            screen.blit(text, [300, 350])

            #vsync
            mainclock.tick(60)

    menu_function()
    #----------------------------------------------------------------------------


    #window name, change it later
    pygame.display.set_caption('Quiz Game')   

    #background, make sure not to mess with the boxes if you change it,
    # or you'll have to redefine x1-y1 etc again
    background = pygame.image.load("images/background_boxed.png").convert()
    background_position = [0,0]
    screen.blit(background,background_position)

    #importing the questions
    def question_import(filename):  
        questions_file = open(filename, "r" , encoding='cp1252')
        #we'll use these outside
        global question,option_1,option_2,option_3,option_4,right_answer

        # .strip() gets rid of blank space at the end
        question = questions_file.readline().strip()  
        option_1 = questions_file.readline().strip() 
        option_2 = questions_file.readline().strip() 
        option_3 = questions_file.readline().strip() 
        option_4 = questions_file.readline().strip() 
        right_answer = questions_file.readline().strip() 

        questions_file.close()

    l=["text\q&a1.txt","text\q&a2.txt","text\q&a3.txt","text\q&a4.txt","text\q&a5.txt","text\q&a6.txt","text\q&a6.txt","text\q&a7.txt","text\q&a8.txt","text\q&a9.txt","text\q&a10.txt"
        ,"text\q&a11.txt","text\q&a12.txt","text\q&a13.txt","text\q&a14.txt","text\q&a15.txt"]

    random.shuffle(l)

    def question_selecter():
        
        fname = l[0]
        l.pop(0)
        question_import(fname)


    #----------------------------gamu start----------------------------------

    def question_screen():

        question_selecter()
        #so now we have question,option_1,option_2,option_3,option_4 and right_answer
        
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Corbel',35)
        '''color_dark = (100,100,100)
        color_light = (170,170,170)
        text = smallfont.render('quit' , True , color)''' #used for boundary check, will get rid of later

        #we need to blit something over the screen so that it 
        # gets rid of previous text, hence the background again
        screen.blit(background,background_position)

        open = True
        #we don't need to define these, but they'll come in use eventually
        x1 = 216; x2 = 214; x3 = 595; x4 = 596
        y1 = 509; y2 = 595; y3 = 505; y4 = 596

        #music, will be changed to one song per category when categories are added
        music_list=['music/theme/dn_ost7.mp3','music/theme/category3_10billion.mp3','music/theme/l_theme.mp3','music/theme/menu_drstone.mp3','music/theme/near_theme.mp3',
                'music/theme/overlord_dungeon_alt.mp3','music/theme/dn_ost7.mp3','music/theme/category3_10billion.mp3','music/theme/l_theme.mp3',
                'music/theme/menu_drstone.mp3','music/theme/near_theme.mp3','music/theme/overlord_dungeon_alt.mp3','music/theme/category3_10billion.mp3',
                'music/theme/menu_drstone.mp3','music/theme/dn_ost7.mp3','music/theme/l_theme.mp3']
        music_name = music_list[question_no]
        
        music_theme = pygame.mixer.Sound(music_name)
        music_theme.play(-1)

        #counters
        global score,lives,game_over
        
        score_counter = smallfont.render('Score:'+str(score) , True , color)
        lives_counter = smallfont.render(str(lives) , True , color)
        lives_counter = smallfont.render(str(lives) , True , color)
        screen.blit(score_counter , (32,18))
        screen.blit(lives_counter , (32,56))

        lives_img = pygame.image.load("images/heart.png").convert()
        screen.blit(lives_img,(54,60))

        #sfx lose life
        normal_hit= pygame.mixer.Sound('music\sfx\Hit Normal Damage.mp3')
        heavy_hit = pygame.mixer.Sound('music\sfx\Hit Super Effective.mp3')
        #sfx score up
        score_up = pygame.mixer.Sound('music\sfx\sfx_score_up_Level Up!.mp3')

        while open:
            mouse = pygame.mouse.get_pos()

            #DO NOT TRY TO SHORTEN THIS BIT, or it'll bug out
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:          #turn this into a pause menu later on
                        open = False
                        pygame.quit()
                #option1
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    music_theme.stop()
                    if 172 <= mouse[0] <= 471 and 494 <= mouse[1] <= 543:
                        if question_no < 15:
                            answer = option_1
                            if answer == right_answer:
                                score += 1
                                score_up.play()
                                open = False                    #wrong answe = game over screen or -1 lives
                            else:
                                lives -= 1
                                normal_hit.play()
                                open = False                #score board goes here
                            if lives == 0:
                                heavy_hit.play()
                                game_over = True
                                open = False
                        else:
                            pygame.quit()
                #option2
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if 170 <= mouse[0] <= 843 and 582 <= mouse[1] <= 630:
                        if question_no < 15:
                            answer = option_2
                            if answer == right_answer:
                                score += 1
                                score_up.play()
                                open = False
                            else:
                                lives -= 1
                                normal_hit.play()
                                open = False
                            if lives == 0:
                                heavy_hit.play()
                                game_over = True
                                open = False
                        else:
                            pygame.quit()
                #option3
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if 545 <= mouse[0] <= x3+320 and 493 <= mouse[1] <= 540:
                        if question_no < 15:
                            answer = option_3
                            if answer == right_answer:
                                score += 1
                                score_up.play()
                                open = False
                            else:
                                lives -= 1
                                normal_hit.play()
                                open = False
                            if lives == 0:
                                heavy_hit.play()
                                game_over = True
                                open = False
                        else:
                            pygame.quit()
                #option4
                if event.type == pygame.KEYDOWN and event.key == pygame.MOUSEBUTTONDOWN:          #exception
                    if 544 <= mouse[0] <= 842 and 581 <= mouse[1] <= 632:
                        if question_no < 15:
                            answer = option_4
                            if answer == right_answer:
                                score += 1 
                                score_up.play()
                                open = False
                            else:
                                lives -= 1
                                normal_hit.play()
                                open = False
                            if lives == 0:
                                heavy_hit.play()
                                game_over = True
                                open = False
                        else:
                            pygame.quit()
            
            
            #to test the boundaries of the option boxes when needed
            '''
            if x1 <= mouse[0] <= x1+320 and y1 <= mouse[1] <= y1+40:
                pygame.draw.rect(screen,color_light,[x1,y1,320,45])   
            else:
                pygame.draw.rect(screen,color_dark,[x1,y1,320,45])
            '''

            #display
            question_display= smallfont.render(question , True, color)
            option_1_display= smallfont.render(option_1 , True, color)
            option_2_display= smallfont.render(option_2 , True, color)
            option_3_display= smallfont.render(option_3 , True, color)
            option_4_display= smallfont.render(option_4 , True, color)

            screen.blit(question_display, (208,370))
            screen.blit(option_1_display, (x1,y1))
            screen.blit(option_2_display, (x2,y2))
            screen.blit(option_3_display, (x3,y3))
            screen.blit(option_4_display, (x4,y4))
            
            
            pygame.display.update()
            pygame.display.flip()

            #framerate limiter/vsync
            mainclock.tick(60)

    
    for question_no in range(1,16):
        if game_over != True:
            question_screen()
    ##########################################################################


    #--------------------------GAME OVER-----------------------------------

    '''Add a score board after this screen
    You only see this screen if you lost all lives'''

    def game_over_screen():
        #title
        pygame.display.set_caption("Game Over")

        #music
        end_theme = pygame.mixer.Sound('music/theme/gameover_kata.mp3')
        end_theme.play(-1)

        #background
        background_select = random.randint(1,2)

        if background_select == 1:
            ebackground = pygame.image.load("images\game_over.png").convert()
        else:
            ebackground = pygame.image.load("images\game_over2.png").convert()

        ebackground_position = [0,0]
        screen.blit(ebackground,ebackground_position)

        #game over loop
        done = False
        end_screen = True
        
        while not done and end_screen:

            #exit loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:         
                        done = False
                        pygame.quit()
                        quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #loop back to menu screen
                    end_theme.stop()
                    return
                    

            #vsync
            mainclock.tick(60)   
            pygame.display.flip()
            pygame.display.update()

        
        

    if game_over == True:
        game_over_screen()




    ###########################################################################

    #the loop below isn't needed since we implement this into every screen
    '''
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

    '''
while True:
    score = 0
    lives = 3
    game_over = False

    main()