import pygame,random,time,pyttsx3

pygame.init()              
pygame.font.init()           
mainclock = pygame.time.Clock()


#tts 
'''
tts = pyttsx3.init()
tts.setProperty('rate', 200)
tts.setProperty('volume', 2)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" 

# Use female voice
tts.setProperty('voice', voice_id)
'''

#window creation
size = [1024, 768]
screen = pygame.display.set_mode(size, pygame.NOFRAME)        

#for fullscreen
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  
#pygame.display.toggle_fullscreen()  

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

        #player name
        global player_name
        player_name_font = pygame.font.Font(None, 40)
        player_text = open('text\scoreboard\player_name.txt', 'r')
        player_name = player_text.read(5)
        player_text.close()
        name_rect = pygame.Rect(320, 387, 175, 32)
        color_active = pygame.Color('azure2')
        color_inactive = pygame.Color('azure3')
        color = color_inactive

        done = False
        show_menu = True
        active = False

        #background, change this, it looks like crap
        mbackground = pygame.image.load("images\instructions_background.png").convert()
        mbackground_position = [0,0]
        screen.blit(mbackground,mbackground_position)
        #pygame.display.update()
        
        #music
        menu_theme = pygame.mixer.Sound('music/theme/menu_mha2.mp3')
        menu_theme.play(-1)            #-1 loops music indefinitely
        
        #menu loop
        while not done and  show_menu:

            mouse = pygame.mouse.get_pos()
            x1=870
            y1=665

            #exit loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:         
                        done = False
                        pygame.quit()
                        exit()

                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif len(player_name) < 5:
                        player_name += event.unicode #forms string

                #text box
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if name_rect.collidepoint(event.pos):
                        active = True

                    elif x1 <= mouse[0] <= x1+140 and y1 <= mouse[1] <= y1+40:
                        pygame.quit()
                        exit()
                    else:
                        #'click anywhere'
                        menu_theme.stop()
                        show_menu = False
                        active = False
                        player_text = open('text\scoreboard\player_name.txt', 'w')
                        player_name = player_name.upper()
                        player_text.write(player_name)
                        player_text.close()

            #changes the color of the button when mouse is hovered over it
            if x1 <= mouse[0] <= x1+140 and y1 <= mouse[1] <= y1+40:
                pygame.draw.rect(screen,quit_light,[x1,y1,140,40])   
            else:
                pygame.draw.rect(screen,quit_dark,[x1,y1,140,40])
        
            screen.blit(quit_text , (x1+40,y1+10))

            black = [0,0,0]
            font = pygame.font.Font(None, 80)

            #you could get rid of these text blits 
            # and edit the background directly and write on it through paint
            text = font.render("Quiz Game", True, black)
            screen.blit(text, [300, 280])

            font = pygame.font.Font(None, 30)

            text = font.render("Click anywhere to start", True, black)
            screen.blit(text, [300, 350])

            #player name text box
            if active:
                color = color_active
            else:
                color = color_inactive

            pygame.draw.rect(screen, color, name_rect)
            name_surface = player_name_font.render(player_name, True, (0, 0, 0))
            screen.blit(name_surface, (name_rect.x+5, name_rect.y+5))

            #vsync
            pygame.display.flip()
            pygame.display.update()
            mainclock.tick(60)

    menu_function()
    #----------------------------------------------------------------------------


    #window name, change it later
    pygame.display.set_caption('Quiz Game')   

    #background, make sure not to mess with the boxes if you change it,
    # or you'll have to redefine x1-y1 etc again
    background = pygame.image.load("images/hollow_purple.png").convert()
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

                   
        
        #next
        next_c = (255,255,255)
        next_text = smallfont.render('NEXT' , True , next_c)
        next_dark = (100,100,100)
        next_light = (170,170,170)
        
        pygame.display.update()
            
        #sound_once = True

        question_answered = False

        while open:
            mouse = pygame.mouse.get_pos()
            '''
            while sound_once:
                #sort of a mess, gotta use gtts instead
                screen.blit(question_display, (208,370))
                pygame.display.update()
                tts.say(question)
                tts.runAndWait()

                screen.blit(option_1_display, (x1,y1))
                pygame.display.update()
                tts.say(option_1)
                tts.runAndWait()

                screen.blit(option_2_display, (x2,y2))
                pygame.display.update()
                tts.say(option_2)
                tts.runAndWait()

                screen.blit(option_3_display, (x3,y3))
                pygame.display.update()
                tts.say(option_3)
                tts.runAndWait()
                
                screen.blit(option_4_display, (x4,y4))
                pygame.display.update()
                tts.say(option_4)
                tts.runAndWait()

                sound_once = False'''


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:          #turn this into a pause menu later on
                        open = False
                        pygame.quit()
                        exit()
                
                bulk_exec = False

                

                if question_answered == False:
                    if event.type == pygame.MOUSEBUTTONDOWN: 

                    #option1
                        if 172 <= mouse[0] <= 471 and 494 <= mouse[1] <= 543:
                            answer = option_1
                            bulk_exec = True
                            music_theme.stop()
                            question_answered = True
                    #option2
                        elif 170 <= mouse[0] <= 843 and 582 <= mouse[1] <= 630:
                            answer = option_2
                            bulk_exec = True
                            music_theme.stop()
                            question_answered = True
                    #option3
                        elif 545 <= mouse[0] <= x3+320 and 493 <= mouse[1] <= 540:
                            answer = option_3
                            bulk_exec = True
                            music_theme.stop()
                            question_answered = True
                    #option4
                        elif 544 <= mouse[0] <= 842 and 581 <= mouse[1] <= 632:
                            answer = option_4
                            bulk_exec = True
                            music_theme.stop()
                            question_answered = True
                    #counters
                    #if it screams answer isnt defined, do answer = ''
                        if bulk_exec == True:
                            if question_no < 15:
                                
                                if answer == right_answer:
                                    score += 1 
                                    score_up.play()
                                    color = 'green'
                                else:
                                    lives -= 1
                                    normal_hit.play()
                                    color = 'red'
                                if lives == 0:
                                    heavy_hit.play()
                                    game_over = True
                                    open = False
                            elif question_no == 15:
                                if answer == right_answer:
                                    score += 1
                                    score_up.play()  
                                    game_over = False    
                                    color = 'green'
                                else:
                                    lives -= 1
                                    normal_hit.play()  
                                    game_over = False  
                                    color = 'red' 
                                if lives == 0:
                                    heavy_hit.play()
                                    game_over = True
                                    open = False
                            bulk_exec = False

            #display
            color1 = 'white'
            question_display= smallfont.render(question , True, color1)
            option_1_display= smallfont.render(option_1 , True, color)            
            option_2_display= smallfont.render(option_2 , True, color)           
            option_3_display= smallfont.render(option_3 , True, color)           
            option_4_display= smallfont.render(option_4 , True, color) 

            screen.blit(question_display, (208,370))
            screen.blit(option_1_display, (x1,y1))
            screen.blit(option_2_display, (x2,y2))
            screen.blit(option_3_display, (x3,y3))
            screen.blit(option_4_display, (x4,y4))

            #next button
            
            if x1 <= mouse[0] <= x1+140 and y1 <= mouse[1] <= y1+40:
                pygame.draw.rect(screen,next_light,[x1,y1,140,40])   
            else:
                pygame.draw.rect(screen,next_dark,[x1,y1,140,40])

            screen.blit(next_text , (x1+40,y1+10))

            #to test the boundaries of the option boxes when needed
            '''
            if x1 <= mouse[0] <= x1+320 and y1 <= mouse[1] <= y1+40:
                pygame.draw.rect(screen,color_light,[x1,y1,320,45])   
            else:
                pygame.draw.rect(screen,color_dark,[x1,y1,320,45])
            '''

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
                    exit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:         
                        pygame.quit()
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #loop back to menu screen
                    end_theme.stop()
                    #return
                    done = True
                    

            #vsync
            mainclock.tick(60)   
            pygame.display.flip()
            pygame.display.update()


    if game_over == True:
        game_over_screen()

    ###########################################################################

    global show_score_menu,show_highscore_menu, first, second
    show_score_menu = True
    show_highscore_menu = False
    first = True
    second = True

    #------------------------------Score Board--------------------------------#
    def score_board():
        
        #these are only the recent scores
        pink = (255, 192, 203)
        yellow = (255,255,0)

        #quit button
        quit_light = (170,170,170)
        swamp_green = (2,75,64)
        swamp_ltgreen = (0,66,60)

        smallfont = pygame.font.SysFont('Raleway',35)
        quit_text = smallfont.render('QUIT' , True , yellow)

        #menu button
        menu_text = smallfont.render('MENU' , True , yellow)

        #recent button
        time_text = smallfont.render('TIME' , True , yellow)

        #highest button
        score_text = smallfont.render('SCORE' , True , yellow)



        #replace font with the one from hotline miami
        score_font2 = pygame.font.SysFont('Arial Rounded MT Bold',60)

        #title
        pygame.display.set_caption("Score Board")

        #time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        
        global first
        while first:
            #storing and taking scores from text file
            score_file_temp = open('text\scoreboard\saved_user_responses_temp.txt','w')
            score_file = open('text\scoreboard\saved_user_responses.txt','r')

            global player_name
        
            #score_saver
            #limit name to b/w 5 to 8 for better aligning, replace blank with player name
            if score > 9:
                score_file_temp.write('       '+ str(score)+ '                                    ' + current_time + '                         ' +player_name + '\n')
            else: 
                score_file_temp.write('       '+ '0' + str(score)+ '                                    ' + current_time + '                         ' +player_name + '\n')
            #^ to fix alignment

            score_file2 = score_file.read()
            for line in score_file2:
                score_file_temp.write(line)
        
            score_file.close()
            score_file_temp.close()
        
            score_file_temp = open('text\scoreboard\saved_user_responses_temp.txt','r')
            score_file = open('text\scoreboard\saved_user_responses.txt','w')

            score_file2 = score_file_temp.read()
            for line in score_file2:
                score_file.write(line)
            score_file.close()
            score_file_temp.close()
            first = False
        
        global second
        while second:
            #score_saver
            score_file = open('text\scoreboard/not_sorted_scores.txt','a')
            if score > 9:
                score_file.write('       '+ str(score)+ '                                    ' + current_time + '                         ' +player_name + '\n')
            else:
                score_file.write('       '+ '0' + str(score)+ '                                    ' + current_time + '                         ' +player_name + '\n')
            score_file.close()

            #sort scores
            score_file = open('text\scoreboard/not_sorted_scores.txt','r')

            score_list=[]
            for line in score_file:
                score_list.append(line)
        
            score_file.close()

            score_list.sort(reverse = True)

            score_sorted = open("text\scoreboard\sorted_scores.txt",'w')
        
            for element in score_list:
                score_sorted.write(element)

            score_sorted.close()
            second = False

        global show_score_menu,show_highscore_menu

        #display scores
        if show_highscore_menu == True:
            score_file = open('text\scoreboard\sorted_scores.txt','r')
        else:
            score_file = open('text\scoreboard\saved_user_responses.txt','r')

        #header
        score_display_top = score_font2.render('Score                         Time                           Name', True , yellow)

        score_font = pygame.font.SysFont('papyrus',40)
        score_font3 = pygame.font.SysFont('papyrus',36)
        #sort scores:
        sort_text = score_font3.render( 'Sort by:', True , yellow)

        #i guess can be shortended with score_display_i in a loop of some sort
        var = score_file.readline().strip()
        score_display_1 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_2 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_3 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_4 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_5 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_6 = score_font.render( var, True , pink)
        var = score_file.readline().strip()
        score_display_7 = score_font.render( var, True , pink)
        
        score_file.close()
        #^ this whole thing took me three hours to figure out

        #background
        sbackground = pygame.image.load("images\hotline_miami3.jpg").convert()
        sbackground_position = [0,0]
        screen.blit(sbackground,sbackground_position)

        #display scores
        screen.blit(score_display_top , (40,58))
        screen.blit(score_display_1 , (40,145))
        screen.blit(score_display_2 , (40,221))
        screen.blit(score_display_3 , (40,294))
        screen.blit(score_display_4 , (40,370))
        screen.blit(score_display_5 , (40,446))
        screen.blit(score_display_6 , (40,519))
        screen.blit(score_display_7 , (40,596))

        pygame.display.flip()
        pygame.display.update()

        x=870
        y=710
        x1 = 700
        x2 = 200
        x3 = 370

        done = False
        show_score = True
        

        while not done and  show_score:

            mouse = pygame.mouse.get_pos()
            #quit button
            if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                pygame.draw.rect(screen,swamp_ltgreen,[x,y,140,40]) 
            else:
                pygame.draw.rect(screen,swamp_green,[x,y,140,40])  

            #menu button
            if x1 <= mouse[0] <= x1+140 and y <= mouse[1] <= y+40:
                pygame.draw.rect(screen,swamp_ltgreen,[x1,y,140,40]) 
            else:
                pygame.draw.rect(screen,swamp_green,[x1,y,140,40])

            #time button
            if x2 <= mouse[0] <= x2+140 and y <= mouse[1] <= y+40:
                pygame.draw.rect(screen,swamp_ltgreen,[x2,y,140,40]) 
            else:
                pygame.draw.rect(screen,swamp_green,[x2,y,140,40])
            
            #highscore button
            if x3 <= mouse[0] <= x3+140 and y <= mouse[1] <= y+40:
                pygame.draw.rect(screen,swamp_ltgreen,[x3,y,140,40]) 
            else:
                pygame.draw.rect(screen,swamp_green,[x3,y,140,40])
            
            screen.blit(sort_text , (40,700))
            screen.blit(quit_text , (x+40,y+10))
            screen.blit(menu_text , (x1+40,y+10))
            screen.blit(time_text , (x2+40,y+10))
            screen.blit(score_text , (x3+30,y+10))
            
            #vsync
            pygame.display.flip()
            mainclock.tick(60)
            pygame.display.update()
            
            #exit loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:         
                        pygame.quit()
                        exit()
                #quit button
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                            pygame.quit()
                            exit()
                #menu button
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if x1 <= mouse[0] <= x1+140 and y <= mouse[1] <= y+40:
                            show_score_menu = False
                            show_highscore_menu = False
                            done = True
                            return
                #recent score button
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if x2 <= mouse[0] <= x2+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = False
                            return
                #highscore button
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if x3 <= mouse[0] <= x3+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = True
                            return


    while show_score_menu == True or show_highscore_menu == True:
        score_board()

###########################################################################

while True:
    score = 0
    lives = 3
    game_over = False

    main()