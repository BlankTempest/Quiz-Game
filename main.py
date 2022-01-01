import pygame
import random
import time
import os #to set window loc

os.environ['SDL_VIDEO_WINDOW_POS'] = '480,125'
pygame.init()              
pygame.font.init()           
pygame.display.init()
mainclock = pygame.time.Clock()

#window creation
size = [1024, 768]
#for borderless option
screen = pygame.display.set_mode(size, pygame.NOFRAME)

#for fullscreen option
#pygame.display.toggle_fullscreen()
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#for windowed option,
# needs restart
#screen = pygame.display.set_mode(size)


#window icon, change it later
# make sure icon res is smol
image_icon = pygame.image.load('images\icon.jpg')
pygame.display.set_icon(image_icon)



#--------------------------------------------------------------------

#we're using the main function to loop the game after the game over screen
def main():

        #something for the future
        #screenshot button, cause why not
        ##im1 = pyautogui.screenshot()
        ##im1.save('my_screenshot.png')
        ###im2 = pyautogui.screenshot('my_screenshot2.png')

        #something else for later
        # pygame.mouse.set_cursor(pygame.cursors.Cursor)
    
    global score,lives,game_over,ques_ans,total_questions,zen_mode
    score = 0
    lives = 3
    game_over = False
    ques_ans = 0
    total_questions = 15
    zen_mode = False
    #---------------------------------menu--------------------------------------

    def menu_function():
        
        #title
        pygame.display.set_caption("aenigma: Menu Screen")

        #player name
        #####################move to profile screen##########################
        global player_name,total_questions,zen_mode
        
        player_text = open('text\scoreboard\player_name.txt', 'r')
        player_name = player_text.read(5)
        player_text.close()
        '''player_name_font = pygame.font.Font(None, 40)
        name_rect = pygame.Rect(320, 387, 175, 32)
        color_active = pygame.Color('azure2')
        color_inactive = pygame.Color('azure3')
        color = color_inactive
        active = False'''
        #####################################################################
        done = False
        show_menu = True

        #background
        mbackground = pygame.image.load("images/naissancee4.png").convert()
        mbackground_position = [0,0]
        
        #music
        menu_theme = pygame.mixer.Sound('music/theme/Pauline Oliveiros  A Woman Sees How the World Goes with No Eyes.mp3')
        menu_theme.play(-1)            #-1 loops music indefinitely

        #sfx
        menu_rollover = pygame.mixer.Sound('music/sfx/menu rollover.mp3')
        menu_click = pygame.mixer.Sound('music/sfx/Menu-click.mp3')
        #if when game is started and the mouse happens to be on any button,
        # then it'll throw an error, so we define these here
        sfx_play_1 = True
        sfx_play_2 = True
        sfx_play_3 = True
        sfx_play_4 = True
        sfx_play_5 = True
        sfx_play_6 = True
        sfx_play_7 = True

        #menu selectables
        #when not hovered over
        m_play = pygame.image.load("images/menu_play.png").convert()
        m_zen = pygame.image.load("images/menu_zen.png").convert()
        m_options = pygame.image.load("images/menu_options.png").convert()
        m_help = pygame.image.load("images/menu_help.png").convert()
        m_profile = pygame.image.load("images/menu_profile.png").convert()
        m_category = pygame.image.load("images/menu_category.png").convert()
        m_exit = pygame.image.load("images/menu_exit.png").convert()

        #when hovered over
        m_play_w = pygame.image.load("images/menu_play_w.png").convert()
        m_zen_w = pygame.image.load("images/menu_zen_w.png").convert()
        m_options_w = pygame.image.load("images/menu_options_w.png").convert()
        m_help_w = pygame.image.load("images/menu_help_w.png").convert()
        m_profile_w = pygame.image.load("images/menu_profile_w.png").convert()
        m_category_w = pygame.image.load("images/menu_category_w.png").convert()
        m_exit_w = pygame.image.load("images/menu_exit_w.png").convert()

        #top bar
        top_text_font = pygame.font.SysFont('Arial', 18)
        top_text_color = (35,35,35)
        
        #menu loop
        while not done and  show_menu:

            mouse = pygame.mouse.get_pos()
            x= 90
            top_text_str = 'Welcome to aenigma'
            
            #assign these first since we collidepoint underneath
            screen.blit(mbackground,mbackground_position)

            #play
            if x <= mouse[0] <= x+134 and 214 <= mouse[1] <= 214+34:
                m_play_blit = screen.blit(m_play_w ,(x,214))
                top_text_str = 'Start a new game.'
                #play sfx
                if sfx_play_1 == True:
                    menu_rollover.play()
                    sfx_play_1 = False 
            else:
                sfx_play_1 = True
                m_play_blit = screen.blit(m_play ,(x,214))

            #zen
            if x <= mouse[0] <= x+134 and 273 <= mouse[1] <= 273+33:
                m_zen_blit = screen.blit(m_zen_w ,(x,273))
                top_text_str = 'Go up against the maximum number of questions.'
                #play sfx
                if sfx_play_2 == True:
                    menu_rollover.play()
                    sfx_play_2 = False 
            else:
                sfx_play_2 = True
                m_zen_blit = screen.blit(m_zen ,(x,273))
            
            #options
            if x <= mouse[0] <= x+135 and 333 <= mouse[1] <= 333+32:
                m_options_blit = screen.blit(m_options_w ,(x,333))
                top_text_str = 'Change graphic options.'
                #play sfx
                if sfx_play_3 == True:
                    menu_rollover.play()
                    sfx_play_3 = False 
            else:
                sfx_play_3 = True
                m_options_blit = screen.blit(m_options ,(x,333))
            
            #help
            if x <= mouse[0] <= x+136 and 391 <= mouse[1] <= 391+35:
                m_help_blit = screen.blit(m_help_w , (x,391))
                top_text_str = 'Look at how the game mechanics work.'
                #play sfx
                if sfx_play_4 == True:
                    menu_rollover.play()
                    sfx_play_4 = False 
            else:
                sfx_play_4 = True
                m_help_blit = screen.blit(m_help , (x,391))
            
            #profile
            if x <= mouse[0] <= x+134 and 451 <= mouse[1] <= 451+34:
                m_profile_blit = screen.blit(m_profile_w , (x,451))
                top_text_str = 'Change you allias.'
                #play sfx
                if sfx_play_5 == True:
                    menu_rollover.play()
                    sfx_play_5 = False 
            else:
                sfx_play_5 = True
                m_profile_blit = screen.blit(m_profile , (x,451))

            #category
            if x <= mouse[0] <= x+135 and 511 <= mouse[1] <= 511+32:
                m_category_blit = screen.blit(m_category_w , (x,511))
                top_text_str = 'Choose what categories to answer from.'
                #play sfx
                if sfx_play_6 == True:
                    menu_rollover.play()
                    sfx_play_6 = False 
            else:
                sfx_play_6 = True
                m_category_blit = screen.blit(m_category , (x,511))
            
            #exit
            if x <= mouse[0] <= x+135 and 605 <= mouse[1] <= 605+34:
                top_text_str = 'Exit the game and return to your reality'
                m_exit_blit = screen.blit(m_exit_w , (x,605))
                #play sfx
                if sfx_play_7 == True:
                    menu_rollover.play()
                    sfx_play_7 = False 
            else:
                sfx_play_7 = True
                m_exit_blit = screen.blit(m_exit , (x,605))

            #top text
            top_text = top_text_font.render(top_text_str , True , top_text_color)
            screen.blit(top_text, [94, 66])


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

                    '''move to profile screen
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif len(player_name) < 5:
                        player_name += event.unicode #forms string'''

                
                if event.type == pygame.MOUSEBUTTONDOWN:
                #play button
                    if m_play_blit.collidepoint(event.pos):
                        menu_theme.stop()
                        menu_click.play()
                        show_menu = False
                        '''move to profile screen
                        active = False
                        player_text = open('text\scoreboard\player_name.txt', 'w')
                        player_name = player_name.upper()
                        player_text.write(player_name)
                        player_text.close()'''

                    if m_zen_blit.collidepoint(event.pos):
                        total_questions = 47
                        zen_mode = True
                        menu_theme.stop()
                        menu_click.play()
                        show_menu = False

                    if m_options_blit.collidepoint(event.pos):
                        menu_click.play()
                        pass

                    if m_help_blit.collidepoint(event.pos):
                        menu_click.play()
                        pass

                    if m_profile_blit.collidepoint(event.pos):
                        menu_click.play()
                        pass

                    if m_category_blit.collidepoint(event.pos):
                        menu_click.play()
                        pass

                    if m_exit_blit.collidepoint(event.pos):
                        menu_theme.stop()
                        menu_click.play()
                        pygame.quit()
                        exit()
                        


                    '''move to profile screen
                    if name_rect.collidepoint(event.pos):
                        active = True'''
                        

            #player name text box
            '''move to profile screen
            if active:
                color = color_active
            else:
                color = color_inactive

            pygame.draw.rect(screen, color, name_rect)
            name_surface = player_name_font.render(player_name, True, (0, 0, 0))
            screen.blit(name_surface, (name_rect.x+5, name_rect.y+5))'''

            #vsync
            pygame.display.flip()
            pygame.display.update()
            mainclock.tick(60)

    menu_function()
    #----------------------------------------------------------------------------

    #window name, change it later
    pygame.display.set_caption('aenigma')

    #importing the questions
    def question_import(filename):  
        questions_file = open(filename, "r" , encoding='cp1252')
        #we'll use these outside
        global question,option_1,option_2,option_3,option_4,right_answer,music_ques

        # .strip() gets rid of blank space at the end
        question = questions_file.readline().strip()  
        option_1 = questions_file.readline().strip() 
        option_2 = questions_file.readline().strip() 
        option_3 = questions_file.readline().strip() 
        option_4 = questions_file.readline().strip() 
        right_answer = questions_file.readline().strip() 
        music_ques = questions_file.readline().strip() 
        music_ques = 'music/music_based/' + music_ques

        questions_file.close()

    #47 questions in total
    #l=["text\q&a1.txt","text\q&a2.txt","text\q&a3.txt","text\q&a4.txt","text\q&a5.txt","text\q&a6.txt","text\q&a7.txt","text\q&a8.txt","text\q&a9.txt","text\q&a10.txt"
        #,"text\q&a11.txt","text\q&a12.txt","text\q&a13.txt","text\q&a14.txt","text\q&a15.txt"]

    #if music category selected:
    l_m = ['text\music_based\q1.txt','text\music_based\q2.txt','text\music_based\q3.txt','text\music_based\q4.txt','text\music_based\q5.txt','text\music_based\q6.txt',
        'text\music_based\q7.txt','text\music_based\q8.txt','text\music_based\q9.txt','text\music_based\q10.txt','text\music_based\q11.txt','text\music_based\q12.txt',
        'text\music_based\q13.txt','text\music_based\q14.txt','text\music_based\q15.txt','text\music_based\q16.txt','text\music_based\q17.txt']

    #if history category is selected:
    l_h = ["text\history\q1.txt","text\history\q2.txt","text\history\q3.txt","text\history\q4.txt","text\history\q5.txt","text\history\q6.txt","text\history\q7.txt"
        ,"text\history\q8.txt","text\history\q9.txt","text\history\q10.txt","text\history\q11.txt","text\history\q12.txt","text\history\q13.txt","text\history\q14.txt","text\history\q15.txt"]

    #specify that books' category also contains plays
    l_b = ["text/books/q1.txt","text/books/q2.txt","text/books/q3.txt","text/books/q4.txt","text/books/q5.txt","text/books/q6.txt","text/books/q7.txt"
        ,"text/books/q8.txt","text/books/q9.txt","text/books/q10.txt","text/books/q11.txt","text/books/q12.txt","text/books/q13.txt","text/books/q14.txt","text/books/q15.txt"]

    random.shuffle(l_h)
    random.shuffle(l_m)
    random.shuffle(l_b)
    global question_list
    question_list = []

    def question_selecter():
        #remove random chance and edit it with category chosen
        if zen_mode == True:
            chance = random.randint(1,3)
            if chance == 1:
                if l_h != []:
                    fname = l_h[0]
                    question_list.append(fname)
                    l_h.pop(0)
                elif l_b != []:
                    fname = l_b[0]
                    question_list.append(fname)
                    l_b.pop(0)
                else: 
                    fname = l_m[0]
                    question_list.append(fname)
                    l_m.pop(0)
            elif chance == 2:
                if l_m != []:
                    fname = l_m[0]
                    question_list.append(fname)
                    l_m.pop(0)
                elif l_h != 0: 
                    fname = l_h[0]
                    question_list.append(fname)
                    l_h.pop(0)
                else:
                    fname = l_b[0]
                    question_list.append(fname)
                    l_b.pop(0)
            elif chance == 3:
                if l_b != []:
                    fname = l_b[0]
                    question_list.append(fname)
                    l_b.pop(0)
                elif l_m != []: 
                    fname = l_m[0]
                    question_list.append(fname)
                    l_m.pop(0)
                else: 
                    fname = l_h[0]
                    question_list.append(fname)
                    l_h.pop(0)
            question_import(fname)

        else:
            #select randomly out of 2 categories
            chance = random.randint(1,3)
            if chance == 1:
                fname = l_h[0]
                question_list.append(fname)
                l_h.pop(0)
            elif chance == 2:
                fname = l_m[0]
                question_list.append(fname)
                l_m.pop(0)
            elif chance == 3:
                fname = l_b[0]
                question_list.append(fname)
                l_b.pop(0)
            question_import(fname)

    #----------------------------gamu start----------------------------------

    def question_screen():

        question_selecter()
        #so now we have question,option_1,option_2,option_3,option_4 and right_answer
        global question
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Corbel',35)
        '''color_dark = (100,100,100)
        color_light = (170,170,170)
        text = smallfont.render('quit' , True , color)''' #used for boundary check, will get rid of later

        #background
        if len(question) > 38:
            background = pygame.image.load("images/hollow_purple_bigger.png").convert()
        else:
            background = pygame.image.load("images/hollow_purple.png").convert()
        background_position = [0,0]
        screen.blit(background,background_position)
        #slicing
        if len(question) > 38:
            question1 = question[:37]
            question2 = question[37:]

        open = True
        #we don't need to define these, but they'll come in use eventually
        x1 = 216; x2 = 214; x3 = 595; x4 = 596; x5 = 870
        y1 = 509; y2 = 595; y3 = 505; y4 = 596; y5 = 665

        #music, will be changed to one song per category when categories are added
        music_list=['music/theme/dn_ost7.mp3','music/theme/category3_10billion.mp3','music/theme/l_theme.mp3','music/theme/menu_drstone.mp3','music/theme/near_theme.mp3',
                'music/theme/overlord_dungeon_alt.mp3']
        random.shuffle(music_list)
        music_name = music_list[0]
        
        #if music category
        if music_ques.endswith('.mp3'):
            music_theme = pygame.mixer.Sound(music_ques)
            music_theme.play()
        else:
            music_theme = pygame.mixer.Sound(music_name)
            music_theme.play(-1)

        

        #counters
        global score,lives,game_over,mod_50_used,answer,ques_ans,total_questions
        

        lives_img = pygame.image.load("images/heart.png").convert()
        lives_grey_img = pygame.image.load("images/heart_grey.png").convert()

        #sfx lose life
        normal_hit= pygame.mixer.Sound('music\sfx\Hit Normal Damage.mp3')
        heavy_hit = pygame.mixer.Sound('music\sfx\Hit Super Effective.mp3')
        #sfx score up
        score_up = pygame.mixer.Sound('music\sfx\sfx_score_up_Level Up!.mp3')
        #sfx 50-50 used
        mod_50_used_sfx = pygame.mixer.Sound('music/sfx/50-50-BodySlam.mp3')

        #timer
        font_timer = pygame.font.SysFont('Raleway', 76)
        frame_count = 0
        frame_rate = 60
        start_time = 8
        
        #mods
        mod_50 = pygame.image.load("images/50-50.png").convert()
        mod_50_grey = pygame.image.load("images/50-50-grey.png ").convert()
        

        #next
        next_c = (255,255,255)
        nextfont = pygame.font.SysFont('Raleway',35)
        
        pygame.display.update()

        question_answered = False
        bulk_exec = False
        third = True
        timed_out = False
        answer = ''
        #50-50 functionals
        option_1_visible = True
        option_2_visible = True
        option_3_visible = True
        option_4_visible = True
        mod_temp = True
        mod_50_being_used = False
        
        #50-50 effect
        tv_screen = pygame.image.load("images/tv_screen.jpg").convert()
        tv_screen_position = [0,0]
        while open:

            mouse = pygame.mouse.get_pos()

            #we need to blit something over the screen so that it 
            # gets rid of previous text, hence the background again
            screen.blit(background,background_position)

            #counters
            #lives_counter = smallfont.render(str(lives) , True , color)

            #render a greyed out heart instead
            if lives == 3:
                screen.blit(lives_img,(32,60))
                screen.blit(lives_img,(68,60))
                screen.blit(lives_img,(104,60))
            elif lives == 2:
                screen.blit(lives_img,(32,60))
                screen.blit(lives_img,(68,60))
                screen.blit(lives_grey_img,(104,60))
            elif lives == 1:
                screen.blit(lives_img,(32,60))
                screen.blit(lives_grey_img,(68,60))
                screen.blit(lives_grey_img,(104,60))
            elif lives == 0:
                screen.blit(lives_grey_img,(32,60))
                screen.blit(lives_grey_img,(68,60))
                screen.blit(lives_grey_img,(104,60))
            
            score_counter = smallfont.render('Score:'+str(score) , True , color)
            screen.blit(score_counter , (32,18))
            #screen.blit(lives_counter , (32,56))

            next_text = nextfont.render('NEXT' , True , next_c)

            #mods
            if mod_50_used == False:
                mod_50_blit = screen.blit(mod_50, [967, 27])
            else:
                mod_50_blit = screen.blit(mod_50_grey, [967, 27])
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #esc key to exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:    #turn this into a pause menu later
                        pygame.quit()
                        exit()

                if question_answered == False:
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                    #mod 50-50
                    #& so that it doesnt repeat for the next question
                        if mod_50_used != True:
                            if mod_50_blit.collidepoint(event.pos):
                                mod_50_used = True
                                mod_50_being_used = True 
                                mod_50_used_sfx.play()
                                screen.blit(tv_screen,tv_screen_position)
                                pygame.display.update()

                    #option1
                        if option_1_visible == True:
                            if 172 <= mouse[0] <= 471 and 494 <= mouse[1] <= 543:
                                answer = option_1
                                bulk_exec = True
                                question_answered = True
                    #option2
                        if option_2_visible == True:
                            if 170 <= mouse[0] <= 468 and  579<= mouse[1] <= 630:
                                answer = option_2
                                bulk_exec = True
                                question_answered = True
                    #option3
                        if option_3_visible == True:
                            if 545 <= mouse[0] <= 844 and 493 <= mouse[1] <= 540:
                                answer = option_3
                                bulk_exec = True
                                question_answered = True
                    #option4
                        if option_4_visible == True:
                            if 544 <= mouse[0] <= 842 and 581 <= mouse[1] <= 632:
                                answer = option_4
                                bulk_exec = True
                                question_answered = True
                    
                #next button
                if question_answered == True:
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if x5 <= mouse[0] <= x5+140 and y5 <= mouse[1] <= y5+40:
                            if lives == 0:
                                    game_over = True
                                    
                            open = False
                            music_theme.stop()

            #counters
            if bulk_exec == True:
                if answer == right_answer:
                    score += 1
                    score_up.play()  
                    #last question
                    if question_no == total_questions:
                        game_over = False

                else:
                    lives -= 1
                    question_answered = True
                    if lives == 0:
                        heavy_hit.play()
                    else:
                        normal_hit.play()
                    #last question
                    if question_no == total_questions:
                        game_over = False
                ques_ans += 1
                bulk_exec = False


            #timer box
            x6= 468; y6 = 12
            timerbox = pygame.image.load("images/timerbox.jpg").convert()
            screen.blit(timerbox, [x6, y6])

            #timer
            total_seconds = frame_count // frame_rate
            total_seconds = start_time - (frame_count // frame_rate)
            if question_answered == True:
                third = False
            if total_seconds <= 0:
                total_seconds = 0
                while third:
                    bulk_exec = True
                    third = False
                    timed_out = True
            
            output_string = str(total_seconds)
            text_timer = font_timer.render(output_string, True, 'white')
            screen.blit(text_timer, [x6+25, y6+15])

            if question_answered != True and mod_50_being_used == False:
                frame_count += 1

            
            #mod 50-50 display check, mod_temp to make it run once
            if mod_50_used == True and mod_temp == True and mod_50_being_used == True:
                option_list = [option_1,option_2,option_3,option_4]
                random.shuffle(option_list)
                temp_k=2
                for temp_option in option_list:
                    if temp_option != right_answer:
                        option_list.remove(temp_option)
                        temp_k -= 1
                        if temp_k == 0:
                            break
                mod_temp = False
                if option_1 not in option_list:
                    option_1_visible = False
                if option_2 not in option_list:
                    option_2_visible = False
                if option_3 not in option_list:
                    option_3_visible = False
                if option_4 not in option_list:
                    option_4_visible = False

                
            #display red/green
            color_white = 'white'
            color_green = 'green'
            color_red = 'red'
            

            
            if len(question) > 38:
                question_display1= smallfont.render(question1 , True, color_white)
                question_display2= smallfont.render(question2 , True, color_white)
            question_display= smallfont.render(question , True, color_white)
            option_1_display= smallfont.render(option_1 , True, color_white)
            option_2_display= smallfont.render(option_2 , True, color_white)
            option_3_display= smallfont.render(option_3 , True, color_white)
            option_4_display= smallfont.render(option_4 , True, color_white)

            #optimize
            if question_answered == True:
                if answer == option_1:
                    option_1_display= smallfont.render(option_1 , True, color_red) 
                elif answer == option_2:
                    option_2_display= smallfont.render(option_2 , True, color_red)
                elif answer == option_3:
                    option_3_display= smallfont.render(option_3 , True, color_red) 
                elif answer == option_4:
                    option_4_display= smallfont.render(option_4 , True, color_red) 

                if timed_out == True:
                    option_1_display= smallfont.render(option_1 , True, color_red)
                    option_2_display= smallfont.render(option_2 , True, color_red)
                    option_3_display= smallfont.render(option_3 , True, color_red)
                    option_4_display= smallfont.render(option_4 , True, color_red)

                if option_1 == right_answer:
                    option_1_display= smallfont.render(option_1 , True, color_green)   
                elif option_2 == right_answer:         
                    option_2_display= smallfont.render(option_2 , True, color_green)       
                elif option_3 == right_answer:    
                    option_3_display= smallfont.render(option_3 , True, color_green)
                elif option_4 == right_answer:       
                    option_4_display= smallfont.render(option_4 , True, color_green) 
            
            if len(question) >38:
                screen.blit(question_display1, (217,292))
                screen.blit(question_display2, (208,337))
            else:
                screen.blit(question_display, (219,370))
            if option_1_visible == True:
                screen.blit(option_1_display, (x1,y1))
            if option_2_visible == True:
                screen.blit(option_2_display, (x2,y2))
            if option_3_visible == True:
                screen.blit(option_3_display, (x3,y3))
            if option_4_visible == True:
                screen.blit(option_4_display, (x4,y4))

            #next button
            
            if x5 <= mouse[0] <= x5+140 and y5 <= mouse[1] <= y5+40:
                pygame.draw.rect(screen,'purple',[x5,y5,140,40])   
            else:
                pygame.draw.rect(screen,'pink',[x5,y5,140,40])

            screen.blit(next_text , (x5+40,y5+10))

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

    global mod_50_used
    mod_50_used = False
    for question_no in range(1,total_questions+1):
        if game_over != True:
            question_screen()
            if question_list != None:
                    fname2 = question_list[-1]
                    saved_text = open(fname2, 'a')
                    saved_text.write('\n'+answer)
                    saved_text.close()
    ##########################################################################


    #--------------------------GAME OVER-----------------------------------

    '''Add a score board after this screen
    You only see this screen if you lost all lives'''

    def game_over_screen():
        #title
        pygame.display.set_caption("aenigma: Game Over")

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
                    end_theme.stop()
                    done = True

            #vsync
            mainclock.tick(60)   
            pygame.display.flip()
            pygame.display.update()


    if game_over == True:
        game_over_screen()

    ###########################################################################

    #--------------------------Choice Score----------------------------------

    def choice_screen():
        #title
        pygame.display.set_caption("aenigma: Choices")

        #music
        end_theme = pygame.mixer.Sound('music/theme/matrix_theme.mp3')
        end_theme.play(-1)

        #background
        pbackground = pygame.image.load("images\choices.jpg").convert()
        pbackground_position = [0,0]
        screen.blit(pbackground,pbackground_position)

        global choice_percentage,ques_ans
        page = 1

        #file
        def value_finder(fname3):
            global question,answer
            saved_text = open(fname3, 'r')
            choices_list = []
            for line in saved_text:
                choices_list.append(line.strip())
            saved_text.close()

            #count
            question = choices_list[0]
            #slicing
            if len(question) > 35:
                question = question[:35] + '...'
            option_1 = choices_list[1]
            option_2 = choices_list[2]
            option_3 = choices_list[3]
            option_4 = choices_list[4]

            #lines 1-4 have answers, so we subtract 1
            option_1_count = choices_list.count(option_1) - 1
            option_2_count = choices_list.count(option_2) - 1
            option_3_count = choices_list.count(option_3) - 1
            option_4_count = choices_list.count(option_4) - 1
            answer = choices_list[-1]

            #line 5 also has right_answer, so - 1
            if answer == option_1:
                answer_count = option_1_count - 1
            elif answer == option_2:
                answer_count = option_2_count - 1
            elif answer == option_3:
                answer_count = option_3_count - 1
            elif answer == option_4:
                answer_count = option_4_count - 1
            
            #find perc
            total_count = option_1_count+ option_2_count+ option_3_count+ option_4_count -1
            global choice_percentage
            choice_percentage = answer_count/total_count*100

        #text blips
        answer_font = pygame.font.SysFont('Raleway',34)
        question_font = pygame.font.SysFont('Raleway',42)
        perc_font = pygame.font.SysFont('Raleway',32)
        def text_blip(choice_percentage):
            global question_text,answer_text,perc_text,question,answer
            question_text = question_font.render(question , True , 'azure3')
            answer_text = answer_font.render(answer , True , 'black')
            choice_percentage = round(choice_percentage)
            perc_str = "Picked by "+str(choice_percentage)+"% of players "
            perc_text = perc_font.render(perc_str , True , 'black')


        #draw bars
        #can optimize with functions
        choice_green = (66,71,40)
        choice_red = (90,15,13)
        xl = 658
        xr= 250; yr= 47
        #first slot
        def first_slot(fname4):
                value_finder(fname4)
                yl =199
                xg= xr*choice_percentage/100 ; yg= yr
                pygame.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pygame.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pygame.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 201])
                screen.blit(answer_text, [110, 171])
                screen.blit(perc_text, [645, 162])
                pygame.display.flip()

        #second slot
        def second_slot(fname4):
                value_finder(fname4)
                yl =292
                xg= xr*choice_percentage/100 ; yg= yr
                pygame.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pygame.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pygame.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 293])
                screen.blit(answer_text, [110, 259])
                screen.blit(perc_text, [645, 255])
                pygame.display.flip()

        #third slot
        def third_slot(fname4):
                value_finder(fname4)
                yl =384
                xg= xr*choice_percentage/100 ; yg= yr
                pygame.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pygame.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pygame.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 385])
                screen.blit(answer_text, [110, 351])
                screen.blit(perc_text, [645, 350])
                pygame.display.flip()

        #in case you lose after 3 fail attempts
        #fourth slot
        def fourth_slot(fname4):
                value_finder(fname4)
                yl =478
                xg= xr*choice_percentage/100 ; yg= yr
                pygame.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pygame.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pygame.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 474])
                screen.blit(answer_text, [110, 442])
                screen.blit(perc_text, [645, 439])
                pygame.display.flip()

        #fifth slot
        def fifth_slot(fname4):
                value_finder(fname4)
                yl =567
                xg= xr*choice_percentage/100 ; yg= yr
                pygame.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pygame.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pygame.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 569])
                screen.blit(answer_text, [110, 534])
                screen.blit(perc_text, [645, 530])
                pygame.display.flip()
        

        continue_text = question_font.render('CLICK TO CONTINUE' , True , 'azure3')
        
        global doing
        doing = False
        choice_screen = True

        while not doing and choice_screen:
            #blit here so that screen refreshes
            
            screen.blit(continue_text, [368, 685])

            #get values from the chosen question for the slot
            def pager(n,x):
                if page == n:
                    if ques_ans >x:
                        first_slot(question_list[x])
                    if ques_ans >x+1:
                        second_slot(question_list[x+1])
                    if ques_ans >x+2:
                        third_slot(question_list[x+2])
                    if ques_ans >x+3:
                        fourth_slot(question_list[x+3])
                    if ques_ans >x+4:
                        fifth_slot(question_list[x+4])
            pager(1,0)
            pager(2,5)
            pager(3,10)
            pager(4,15)
            pager(5,20)
            pager(6,25)
            pager(7,30)
            pager(8,35)
            pager(9,40)
            pager(10,45)


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
                    #click to continue essentially, then scoreboard if last page
                    def stopper(y,z):
                        global doing
                        if page == y and ques_ans < z:
                            end_theme.stop()
                            doing = True
                    stopper(1,6)
                    stopper(2,11)
                    stopper(3,16)
                    stopper(4,21)
                    stopper(5,26)
                    stopper(6,31)
                    stopper(7,36)
                    stopper(8,41)
                    stopper(9,46)
                    stopper(10,51)

                    #so that screen refreshes
                    screen.blit(pbackground,pbackground_position)
                    page+=1
                    

            #vsync
            mainclock.tick(60)   
            pygame.display.flip()
            pygame.display.update()

    
    choice_screen()

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
        pygame.display.set_caption("aenigma: Score Board")

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
                        if x1 <= mouse[0] <= x1+140 and y <= mouse[1] <= y+40:
                            show_score_menu = False
                            show_highscore_menu = False
                            done = True
                            return
                #recent score button
                        if x2 <= mouse[0] <= x2+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = False
                            return
                #highscore button
                        if x3 <= mouse[0] <= x3+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = True
                            return


    while show_score_menu == True or show_highscore_menu == True:
        score_board()

###########################################################################

while True:
    main()