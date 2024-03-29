#modules
import pygame as pg
from random import shuffle,randint 
from time import localtime,strftime #for scoreboard
from os import environ #to set window loc

#initializations
environ['SDL_VIDEO_WINDOW_POS'] = '480,125'
pg.init()              
pg.font.init()           
pg.display.init()
pg.mixer.pre_init(44100, -16, 2, 10)

#for timer and vsync
mainclock = pg.time.Clock()

#window creation
size = [1024, 768]

#for borderless option
resize_file = open('text/options/resizable.txt', 'r')
m_resize = int(resize_file.readline().strip())
resize_file.close()

if m_resize == 0:
    screen = pg.display.set_mode(size, pg.NOFRAME)
elif m_resize == 1:
    screen = pg.display.set_mode(size)

#window icon (only visible when hovered over from taskbar)
# make sure icon res is small
image_icon = pg.image.load('images\icon.jpg')
pg.display.set_icon(image_icon)

#options menu saves
global m_fullscreen, m_sound, m_showfps
options_file = open('text\options\options.txt', 'r')
m_fullscreen = int(options_file.readline().strip())
m_sound = int(options_file.readline().strip())
m_showfps = int(options_file.readline().strip())
options_file.close()

if m_fullscreen == 1:
    pg.display.toggle_fullscreen()


#--------------------------------------------------------------------

#we're using the main function to loop the game after the game over screen
def main():

        #something for the future
        #screenshot button, cause why not
        #im1 = pyautogui.screenshot()
        #im1.save('my_screenshot.png')
        #or
        #im2 = pyautogui.screenshot('my_screenshot2.png')
        #will have to find and increment the number to not replace img

        #something else for later
        # pg.mouse.set_cursor(pg.cursors.Cursor)
    

    #since we return back to menu from the score board
        # we need to reinitialize all the values
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
        pg.display.set_caption("aenigma: Menu Screen")

        #player name + profile sub-menu
        global player_name,total_questions,zen_mode, lives
        #options menu vars
        global m_fullscreen, m_sound, m_showfps
        
        player_text = open('text\scoreboard\player_name.txt', 'r')
        player_name = player_text.read(5)
        player_text.close()
        player_name_font = pg.font.Font(None, 32)
        name_rect = pg.Rect(384, 452, 105, 32)
        color_active = pg.Color(170,170,170)
        color_inactive = pg.Color(190,190,190)
        color = color_inactive
        active = False

        done = False
        show_menu = True

        #background
        #.convert() is used to draw the img faster
        mbackground = pg.image.load("images/naissancee4.png").convert()
        mbackground_position = [0,0]
        
        #music
        menu_theme = pg.mixer.Sound('music/theme/Pauline Oliveiros  A Woman Sees How the World Goes with No Eyes.mp3')
        menu_theme.play(-1)            #-1 loops music indefinitely but also lags when you press next
        if m_sound == 1:
            menu_theme.set_volume(1)
            
        #sfx
        menu_rollover = pg.mixer.Sound('music/sfx/menu rollover.mp3')
        menu_click = pg.mixer.Sound('music/sfx/Menu-click.mp3')
        #if when game is started and the mouse happens to be on any button,
        # then it'll throw an error, so we define these here
        sfx_play_1 = True
        sfx_play_2 = True
        sfx_play_3 = True
        sfx_play_4 = True
        sfx_play_5 = True
        sfx_play_6 = True
        sfx_play_7 = True

        #if i use functions to load images, it'll only make the the loading slower
        #menu selectables
        #when not hovered over
        m_play = pg.image.load("images/menu_play.png").convert()
        m_zen = pg.image.load("images/menu_zen.png").convert()
        m_options = pg.image.load("images/menu_options.png").convert()
        m_help = pg.image.load("images/menu_help.png").convert()
        m_profile = pg.image.load("images/menu_profile.png").convert()
        m_category = pg.image.load("images/menu_category.png").convert()
        m_exit = pg.image.load("images/menu_exit.png").convert()

        #when hovered over
        m_play_w = pg.image.load("images/menu_play_w.png").convert()
        m_zen_w = pg.image.load("images/menu_zen_w.png").convert()
        m_options_w = pg.image.load("images/menu_options_w.png").convert()
        m_help_w = pg.image.load("images/menu_help_w.png").convert()
        m_profile_w = pg.image.load("images/menu_profile_w.png").convert()
        m_category_w = pg.image.load("images/menu_category_w.png").convert()
        m_exit_w = pg.image.load("images/menu_exit_w.png").convert()     

        #category buttons
        music_select = pg.image.load("images/category_buttons/music_selected.png").convert()
        music_unselect = pg.image.load("images/category_buttons/music_unselected.png").convert()
        history_select = pg.image.load("images/category_buttons/history_selected.png").convert()
        history_unselect = pg.image.load("images/category_buttons/history_unselected.png").convert()
        books_select = pg.image.load("images/category_buttons/books_selected.png").convert()
        books_unselect = pg.image.load("images/category_buttons/books_unselected.png").convert()
        image_select = pg.image.load("images/category_buttons/image_selected.png").convert()
        image_unselect = pg.image.load("images/category_buttons/image_unselected.png").convert()
        anime_select = pg.image.load("images/category_buttons/anime_selected.png").convert()
        anime_unselect = pg.image.load("images/category_buttons/anime_unselected.png").convert()
        tv_select = pg.image.load("images/category_buttons/tv_selected.png").convert()
        tv_unselect = pg.image.load("images/category_buttons/tv_unselected.png").convert()
        manga_select = pg.image.load("images/category_buttons/manga_selected.png").convert()
        manga_unselect = pg.image.load("images/category_buttons/manga_unselected.png").convert()
        vidya_select = pg.image.load("images/category_buttons/vidya_selected.png").convert()
        vidya_unselect = pg.image.load("images/category_buttons/vidya_unselected.png").convert()
        art_select = pg.image.load("images/category_buttons/art_selected.png").convert()
        art_unselect = pg.image.load("images/category_buttons/art_unselected.png").convert()
        
        #menu checks/ticks
        check_ticked = pg.image.load("images/check_tick.png").convert()
        check_unticked = pg.image.load("images/check_untick.png").convert()

        #show menus
        show_profile = False
        show_category = False
        show_help = False
        show_options = False
        show_options2 = False
        fullscreen_changed = False

        #top bar
        top_text_font = pg.font.SysFont('Arial', 18)
        top_text_color = (35,35,35)

        global c_music, c_history, c_books, c_image, c_anime, c_tv, c_manga, c_vidya, c_art

        #load category options
        cat_file = open('text/m_category/category_save.txt', 'r')
        c_music = cat_file.readline().strip()
        c_history = cat_file.readline().strip()
        c_books = cat_file.readline().strip()
        c_image = cat_file.readline().strip()
        c_anime = cat_file.readline().strip()
        c_tv = cat_file.readline().strip()
        c_manga = cat_file.readline().strip()
        c_vidya = cat_file.readline().strip()
        c_art = cat_file.readline().strip()
        cat_file.close()
        
        #.readline(1) doesn't work so we use this instead
        #   it reads again after the first char
        #.readlines(1)[1] doesnt work, where [] is line no
        #   list index is out of range
        c_history = c_history[0]
        c_books = c_books[0]
        c_image = c_image[0]
        c_anime = c_anime[0]
        c_tv = c_tv[0]
        c_manga = c_manga[0]
        c_vidya = c_vidya[0]
        c_music = c_music[0]
        c_art = c_art[0]

        #category-save file
        #function so that it can be called when we exit
        #we add the +cat_name so its easier to debug/edit/make changes
        def category_save_file():
            cat_file2 = open('text/m_category/category_save.txt', 'w')
            cat_file2.write(c_music + ' music' + '\n')
            cat_file2.write(c_history + ' history' + '\n')
            cat_file2.write(c_books + ' books' + '\n')
            cat_file2.write(c_image + ' image' + '\n')
            cat_file2.write(c_anime + ' anime' + '\n')
            cat_file2.write(c_tv + ' tv'+ '\n')
            cat_file2.write(c_manga + ' manga' + '\n')
            cat_file2.write(c_vidya + ' vidya' + '\n')
            cat_file2.write(c_art + ' art' + '\n')
            cat_file2.close()

        #menu loop
        while not done and  show_menu:
            
            #we take the mouse pos so that when it is hovered over the desired button
                #it can change colour & play sfx, also to find out whether a specific mouse click
                #is over a button
            mouse = pg.mouse.get_pos()
            x= 90

            #the top text will be changed when the mouse is hovered over a specific button
            top_text_str = 'Welcome to aenigma'
            
            #assign these first since we collidepoint underneath
            #or else background or other blits will overlap
            screen.blit(mbackground,mbackground_position)
            
            #fps init
            if m_showfps == 1:
                fps = mainclock.get_fps()
                fps = round(fps, 2)
                fps_font = pg.font.Font(None, 18)
                fps_text = fps_font.render(str(fps) , True , (0,255,0))
                screen.blit(fps_text,(0,0))
            
            #play
            if x <= mouse[0] <= x+134 and 214 <= mouse[1] <= 214+34:
                m_play_blit = screen.blit(m_play_w ,(x,214))
                top_text_str = 'Start a new game.'
                #play sfx
                if sfx_play_1 == True:
                    if m_sound == 1:
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
                    if m_sound == 1:
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
                    if m_sound == 1:
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
                    if m_sound == 1:
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
                    if m_sound == 1:
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
                    if m_sound == 1:
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
                    if m_sound == 1:
                        menu_rollover.play()
                    sfx_play_7 = False 
            else:
                sfx_play_7 = True
                m_exit_blit = screen.blit(m_exit , (x,605))

            #top text
            top_text = top_text_font.render(top_text_str , True , top_text_color)
            screen.blit(top_text, [94, 66])

            #checkbox render
                #checks with the values loaded from savefile and also checks realtime
            if show_options2:
                    if m_fullscreen == 1:
                        fullscreen_check = screen.blit(check_ticked,(427,305))
                    else: 
                        fullscreen_check = screen.blit(check_unticked,(427,305))
                    if m_sound == 1:
                        sound_check = screen.blit(check_ticked,(427,340))
                    else: 
                        sound_check = screen.blit(check_unticked,(427,340))
                    if m_showfps == 1:
                        fps_check = screen.blit(check_ticked,(427,375))
                    else:
                        fps_check = screen.blit(check_unticked,(427,375))

            #since fullscreen is toggle, we see if the option is changed with fullscreen_changed
                #var, else the game'll need to be restarted
            if fullscreen_changed == True: 
                    pg.display.toggle_fullscreen()
                    fullscreen_changed = False
            
            #category sub items
                #it'll be displayed depending on the save file
            if show_category:
                if c_music == '1':
                    c_music_display = screen.blit(music_select,(310,218))
                else:
                    c_music_display = screen.blit(music_unselect,(310,218))

                if c_history == '1':
                    c_history_display = screen.blit(history_select,(480,218))
                else:
                    c_history_display = screen.blit(history_unselect,(480,218))

                if c_books == '1':
                    c_books_display = screen.blit(books_select,(652,218))
                else:
                    c_books_display = screen.blit(books_unselect,(652,218))

                if c_image == '1':
                    c_image_display = screen.blit(image_select,(310,330))
                else:
                    c_image_display = screen.blit(image_unselect,(310,330))
                
                if c_anime == '1':
                    c_anime_display = screen.blit(anime_select,(480,330))
                else:
                    c_anime_display = screen.blit(anime_unselect,(480,330))
                
                if c_tv == '1':
                    c_tv_display = screen.blit(tv_select,(652,330))
                else:
                    c_tv_display = screen.blit(tv_unselect,(652,330))
                
                if c_manga == '1':
                    c_manga_display = screen.blit(manga_select,(310,434))
                else:
                    c_manga_display = screen.blit(manga_unselect,(310,434))
                
                if c_vidya == '1':
                    c_vidya_display = screen.blit(vidya_select,(480,434))
                else:
                    c_vidya_display = screen.blit(vidya_unselect,(480,434))
                
                if c_art == '1':
                    c_art_display = screen.blit(art_select,(652,434))
                else:
                    c_art_display = screen.blit(art_unselect,(652,434))

            #category sum count
            c_sum = int(c_music) + int(c_history) + int(c_books) + int(c_image) + int(c_anime) + int(c_tv) + int(c_manga) + int(c_vidya) + int(c_art) 

            #exit loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    category_save_file()
                    pg.quit()
                    exit()
                #esc key to exit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        category_save_file()
                        pg.quit()
                        exit()

                    #text box for player name
                    if active == True:
                        if event.key == pg.K_BACKSPACE:
                            player_name = player_name[:-1]
                        elif len(player_name) < 5:
                            player_name += event.unicode
    
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    #player name savefile
                    active = False
                    player_text = open('text\scoreboard\player_name.txt', 'w')
                    player_name = player_name.upper()
                    player_text.write(player_name)
                    player_text.close()
                    #activate textbox
                    if name_rect.collidepoint(event.pos):
                        active = True

                    #category item clicks
                    if show_category:
                        
                        #wrapped fnc which plays sfx and changes whether a category is selected or not
                        def toggle_category_values(category_name):
                            if category_name == '1':
                                category_name = 0
                                if m_sound == 1:
                                    menu_click.play()
                            elif category_name == '0':
                                # so that only 3 max cats selected
                                if c_sum < 3:
                                    category_name = '1'
                                    if m_sound == 1:
                                        menu_click.play()
                                else: 
                                    #menu_click_error.play()
                                    menu_rollover.play()
                            return category_name

                        #music
                        if c_music_display.collidepoint(event.pos):
                            c_music = toggle_category_values(c_music)
                            c_music = str(c_music)
                        #history
                        if c_history_display.collidepoint(event.pos):
                            c_history = toggle_category_values(c_history)
                            c_history = str(c_history)
                        #books
                        if c_books_display.collidepoint(event.pos):
                            c_books = toggle_category_values(c_books)
                            c_books = str(c_books)
                        #image
                        if c_image_display.collidepoint(event.pos):
                            c_image = toggle_category_values(c_image)
                            c_image = str(c_image)
                        #anime
                        if c_anime_display.collidepoint(event.pos):
                            c_anime = toggle_category_values(c_anime)
                            c_anime = str(c_anime)
                        #tv
                        if c_tv_display.collidepoint(event.pos):
                            c_tv = toggle_category_values(c_tv)
                            c_tv = str(c_tv)
                        #manga
                        if c_manga_display.collidepoint(event.pos):
                            c_manga = toggle_category_values(c_manga)
                            c_manga = str(c_manga)
                        #vidya
                        if c_vidya_display.collidepoint(event.pos):
                            c_vidya = toggle_category_values(c_vidya)
                            c_vidya = str(c_vidya)
                        #art
                        if c_art_display.collidepoint(event.pos):
                            c_art = toggle_category_values(c_art)
                            c_art = str(c_art)
                    
                #within options
                    #fullscreen check
                    if show_options2:
                        if fullscreen_check.collidepoint(event.pos):
                            if m_sound == 1:
                                menu_click.play()
                            if m_fullscreen == 0:
                                m_fullscreen = 1
                            elif m_fullscreen == 1:
                                m_fullscreen = 0

                            options_file = open('text\options\options.txt', 'w')
                            options_file.write (str(m_fullscreen) + '\n')
                            options_file.write (str(m_sound) + '\n')
                            options_file.write (str(m_showfps) + '\n')
                            options_file.close()
                            fullscreen_changed = True
                    #fps check
                    if show_options2:
                        if fps_check.collidepoint(event.pos):
                            if m_sound == 1:
                                menu_click.play()
                            if m_showfps == 0:
                                m_showfps = 1
                            elif m_showfps == 1:
                                m_showfps = 0
                    #sound check
                    if show_options2:
                        if sound_check.collidepoint(event.pos):
                            menu_click.play()
                            if m_sound == 0:
                                m_sound = 1
                                menu_theme.set_volume(1)
                            elif m_sound == 1:
                                m_sound = 0
                                menu_theme.set_volume(0)

                            options_file = open('text\options\options.txt', 'w')
                            options_file.write (str(m_fullscreen) + '\n')
                            options_file.write (str(m_sound) + '\n')
                            options_file.write (str(m_showfps) + '\n')
                            options_file.close()
                        

                #close the pop up window
                    if show_profile == True:
                        if (280 <= mouse[0] <= 662 and 390 <= mouse[1] <= 530) == False:
                            mbackground = pg.image.load("images/naissancee4.png").convert()
                            show_profile = False
                        #sound when you close the window
                            #collide point if's makes sure the sound doesn't play when you click on a button
                            if m_sound == 1 and m_play_blit.collidepoint(event.pos) == False and m_zen_blit.collidepoint(event.pos) == False and m_options_blit.collidepoint(event.pos) == False:
                                if m_category_blit.collidepoint(event.pos) == False and m_profile_blit.collidepoint(event.pos) == False and m_help_blit.collidepoint(event.pos) == False:
                                    menu_rollover.play()

                    if show_help == True:
                        if (278 <= mouse[0] <= 885 and 123 <= mouse[1] <= 642) == False:
                            mbackground = pg.image.load("images/naissancee4.png").convert()
                            show_help = False
                            if m_sound == 1 and m_play_blit.collidepoint(event.pos) == False and m_zen_blit.collidepoint(event.pos) == False and m_options_blit.collidepoint(event.pos) == False:
                                if m_category_blit.collidepoint(event.pos) == False and m_profile_blit.collidepoint(event.pos) == False and m_help_blit.collidepoint(event.pos) == False:
                                    menu_rollover.play()

                    if show_options == True:
                        if (286 <= mouse[0] <= 737 and 246 <= mouse[1] <= 414) == False:
                            mbackground = pg.image.load("images/naissancee4.png").convert()
                            show_options = False
                            show_options2 = False
                            if m_sound == 1 and m_play_blit.collidepoint(event.pos) == False and m_zen_blit.collidepoint(event.pos) == False and m_options_blit.collidepoint(event.pos) == False:
                                if m_category_blit.collidepoint(event.pos) == False and m_profile_blit.collidepoint(event.pos) == False and m_help_blit.collidepoint(event.pos) == False:
                                    menu_rollover.play()

                    if show_category == True:
                        if (278 <= mouse[0] <= 885 and 123 <= mouse[1] <= 642) == False:
                            mbackground = pg.image.load("images/naissancee4.png").convert()
                            show_category = False
                            if m_sound == 1 and m_play_blit.collidepoint(event.pos) == False and m_zen_blit.collidepoint(event.pos) == False and m_options_blit.collidepoint(event.pos) == False:
                                if m_category_blit.collidepoint(event.pos) == False and m_profile_blit.collidepoint(event.pos) == False and m_help_blit.collidepoint(event.pos) == False:
                                    menu_rollover.play()

                #play button click
                    if m_play_blit.collidepoint(event.pos):
                        menu_theme.stop()
                        if m_sound == 1:
                            menu_click.play()
                        show_menu = False

                #zen button click
                    if m_zen_blit.collidepoint(event.pos):
                        total_questions = 113
                        zen_mode = True
                        lives = 300
                        menu_theme.stop()
                        if m_sound == 1:
                            menu_click.play()
                        show_menu = False

                #options button click
                    if m_options_blit.collidepoint(event.pos):
                        if m_sound == 1:
                            menu_click.play()
                        mbackground = pg.image.load("images/naissancee4_options.png").convert()
                        show_options = True
                        show_options2 = True

                #help button click
                    if m_help_blit.collidepoint(event.pos):
                        if m_sound == 1:
                            menu_click.play()
                        mbackground = pg.image.load("images/naissancee4_help.png").convert()
                        show_help = True

                #profile button click
                    if m_profile_blit.collidepoint(event.pos):
                        if m_sound == 1:
                            menu_click.play()
                        mbackground = pg.image.load("images/naissancee4_profile.png").convert()
                        show_profile = True

                #category button click
                    if m_category_blit.collidepoint(event.pos):
                        if m_sound == 1:
                            menu_click.play()
                        mbackground = pg.image.load("images/naissancee4_category.png").convert()
                        show_category = True

                #exit button click
                    if m_exit_blit.collidepoint(event.pos):
                        menu_theme.stop()
                        if m_sound == 1:
                            menu_click.play()
                        category_save_file()
                        pg.quit()
                        exit() 
                    
            #player name text box color change
            if show_profile:
                if active:
                    color = color_active
                else:
                    color = color_inactive

                pg.draw.rect(screen, color, name_rect)
                name_surface = player_name_font.render(player_name, True, (35,35,35))
                screen.blit(name_surface, (name_rect.x+5, name_rect.y+5))

            #vsync
            pg.display.flip()
            pg.display.update()
            mainclock.tick(60)
        
        #cateogry save file
        
            #this is when the user leaves all of the category options unselected
            #this method is neither efficient nor random
            # this only picks the default first options

        if c_sum < 3:
            if c_music != '1':
                c_music = '1'
            elif c_history != '1':
                c_history = '1'
            elif c_books != '1':
                c_books = '1'
            c_sum = int(c_music) + int(c_history) + int(c_books) + int(c_image) + int(c_anime) + int(c_tv) + int(c_manga) + int(c_vidya) + int(c_art)
        
        if c_sum < 3:
            if c_image != '1':
                c_image = '1'
            elif c_anime != '1':
                c_anime = '1'
            elif c_tv != '1':
                c_tv = '1'
            c_sum = int(c_music) + int(c_history) + int(c_books) + int(c_image) + int(c_anime) + int(c_tv) + int(c_manga) + int(c_vidya) + int(c_art) 
        
        if c_sum < 3:
            if c_manga != '1':
                c_manga = '1'
            elif c_vidya != '1':
                c_vidya = '1'
            elif c_art != '1':
                c_art = '1'
            c_sum = int(c_music) + int(c_history) + int(c_books) + int(c_image) + int(c_anime) + int(c_tv) + int(c_manga) + int(c_vidya) + int(c_art) 
        
        category_save_file()

    menu_function()
    #----------------------------------------------------------------------------

    #window name
    pg.display.set_caption('aenigma')

    #importing the questions
    def question_import(filename):  

        questions_file = open(filename, "r" , encoding='cp1252')
        #we'll use these outside
        global question,option_1,option_2,option_3,option_4,right_answer,music_ques,image_ques

        # .strip() gets rid of blank space at the end
        # add working dir to music questions
        question = questions_file.readline().strip()  
        option_1 = questions_file.readline().strip() 
        option_2 = questions_file.readline().strip() 
        option_3 = questions_file.readline().strip() 
        option_4 = questions_file.readline().strip() 
        right_answer = questions_file.readline().strip() 
        music_ques = questions_file.readline().strip() 
        image_ques = music_ques
        music_ques = 'music/music_based/' + music_ques
        image_ques = 'images/image_based/' + image_ques

        #shuffling the options
        option_shuffle_list = [option_1, option_2, option_3, option_4]
        shuffle(option_shuffle_list)
        option_1 = option_shuffle_list[0]
        option_2 = option_shuffle_list[1]
        option_3 = option_shuffle_list[2]
        option_4 = option_shuffle_list[3]
        questions_file.close()

    #113 questions in total

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
    
    #image
    l_i = ["text/image_based/q1.txt","text/image_based/q2.txt","text/image_based/q3.txt","text/image_based/q4.txt","text/image_based/q5.txt","text/image_based/q6.txt","text/image_based/q7.txt"
        ,"text/image_based/q8.txt","text/image_based/q9.txt","text/image_based/q10.txt","text/image_based/q11.txt","text/image_based/q12.txt","text/image_based/q13.txt","text/image_based/q14.txt"
        ,"text/image_based/q15.txt"]

    #anime
    l_a = ["text/anime/q1.txt","text/anime/q2.txt","text/anime/q3.txt","text/anime/q4.txt","text/anime/q5.txt","text/anime/q6.txt"]

    #tv
    l_t = ["text/tv/q1.txt","text/tv/q2.txt","text/tv/q3.txt","text/tv/q4.txt","text/tv/q5.txt","text/tv/q6.txt","text/tv/q7.txt"
        ,"text/tv/q8.txt","text/tv/q9.txt","text/tv/q10.txt","text/tv/q11.txt","text/tv/q12.txt"]

    #manga
    l_man =["text/manga/q1.txt","text/manga/q2.txt","text/manga/q3.txt","text/manga/q4.txt","text/manga/q5.txt","text/manga/q6.txt","text/manga/q7.txt"
        ,"text/manga/q8.txt","text/manga/q9.txt","text/manga/q10.txt","text/manga/q11.txt","text/manga/q12.txt","text/manga/q13.txt","text/manga/q14.txt","text/manga/q15.txt"]

    #vidya
    l_v = ["text/vidya/q1.txt","text/vidya/q2.txt","text/vidya/q3.txt","text/vidya/q4.txt","text/vidya/q5.txt","text/vidya/q6.txt","text/vidya/q7.txt"
        ,"text/vidya/q8.txt","text/vidya/q9.txt","text/vidya/q10.txt","text/vidya/q11.txt","text/vidya/q12.txt","text/vidya/q13.txt"]

    #art
    l_art =["text/art/q1.txt","text/art/q2.txt","text/art/q3.txt","text/art/q4.txt","text/art/q5.txt"]

    #shuffle ques
    shuffle(l_h)
    shuffle(l_m)
    shuffle(l_b)
    shuffle(l_i)
    shuffle(l_a)
    shuffle(l_t)
    shuffle(l_man)
    shuffle(l_v)
    shuffle(l_art)
    global question_list
    question_list = []

    #for zen mode, take all questions as a single list 
            #we dont simpley add it all so that category order is shuffled
    l_added = []
    temp_lister = [l_h, l_m ,l_b ,l_i, l_a, l_t, l_man, l_v, l_art]
    shuffle(temp_lister)
    for lis_que in temp_lister:
        l_added += lis_que
    
    #to debug
    #l_added = l_h+ l_m +l_b +l_i+ l_a+ l_t+ l_man+ l_v+ l_art

    global c_history_count, c_music_count, c_books_count, c_image_count, c_anime_count, c_tv_count, c_manga_count, c_vidya_count, c_art_count
    #we only need to display 5 questions per category for normal mode, so we set a counter
    c_history_count = 1
    c_music_count = 1
    c_books_count = 1
    c_image_count = 1
    c_anime_count = 1
    c_tv_count = 1
    c_manga_count = 1
    c_vidya_count = 1
    c_art_count = 1

    def question_selecter():

        global c_history_count, c_music_count, c_books_count, c_image_count, c_anime_count, c_tv_count, c_manga_count, c_vidya_count, c_art_count

        if zen_mode:
            fname = l_added[0]
            question_list.append(fname)
            l_added.pop(0)
            question_import(fname)

        else:
            #when h is selected, we'll display 5 questions from it, then 5 from the next cat
                #then append the fname to a list that will be used later to display choices
                
            if c_history == '1' and c_history_count < 6:
                fname = l_h[0]
                question_list.append(fname)
                l_h.pop(0)
                c_history_count += 1

            elif c_music == '1' and c_music_count < 6:
                    fname = l_m[0]
                    question_list.append(fname)
                    l_m.pop(0)
                    c_music_count += 1

            elif c_books == '1' and c_books_count < 6:
                    fname = l_b[0]
                    question_list.append(fname)
                    l_b.pop(0)
                    c_books_count += 1

            elif c_image == '1' and c_image_count < 6:
                    fname = l_i[0]
                    question_list.append(fname)
                    l_i.pop(0)
                    c_image_count += 1

            elif c_anime == '1' and c_anime_count < 6:
                    fname = l_a[0]
                    question_list.append(fname)
                    l_a.pop(0)
                    c_anime_count += 1

            elif c_tv == '1' and c_tv_count < 6:
                    fname = l_t[0]
                    question_list.append(fname)
                    l_t.pop(0)
                    c_tv_count += 1

            elif c_manga == '1' and c_manga_count < 6:
                    fname = l_man[0]
                    question_list.append(fname)
                    l_man.pop(0)
                    c_manga_count += 1

            elif c_vidya == '1' and c_vidya_count < 6:
                    fname = l_v[0]
                    question_list.append(fname)
                    l_v.pop(0)
                    c_vidya_count += 1

            elif c_art == '1' and c_art_count < 6:
                    fname = l_art[0]
                    question_list.append(fname)
                    l_art.pop(0)
                    c_art_count += 1

            question_import(fname)

    #creating a playlist for background music
    global music_list
    music_list=['music/theme/religious_deathnote.mp3', 'music/theme/lacrimosa.mp3', 'music/theme/Elegy for Rem.mp3', 'music/theme/Takt of Heroes.mp3',  
            'music/theme/ruler of death.mp3', 'music/theme/Heavens Feel.mp3', 'music/theme/tlou No Escape.mp3']

    shuffle(music_list)
    music_name = music_list[0]
    music_list.pop(0)

    pg.mixer.music.load(music_name)
    pg.mixer.music.set_endevent(pg.constants.USEREVENT) #when song ends

    if m_sound == 1:
        pg.mixer.music.play()

    #----------------------------gamu start----------------------------------    
    def question_screen():

        question_selecter()
        #so now we have question,option_1,option_2,option_3,option_4 and right_answer
        global question, music_list
        color = (255,255,255)
        smallfont = pg.font.SysFont('Corbel',35)
        '''color_dark = (100,100,100)
        color_light = (170,170,170)
        text = smallfont.render('quit' , True , color)''' #used for boundary check, get rid of later

        #background
        if len(question) > 38:
            background = pg.image.load("images/hollow_purple_bigger.png").convert()
        else:
            background = pg.image.load("images/hollow_purple.png").convert()
        background_position = [0,0]
        screen.blit(background,background_position)
        #slicing, so it fits the box
        if len(question) > 38:
            question1 = question[:37]
            question2 = question[37:]

        open = True
        #we don't need to define these, but they'll come in use eventually
        # they'll have their day to shine copium
        x1 = 216; x2 = 214; x3 = 595; x4 = 596; x5 = 870
        y1 = 509; y2 = 595; y3 = 505; y4 = 596; y5 = 665
        
        #if music category ques
        #we pause the music temporarily
        if music_ques.endswith('.mp3'):
            pg.mixer.music.pause()
            music_ques_theme = pg.mixer.Sound(music_ques)
            if m_sound == 1:
                music_ques_theme.play()
        else:
            pg.mixer.music.unpause()

        #counters
        global score,lives,game_over,mod_50_used,answer,ques_ans,total_questions,mod_x2_used

        lives_img = pg.image.load("images/heart.png").convert()
        lives_grey_img = pg.image.load("images/heart_grey.png").convert()

        #sfx lose life
        normal_hit= pg.mixer.Sound('music\sfx\Hit Normal Damage.mp3')
        heavy_hit = pg.mixer.Sound('music\sfx\Hit Super Effective.mp3')
        #sfx score up
        score_up = pg.mixer.Sound('music\sfx\sfx_score_up_Level Up!.mp3')
        #sfx first x2 used
        medium_hit= pg.mixer.Sound('music\sfx\HighJumpKick.wav')
        #sfx 50-50 used
        mod_50_used_sfx = pg.mixer.Sound('music/sfx/50-50-BodySlam.mp3')
        #change it to something else later
        mod_x2_used_sfx = pg.mixer.Sound('music/sfx/50-50-BodySlam.mp3')

        #timer
        font_timer = pg.font.SysFont('Raleway', 76)
        frame_count = 0
        frame_rate = 60

        #zen mode infinite time
        start_time = 8

        #progressive difficulty, timer reduces by one second
        if zen_mode == False:
            if question_no < 6:
                start_time = 9
            elif question_no < 11:
                start_time = 8
            elif question_no < 16:
                start_time = 7
            
        #mod images
        mod_50 = pg.image.load("images/50-50.png").convert()
        mod_50_grey = pg.image.load("images/50-50-grey.png ").convert()
        mod_x2 = pg.image.load("images/x2.png").convert()
        mod_x2_grey = pg.image.load("images/x2-grey.png").convert()

        #next
        next_c = (255,255,255)
        nextfont = pg.font.SysFont('Raleway',35)
        
        pg.display.update()

        question_answered = False
        bulk_exec = False
        third = True
        timed_out = False

        answer = ''
        answer2 = ''

        #50-50 functionals
        option_1_visible = True
        option_2_visible = True
        option_3_visible = True
        option_4_visible = True
        mod_temp = True
        mod_50_being_used = False

        #x2 functionals
        mod_x2_being_used = False
        mod_x2_attempts_left = 0

        question_count = 0
        answered_option_1 = False
        answered_option_2 = False
        answered_option_3 = False
        answered_option_4 = False
        
        #mod 50-50 effect
        tv_screen = pg.image.load("images/tv_screen.jpg").convert()
        tv_screen_position = [0,0]
        mod_effect_p1 = pg.image.load("images/mod_effect_p1.png").convert() #mb use later
        mod_effect_p2 = pg.image.load("images/mod_effect_p2.png").convert()

        while open:
            
            mouse = pg.mouse.get_pos()

            #we need to blit something over the screen so that it 
            # gets rid of previous text, hence the background again
            screen.blit(background,background_position)

            #fps init
            if m_showfps == 1:
                fps = mainclock.get_fps()
                fps = round(fps, 2)
                fps_font = pg.font.Font(None, 18)
                fps_text = fps_font.render(str(fps) , True , (0,255,0))
                screen.blit(fps_text,(0,0))

            #counters
            #lives_counter = smallfont.render(str(lives) , True , color)

            #render a greyed out heart instead when you've lost lives
            if lives > 2:
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

            next_text = nextfont.render('NEXT' , True , next_c)

            #displaying image for image based questions
            if image_ques.endswith('.png') or image_ques.endswith('.jpg'):
                image_ques_display = pg.image.load(image_ques).convert()
                screen.blit(image_ques_display,(400,100))
            
            #mods display
            #50-50
            if mod_50_used == False:
                mod_50_blit = screen.blit(mod_50, [967, 27])
            else:
                mod_50_blit = screen.blit(mod_50_grey, [967, 27])
            #x2
            if mod_x2_used == False:
                mod_x2_blit = screen.blit(mod_x2, [967, 77])
            else:
                mod_x2_blit = screen.blit(mod_x2_grey, [967, 77])
            

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                #esc key to exit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:    #can turn this into a pause menu
                        pg.quit()
                        exit()      #if we use quit() istead of exit, we get a fatal error

                #music, next track
                if event.type == pg.constants.USEREVENT:
                    #triggered when song ends
                    if m_sound == 1:
                        if music_list == []:
                            #since we pop the music, we'll recreate the list, shuffle it again and repeat
                            music_list=['music/theme/overlord_dungeon_alt2.mp3', 'music/theme/religious_deathnote.mp3', 'music/theme/lacrimosa.mp3', 'music/theme/Elegy for Rem.mp3', 'music/theme/Takt of Heroes.mp3',  
                                    'music/theme/ruler of death.mp3', 'music/theme/Heavens Feel.mp3', 'music/theme/tlou No Escape.mp3']
                        shuffle(music_list)
                        music_name = music_list[0]
                        music_list.pop(0)
                        pg.mixer.music.load(music_name)
                        pg.mixer.music.play()

                if question_answered == False and question_count <2 :
                    if event.type == pg.MOUSEBUTTONDOWN: 
                    #mod 50-50
                    #& so that it doesnt repeat for the next question
                        if mod_50_used != True:
                            if mod_50_blit.collidepoint(event.pos):
                                mod_50_used = True
                                mod_50_being_used = True 
                                if m_sound == 1:
                                    mod_50_used_sfx.play()
                                #mod effect
                                screen.blit(tv_screen,tv_screen_position)
                                pg.display.update()
                    #mod x2
                        if mod_x2_used != True:
                            if mod_x2_blit.collidepoint(event.pos):
                                mod_x2_used = True
                                mod_x2_being_used = True 
                                mod_x2_attempts_left = 1
                                if m_sound == 1:
                                    mod_x2_used_sfx.play()
                                #mod effect
                                screen.blit(mod_effect_p2,tv_screen_position)
                                pg.display.update()
                                pg.time.delay(60)
                                screen.blit(mod_effect_p1,tv_screen_position)
                                pg.display.update()
                                pg.time.delay(60)
                                screen.blit(mod_effect_p2,tv_screen_position)
                                pg.display.update()
                                pg.time.delay(60)


                    #option1
                        if option_1_visible == True:
                            if answered_option_1 == False:
                                if 172 <= mouse[0] <= 471 and 494 <= mouse[1] <= 543:
                                    answer = option_1
                                    bulk_exec = True
                                    answered_option_1 = True
                                    #so that you can answer again when mod x2 is used
                                    if mod_x2_attempts_left != 0:
                                        question_count = 0
                                    else:
                                        question_answered = True
                    #option2
                        if option_2_visible == True:
                            if answered_option_2 == False:
                                if 170 <= mouse[0] <= 468 and  579<= mouse[1] <= 630:
                                    answer = option_2
                                    bulk_exec = True
                                    answered_option_2 = True
                                    #so that you can answer again when mod x2 is used
                                    if mod_x2_attempts_left != 0:
                                        question_count = 0
                                    else:
                                        question_answered = True
                    #option3
                        if option_3_visible == True:
                            if answered_option_3 == False:
                                if 545 <= mouse[0] <= 844 and 493 <= mouse[1] <= 540:
                                    answer = option_3
                                    bulk_exec = True
                                    answered_option_3 = True
                                    #so that you can answer again when mod x2 is used
                                    if mod_x2_attempts_left != 0:
                                        question_count = 0
                                    else:
                                        question_answered = True
                    #option4
                        if option_4_visible == True:
                            if answered_option_4 == False:
                                if 544 <= mouse[0] <= 842 and 581 <= mouse[1] <= 632:
                                    answer = option_4
                                    bulk_exec = True
                                    answered_option_4 = True
                                    #so that you can answer again when mod x2 is used
                                    if mod_x2_attempts_left != 0:
                                        question_count = 0
                                    else:
                                        question_answered = True
                    
                #next button
                if question_answered == True:
                    if event.type == pg.MOUSEBUTTONDOWN: 
                        if x5 <= mouse[0] <= x5+140 and y5 <= mouse[1] <= y5+40:
                            if lives == 0:
                                    game_over = True
                                    
                            open = False
                            if music_ques.endswith('.mp3'):
                                music_ques_theme.stop()
                            score_up.stop()
                            heavy_hit.stop()
                            normal_hit.stop()                          

            #counters
            if bulk_exec == True:
                if answer == right_answer:
                    question_answered = True
                    question_count += 2
                    mod_x2_attempts_left = 0 # cant use x2 mod to answer again
                    score += 1
                    if m_sound == 1:
                        score_up.play()  
                    #last question
                    if question_no == total_questions:
                        game_over = False

                else:
                    #first time using x2 mod
                    if mod_x2_attempts_left != 1:
                        lives -= 1
                        question_count += 1
                        question_answered = True
                        if lives == 0:
                            if m_sound == 1:
                                heavy_hit.play()
                        else:
                            if m_sound == 1:
                                normal_hit.play()
                        #last question, so that it doesnt show game over screen
                        if question_no == total_questions:
                            game_over = False
                    else:
                        if m_sound == 1:
                            medium_hit.play()
                        answer2 = answer #temp answer so we can blip it red for x2 mod

                if mod_x2_attempts_left != 1:
                    ques_ans += 1

                #cant attempt to answer with x2 anymore
                mod_x2_attempts_left = 0
                bulk_exec = False

            #timer box
            x6= 468; y6 = 12
            timerbox = pg.image.load("images/timerbox.jpg").convert()
            if zen_mode == False:
                screen.blit(timerbox, [x6, y6])

            #timer
                #we count from 0, then subtract it from the timer for a countdown
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
            
            #no timer for zen mode
            if zen_mode == False:
                output_string = str(total_seconds)
            else:
                output_string = ''
            text_timer = font_timer.render(output_string, True, 'white')
            screen.blit(text_timer, [x6+25, y6+15])

            #freeze timer when mods are used
            if question_answered != True and mod_50_being_used == False and mod_x2_being_used == False and zen_mode == False:
                frame_count += 1

            #mod 50-50 display check, mod_temp to make it run once
            if mod_50_used == True and mod_temp == True and mod_50_being_used == True:
                option_list = [option_1,option_2,option_3,option_4]
                shuffle(option_list)
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

            #display red/green when question is answered
            color_white = 'white'
            color_green = 'green'
            color_red = 'red'
            
            #split the question is length is too big
            if len(question) > 38:
                question_display1= smallfont.render(question1 , True, color_white)
                question_display2= smallfont.render(question2 , True, color_white)
            
            #we first render the options in white
            question_display= smallfont.render(question , True, color_white)
            option_1_display= smallfont.render(option_1 , True, color_white)
            option_2_display= smallfont.render(option_2 , True, color_white)
            option_3_display= smallfont.render(option_3 , True, color_white)
            option_4_display= smallfont.render(option_4 , True, color_white)

            #optimize
            if question_answered == True :
                #when you answer, the answer is turned red
                if answer == option_1 :
                    option_1_display= smallfont.render(option_1 , True, color_red)
                elif answer == option_2 :
                    option_2_display= smallfont.render(option_2 , True, color_red)
                elif answer == option_3 :
                    option_3_display= smallfont.render(option_3 , True, color_red)
                elif answer == option_4 :
                    option_4_display= smallfont.render(option_4 , True, color_red)
                
                #if you time out, all options turn red
                if timed_out == True:
                    option_1_display= smallfont.render(option_1 , True, color_red)
                    option_2_display= smallfont.render(option_2 , True, color_red)
                    option_3_display= smallfont.render(option_3 , True, color_red)
                    option_4_display= smallfont.render(option_4 , True, color_red)
                
                #then right answer is turned green
                # so if answer is also right answer, it'll turn green from red
                if option_1 == right_answer:
                    option_1_display= smallfont.render(option_1 , True, color_green)   
                elif option_2 == right_answer:         
                    option_2_display= smallfont.render(option_2 , True, color_green)       
                elif option_3 == right_answer:    
                    option_3_display= smallfont.render(option_3 , True, color_green)
                elif option_4 == right_answer:       
                    option_4_display= smallfont.render(option_4 , True, color_green) 
            
            #we blit the question into the bigger box
            if len(question) >38:
                screen.blit(question_display1, (217,292))
                screen.blit(question_display2, (208,337))
            else:
                screen.blit(question_display, (219,370))            
            
            #answer 2(first selected wrong answer in this case) 
            # will be blipped red if its used with x2 mod
            if answer2 == option_1 and answer2 != right_answer :
                option_1_display= smallfont.render(option_1 , True, color_red)
            elif answer2 == option_2 and answer2 != right_answer :
                option_2_display= smallfont.render(option_2 , True, color_red)
            elif answer2 == option_3 and answer2 != right_answer :
                option_3_display= smallfont.render(option_3 , True, color_red)
            elif answer2 == option_4 and answer2 != right_answer :
                option_4_display= smallfont.render(option_4 , True, color_red)

            #this is to hide 2 options when mod 50-50 is used
            if option_1_visible == True:
                screen.blit(option_1_display, (x1,y1))
            if option_2_visible == True:
                screen.blit(option_2_display, (x2,y2))
            if option_3_visible == True:
                screen.blit(option_3_display, (x3,y3))
            if option_4_visible == True:
                screen.blit(option_4_display, (x4,y4))

            #NEXT button
            #change the color, it looks off
            
            if x5 <= mouse[0] <= x5+140 and y5 <= mouse[1] <= y5+40:
                pg.draw.rect(screen,'purple',[x5,y5,140,40])   
            else:
                pg.draw.rect(screen,'pink',[x5,y5,140,40])

            screen.blit(next_text , (x5+40,y5+10))

            #to test the boundaries of the option boxes when needed
            '''
            if x1 <= mouse[0] <= x1+320 and y1 <= mouse[1] <= y1+40:
                pg.draw.rect(screen,color_light,[x1,y1,320,45])   
            else:
                pg.draw.rect(screen,color_dark,[x1,y1,320,45])
            '''

            pg.display.update()
            pg.display.flip()
            #framerate limiter/vsync
            mainclock.tick(60)
    
    global mod_50_used, mod_x2_used
    mod_50_used = False
    mod_x2_used = False

    for question_no in range(1,total_questions+1):
        if game_over != True:
            if zen_mode:
                #unlimited mods for zen mode
                mod_50_used = False
                mod_x2_used = False
            question_screen()
            if question_list != None:
                    #saving answers in a text time
                    fname2 = question_list[-1]
                    saved_text = open(fname2, 'a')
                    saved_text.write('\n'+answer)
                    saved_text.close()
    ##########################################################################

    #stop music
    pg.mixer.music.stop()

    #--------------------------GAME OVER-----------------------------------

    '''Turn this into a "You lost all your lives, or seems like that's the farthest you'll get" screen
    You only see this screen if you lose all lives'''

    def game_over_screen():
        #title
        pg.display.set_caption("aenigma: Game Over")

        #music
        end_theme = pg.mixer.Sound('music/theme/gameover_kata.mp3')
        if m_sound == 1:
            end_theme.play(-1)

        #background
        background_select = randint(1,2)

        if background_select == 1:
            ebackground = pg.image.load("images\game_over.png").convert()
        else:
            ebackground = pg.image.load("images\game_over2.png").convert()

        ebackground_position = [0,0]
        
        #game over loop
        done = False
        end_screen = True
        
        while not done and end_screen:

            screen.blit(ebackground,ebackground_position)

            #fps init
            if m_showfps == 1:
                fps = mainclock.get_fps()
                fps = round(fps, 2)
                fps_font = pg.font.Font(None, 18)
                fps_text = fps_font.render(str(fps) , True , (0,255,0))
                screen.blit(fps_text,(0,0))
            #exit loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                #esc key to exit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    end_theme.stop()
                    done = True

            #vsync
            mainclock.tick(60)   
            pg.display.flip()
            pg.display.update()

    if game_over == True:
        game_over_screen()

    ###########################################################################

    #--------------------------Choice Score----------------------------------

    def choice_screen():
        #title
        pg.display.set_caption("aenigma: Choices")

        #music
        end_theme = pg.mixer.Sound('music/theme/matrix_theme.mp3')
        if m_sound == 1:
            end_theme.play(-1)

        #background
        pbackground = pg.image.load("images\choices.jpg").convert()
        pbackground_position = [0,0]
        screen.blit(pbackground,pbackground_position) #stop here

        global choice_percentage,ques_ans
        page = 1

        #we get the answers and options from the file which has been added into a separate list
        # then count the occurance of the option selected, not the right answer picked by everyone
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
            if len(question) > 32:
                question = question[:32] + '...'
            option_1 = choices_list[1]
            option_2 = choices_list[2]
            option_3 = choices_list[3]
            option_4 = choices_list[4]
            right_answer = choices_list[5]

            #lines 1-4 have answers, so we subtract 1
            option_1_count = choices_list.count(option_1) - 1
            option_2_count = choices_list.count(option_2) - 1
            option_3_count = choices_list.count(option_3) - 1
            option_4_count = choices_list.count(option_4) - 1
            answer = choices_list[-1]

            #line 5 also has right_answer, so - 1
            if answer == option_1:
                if answer == right_answer:
                    answer_count = option_1_count - 1
                else:
                    answer_count = option_1_count
            elif answer == option_2:
                if answer == right_answer:
                    answer_count = option_2_count - 1
                else:
                    answer_count = option_2_count
            elif answer == option_3:
                if answer == right_answer:
                    answer_count = option_3_count - 1
                else:
                    answer_count = option_3_count
            elif answer == option_4:
                if answer == right_answer:
                    answer_count = option_4_count - 1
                else:
                    answer_count = option_4_count
            
            #find perc
            total_count = option_1_count+ option_2_count+ option_3_count+ option_4_count -1
            global choice_percentage
            choice_percentage = answer_count/total_count*100

        #text blips
        answer_font = pg.font.SysFont('Raleway',34)
        question_font = pg.font.SysFont('Raleway',42)
        perc_font = pg.font.SysFont('Raleway',32)
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
                pg.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pg.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pg.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 201])
                screen.blit(answer_text, [110, 171])
                screen.blit(perc_text, [645, 162])

        #second slot
        def second_slot(fname4):
                value_finder(fname4)
                yl =292
                xg= xr*choice_percentage/100 ; yg= yr
                pg.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pg.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pg.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 293])
                screen.blit(answer_text, [110, 259])
                screen.blit(perc_text, [645, 255])

        #third slot
        def third_slot(fname4):
                value_finder(fname4)
                yl =384
                xg= xr*choice_percentage/100 ; yg= yr
                pg.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pg.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pg.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 385])
                screen.blit(answer_text, [110, 351])
                screen.blit(perc_text, [645, 350])

        #in case you lose after 3 fail attempts
        #fourth slot
        def fourth_slot(fname4):
                value_finder(fname4)
                yl =478
                xg= xr*choice_percentage/100 ; yg= yr
                pg.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pg.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pg.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 474])
                screen.blit(answer_text, [110, 442])
                screen.blit(perc_text, [645, 439])

        #fifth slot
        def fifth_slot(fname4):
                value_finder(fname4)
                yl =567
                xg= xr*choice_percentage/100 ; yg= yr
                pg.draw.rect(screen, choice_red, [xl,yl,xr,yr])
                pg.draw.rect(screen, choice_green ,[xl,yl,xg,yg])
                pg.draw.rect(screen, 'black', [xl,yl,xr,yr], width=2)
                text_blip(choice_percentage)
                screen.blit(question_text, [106, 569])
                screen.blit(answer_text, [110, 534])
                screen.blit(perc_text, [645, 530])
        
        continue_text = question_font.render('CLICK TO CONTINUE' , True , 'azure3')
        
        global doing
        doing = False
        choice_screen = True

        while not doing and choice_screen:
            #blit here so that screen refreshes
            
            screen.blit(pbackground,pbackground_position)

            screen.blit(continue_text, [368, 685])

            #fps init
            if m_showfps == 1:
                fps = mainclock.get_fps()
                fps = round(fps, 2)
                fps_font = pg.font.Font(None, 18)
                fps_text = fps_font.render(str(fps) , True , (0,255,0))
                screen.blit(fps_text,(0,0))

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
            
            #displaying the 23 pages
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
            pager(11,50)
            pager(12,55)
            pager(13,60)
            pager(14,65)
            pager(15,70)
            pager(16,75)
            pager(17,80)
            pager(18,85)
            pager(19,90)
            pager(20,95)
            pager(21,100)
            pager(22,105)
            pager(23,110)

            #exit loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                #esc key to exit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    #click to continue essentially, then scoreboard if last page
                    def stopper(y,z):
                        global doing
                        if page == y and ques_ans < z:
                            end_theme.stop()
                            doing = True
                    
                    #for the 23 pages
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
                    stopper(11,56)
                    stopper(12,61)
                    stopper(13,66)
                    stopper(14,71)
                    stopper(15,76)
                    stopper(16,81)
                    stopper(17,86)
                    stopper(18,91)
                    stopper(19,96)
                    stopper(20,101)
                    stopper(21,106)
                    stopper(22,111)
                    stopper(23,114)

                    #so that it doesnt show bg for the small
                    #split second before it swaps to the score board
                    if doing == False:
                        #use bg so that screen refreshes
                        screen.blit(pbackground,pbackground_position)
                        page+=1
                    

            #vsync
            mainclock.tick(60)   
            pg.display.flip()
            pg.display.update()

    
    choice_screen()

    ###########################################################################

    global show_score_menu,show_highscore_menu, first, second
    show_score_menu = True
    show_highscore_menu = False

    #we only need to save score once, so we make use of 2 temp variables
    first = True
    second = True

    #------------------------------Score Board--------------------------------#
    def score_board():
        
        #based on whether recent/highest is selected, the scoreboard will reblit everything

        #these are only the recent scores
        pink = (255, 192, 203)
        yellow = (255,255,0)

        #quit button
        swamp_green = (2,75,64)
        swamp_ltgreen = (0,66,60)

        smallfont = pg.font.SysFont('Raleway',35)
        quit_text = smallfont.render('QUIT' , True , yellow)

        #menu button
        menu_text = smallfont.render('MENU' , True , yellow)

        #recent button
        time_text = smallfont.render('TIME' , True , yellow)

        #highest button
        score_text = smallfont.render('SCORE' , True , yellow)

        #replace font with the one from hotline miami
        score_font2 = pg.font.SysFont('Arial Rounded MT Bold',60)

        #title
        pg.display.set_caption("aenigma: Score Board")

        #time
        t = localtime()
        current_time = strftime("%H:%M, %d/%m", t)
        
        global first
        while first:
            #storing and taking scores from text file
            score_file_temp = open('text\scoreboard\saved_user_responses_temp.txt','w')
            score_file = open('text\scoreboard\saved_user_responses.txt','r')

            global player_name
        
            #score_saver
            if not zen_mode:
                if score > 9:
                    score_file_temp.write('       '+ str(score)+ '                                ' + current_time + '                     ' +player_name + '\n')
                else: 
                    score_file_temp.write('       '+ '0' + str(score)+ '                                ' + current_time + '                     ' +player_name + '\n')
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
            if not zen_mode:
                score_file = open('text\scoreboard/not_sorted_scores.txt','a')
                if score > 9:
                    score_file.write('       '+ str(score)+ '                                ' + current_time + '                     ' +player_name + '\n')
                else:
                    score_file.write('       '+ '0' + str(score)+ '                                ' + current_time + '                     ' +player_name + '\n')
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

        score_font = pg.font.SysFont('papyrus',40)
        score_font3 = pg.font.SysFont('papyrus',36)

        #sort scores:
        sort_text = score_font3.render( 'Sort by:', True , yellow)

        #idk how to shorten/optimize this, using list didnt work
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
        sbackground = pg.image.load("images\hotline_miami3.jpg").convert()
        sbackground_position = [0,0]

        x=870
        y=710
        x1 = 700
        x2 = 200
        x3 = 370

        done = False
        show_score = True
        

        while not done and  show_score:
            
            screen.blit(sbackground,sbackground_position)

            #display top/recent 7 scores
            screen.blit(score_display_top , (40,58))
            screen.blit(score_display_1 , (40,145))
            screen.blit(score_display_2 , (40,221))
            screen.blit(score_display_3 , (40,294))
            screen.blit(score_display_4 , (40,370))
            screen.blit(score_display_5 , (40,446))
            screen.blit(score_display_6 , (40,519))
            screen.blit(score_display_7 , (40,596))

            #fps init
            if m_showfps == 1:
                fps = mainclock.get_fps()
                fps = round(fps, 2)
                fps_font = pg.font.Font(None, 18)
                fps_text = fps_font.render(str(fps) , True , (0,255,0))
                screen.blit(fps_text,(0,0))
            
            mouse = pg.mouse.get_pos()
            #quit button
            if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                pg.draw.rect(screen,swamp_ltgreen,[x,y,140,40]) 
            else:
                pg.draw.rect(screen,swamp_green,[x,y,140,40])  

            #menu button
            if x1 <= mouse[0] <= x1+140 and y <= mouse[1] <= y+40:
                pg.draw.rect(screen,swamp_ltgreen,[x1,y,140,40]) 
            else:
                pg.draw.rect(screen,swamp_green,[x1,y,140,40])

            #time button
            if x2 <= mouse[0] <= x2+140 and y <= mouse[1] <= y+40:
                pg.draw.rect(screen,swamp_ltgreen,[x2,y,140,40]) 
            else:
                pg.draw.rect(screen,swamp_green,[x2,y,140,40])
            
            #highscore button
            if x3 <= mouse[0] <= x3+140 and y <= mouse[1] <= y+40:
                pg.draw.rect(screen,swamp_ltgreen,[x3,y,140,40]) 
            else:
                pg.draw.rect(screen,swamp_green,[x3,y,140,40])
            
            #blit text over the buttons
            screen.blit(sort_text , (40,700))
            screen.blit(quit_text , (x+40,y+10))
            screen.blit(menu_text , (x1+40,y+10))
            screen.blit(time_text , (x2+40,y+10))
            screen.blit(score_text , (x3+30,y+10))
            
            #vsync
            pg.display.flip()
            mainclock.tick(60)
            pg.display.update()
            
            #exit loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                #esc key to exit
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit()
                #quit button
                if event.type == pg.MOUSEBUTTONDOWN:
                        if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
                            pg.quit()
                            exit()
                #menu button
                        if x1 <= mouse[0] <= x1+140 and y <= mouse[1] <= y+40:
                            show_score_menu = False
                            show_highscore_menu = False
                            done = True
                            score_theme.stop()
                            return
                #recent score button
                        if x2 <= mouse[0] <= x2+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = False
                            return
                #highscore button
                        if x3 <= mouse[0] <= x3+140 and y <= mouse[1] <= y+40:
                            show_highscore_menu = True
                            return

    #music
    global score_theme
    score_theme = pg.mixer.Sound('music/theme/yt1s.com - MOON  Crystals Hotline Miami Soundtrack.mp3')
    if m_sound == 1:
        score_theme.play(-1)
    
    while show_score_menu == True or show_highscore_menu == True:
        score_board()

###########################################################################

while True:
    main()


    
