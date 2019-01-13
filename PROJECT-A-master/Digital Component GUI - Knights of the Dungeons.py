import pygame
import os
#from pygame.locals import *
# import time
import random
import sys
pygame.init()
font = pygame.font.SysFont('Gabriola', 50, False,False) 
font_3 = pygame.font.SysFont('Gabriola', 50, False,True)
font_2 = pygame.font.SysFont('Gabriola', 50, False,True)
font_4 = pygame.font.SysFont('Gabriola', 29, True,True) # line 83
font_5 = pygame.font.SysFont('Gabriola', 35, True,True) # line 84
font_6 = pygame.font.SysFont('Gabriola', 30, True,True)
font_7 = pygame.font.SysFont('Gabriola', 30, False,True)
# these are the fonts that are going to be used throughout the game
dead = pygame.mixer.Sound('dead.wav')
levelup = pygame.mixer.Sound('levelup.wav')
evillaugh = pygame.mixer.Sound('evil.wav')             # the sound effects
dicesound = pygame.mixer.Sound('RATTLE1.wav')
pageflip = pygame.mixer.Sound('pageflip.wav')
music = pygame.mixer.music.load('epicbattle.mp3')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True
# # if put the_desired_sound_variable.play() it will make that sound each time that code runs
main_menu = True
settings_menu = True
main_menu_2 = True
game = True
instruction_window = True
# the boolean value of each screen if it becomes false it will go onto the next screen
smallfont = pygame.font.SysFont("Gabriola", 30)

#colors for the main menu buttons
brown = (155,112,61) #brown
brown_hover = (130,95, 51) #dark brown when hovering
white = (255,255,255) #white color for text in menu

#(menu) button coordinates
x = 350
y = 400
width = 100
height = 60

#main menu
x_play = 325
y_play = 250
x_music = 325
y_music = 300
x_quit = 325
y_quit = 350

buttonWidth = 100
buttonHeight = 40

# buttons
def text_objects(text, font):
    textSurface = smallfont.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, width, height, inactive, active, action = None):
    global main_menu, settings_menu, main_menu_2, game, instruction_window
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(start_menu, brown_hover, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                main_menu = False
            if action == "music":
                global musicPlaying
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if musicPlaying == True:
                        pygame.mixer.music.stop()
                    if musicPlaying == False:
                        pygame.mixer.music.play(-1,0.0)
                    musicPlaying = not musicPlaying
                    mouseClick = pygame.mouse.get_pressed()
            if action == "quit":
                main_menu = False
                main_menu_2 = False
                game = False
                instruction_window = False
    else:
        pygame.draw.rect(start_menu, inactive, (x,y,width,height))

    textSurf, textRect = text_objects(msg, smallfont)
    textRect.center = ((x+(width/2), (y+(height/2))))
    start_menu.blit(textSurf, textRect)

def action():
    button()
#end of buttons

def dice():
	x = random.randint(1,6)
	return x
def roll_the_dice(num):
		return 'You have thrown {} \n'.format(num)
def draw_text(surface, text, size, color, x, y):
    """Draw text to surface

       surface - Pygame surface to draw to
       text    - string text to draw
       size    - font size
       color   - color of text
       x       - x position of text on surface
       y       - y position of text on surface
    """
    text_surf = font_3.render(str(text), True, color)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (x, y) # I use topleft here because that makes sense to me
                               # for English (unless you want it centered).
                               # But you can use any part of the rect to start drawing the text
    surface.blit(text_surf, text_rect)
def draw_text_2(surface, text, size, color, x, y):
    """Draw text to surface

       surface - Pygame surface to draw to
       text    - string text to draw
       size    - font size
       color   - color of text
       x       - x position of text on surface
       y       - y position of text on surface
    """
    text_surf = font_6.render(str(text), True, color)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (x, y) # I use topleft here because that makes sense to me
                               # for English (unless you want it centered).
                               # But you can use any part of the rect to start drawing the text
    surface.blit(text_surf, text_rect)


start_menu = pygame.display.set_mode((800,600))
pygame.display.set_caption('Knights of the Dungeons')
gb_1 = pygame.image.load('background.png')

kicking = 0
while main_menu:
    kicking += 1
    # pygame.time.delay(100)
    button("Play", x_play, y_play, buttonWidth, buttonHeight, brown, brown_hover, "play")
    button("Quit", x_quit, y_quit, buttonWidth, buttonHeight, brown, brown_hover, "quit")
    button("Music", x_music, y_music, buttonWidth, buttonHeight, brown, brown_hover, "music")
    pygame.display.update()
    for event in pygame.event.get():
        if action == "play":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseClick == pygame.MOUSEBUTTONDOWN:
                    main_menu = False
                    pageflip.play()
            mouseClick = pygame.mouse.get_pressed()
            
        if action == "music":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if musicPlaying == True:
                    pygame.mixer.music.stop()
                if musicPlaying == False:
                    pygame.mixer.music.play(-1,0.0)
                musicPlaying = not musicPlaying
                mouseClick = pygame.mouse.get_pressed()

        if action == "quit":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseClick == pygame.MOUSEBUTTONDOWN:
                    main_menu = False
                    settings_menu = False
                    main_menu_2 = False
                    game = False
                    instruction_window = False
            mouseClick = pygame.mouse.get_pressed()
            pygame.quit()
            os._exit(0)

    start_menu.blit(gb_1,(-200,0))
    
    #try:
     #   start_menu.blit(kik[kicking],(400,300))
    #except IndexError:
     #   kicking = 0
      #  start_menu.blit(kik[kicking],(400,300))

    draw_text(start_menu,'Welcome to Knights of the Dungeons',100,(0,0,0),105,55)



start_menu = pygame.display.set_mode((800,600))
pygame.display.set_caption('Knights of the Dungeons')
gb_1 = pygame.image.load('background.png')
num_player = font_4.render('How many players are going to play the game?',100,(0,0,0))
number1_6 = font_4.render('Please, press a number between 2 and 6.',100,(0,0,0))
if_false = font_5.render('Please choose between 2 to 6 players',100,(0,0,0))
def mainmenu2():
    start_menu.blit(gb_1,(-200,0))
    start_menu.blit(num_player,(25,50))
    start_menu.blit(number1_6,(25,100))
    pygame.display.update()
def mainmenu_false():
    start_menu.blit(gb_1,(-200,0))
    start_menu.blit(if_false,(150,300))
    pygame.display.update()
# these two menu's will show depending on the input of the player during main_menu_2
n_player = []
# the amount of players chosen during main_menu_2 will be appended inside this list


while main_menu_2:
    
    mainmenu2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu_2 = False
            main_menu = False 
            instruction_window = False
            game = False
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_0]:
            mainmenu_false()
            pygame.time.delay(1200)
        if keys[pygame.K_1]:
            mainmenu_false()
            pygame.time.delay(1200)
        if keys[pygame.K_2]:
            n_player.append(2)
            main_menu_2 = False
            pageflip.play()
        if keys[pygame.K_3]:
            n_player.append(3)
            pageflip.play()
            main_menu_2 = False          
        if keys[pygame.K_4]:
            n_player.append(4)
            pageflip.play()
            main_menu_2 = False
        if keys[pygame.K_5]:
            n_player.append(5)
            pageflip.play()
            main_menu_2 = False
        if keys[pygame.K_6]:
            n_player.append(6)
            pageflip.play()
            main_menu_2 = False        
        if keys[pygame.K_7]:
            mainmenu_false()
            pygame.time.delay(1200)
        if keys[pygame.K_8]:
            mainmenu_false()
            pygame.time.delay(1200)
        if keys[pygame.K_9]:
            mainmenu_false()
            pygame.time.delay(1200)
        pygame.display.update()    

instruction_window_ = pygame.display.set_mode((800,600))
pygame.display.set_caption('Knights of the Dungeons')
gb_1 = pygame.image.load('background.png')
header = font_5.render('Instructions ',100,(0,0,0))
Instruction_1 = font_7.render('- By pressing the left arrow key you will decrease your health by  10 points.',100,(0,0,0))
Instruction_2 = font_7.render('- By pressing the right arrow key you will increase your health by  10 points.',100,(0,0,0))
Instruction_3 = font_7.render('- By pressing the up arrow key you will increase your damage by  10 points.',100,(0,0,0))
Instruction_4 = font_7.render('- By pressing the down arrow key you will decrease your damage by  10 points.',100,(0,0,0))
Instruction_5 = font_7.render('- By pressing the space key you will move on to the next level.',100,(0,0,0))
Instruction_6 = font_7.render('- By pressing the enter key you will roll a die and pass on your turn to the next player.',100,(0,0,0))
note = font_5.render('Note ',100,(0,0,0))
note_1 = font_7.render('You can only execute the above instructions only before pressing enter.',100,(0,0,0))
note_2 = font_7.render('For safety purposes you have to hold the keys for 2 seconds.',100,(0,0,0))
note_3 = font_7.render('Remember to use the space key after you have defeated the Boss.',100,(0,0,0))
press_enter_2 = font_4.render('Press Enter to continue',100,(0,0,0))

while instruction_window:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu_2 = False
            main_menu = False 
            game = False
            instruction_window = False
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_RETURN]:
            pageflip.play()
            instruction_window = False
    instruction_window_.blit(gb_1,(-200,0))
    instruction_window_.blit(press_enter_2,(525,660))
    instruction_window_.blit(header,(20,10))
    instruction_window_.blit(Instruction_1,(25,50))
    instruction_window_.blit(Instruction_2,(25,100))
    instruction_window_.blit(Instruction_3,(25,150))
    instruction_window_.blit(Instruction_4,(25,200))
    instruction_window_.blit(Instruction_5,(25,250))
    instruction_window_.blit(note,(20,350))
    instruction_window_.blit(note_1,(25,400))
    instruction_window_.blit(note_2,(25,450))
    instruction_window_.blit(note_3,(25,500))

    pygame.display.update()


win =  pygame.display.set_mode((800,600))
pygame.display.set_caption('Knights of the Dungeons')
gb = pygame.image.load('background.png')
font_3= pygame.font.SysFont('Gabriola', 30, False,True)
message_box = font_5.render('Messages:',10,(0,0,0))
player_stat = [[100,10,1,1],[100,10,1,1],[100,10,1,1],[100,10,1,1],[100,10,1,1],[100,10,1,1]]
# player_stat is the stats of all the palyers if you change it, it will be passed onto player_(depending on which player)_ which will be blitted onto the window in line 369 through 401
message = ['Player 1 it is your turn']
# each time we want a message to display we append it in our while game loop and it will be displayed on the screen   
player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   postition: '+str(player_stat[0][3]),10,(0,0,0))
player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   postition: '+str(player_stat[1][3]),10,(0,0,0))
player_3_ = font_6.render('Player 3     '+'Health: ' + str(player_stat[2][0])+'  Damage:  ' + str(player_stat[2][1])+'    Level:  '+str(player_stat[2][2])+'   postition: '+str(player_stat[2][3]),10,(0,0,0))
player_4_ = font_6.render('Player 4     '+'Health: ' + str(player_stat[3][0])+'  Damage:  ' + str(player_stat[3][1])+'    Level:  '+str(player_stat[3][2])+'   postition: '+str(player_stat[3][3]),10,(0,0,0))
player_5_ = font_6.render('Player 5     '+'Health: ' + str(player_stat[4][0])+'  Damage:  ' + str(player_stat[4][1])+'    Level:  '+str(player_stat[4][2])+'   postition: '+str(player_stat[4][3]),10,(0,0,0))
player_6_ = font_6.render('Player 6     '+'Health: ' + str(player_stat[5][0])+'  Damage:  ' + str(player_stat[5][1])+'    Level:  '+str(player_stat[5][2])+'   postition: '+str(player_stat[5][3]),10,(0,0,0))


def change_level(player):
    player_stat[player -1][2] += 1
def change_position(player,change_to):
    player_stat[player -1][3] = change_to
def change_health(player,change_to):
    player_stat[player -1][0] = change_to

def updating_health(player,adding = 0,subtract = 0):
    player_stat[player - 1][0] = player_stat[player -1][0] - subtract
    player_stat[player - 1][0] = player_stat[player -1][0] + adding
def updating_damage(player,adding = 0,subtract = 0):
    player_stat[player - 1][1] = player_stat[player -1][1] - subtract
    player_stat[player - 1][1] = player_stat[player -1][1] + adding
def updating_level(player,adding = 0,subtract = 0):
    player_stat[player - 1][2] = player_stat[player -1][2] - subtract
    player_stat[player - 1][2] = player_stat[player -1][2] + adding
def updating_position(player,adding = 0,subtract = 0):
    player_stat[player - 1][3] = player_stat[player -1][3] - subtract
    player_stat[player - 1][3] = adding

def return_level(player):
    return player_stat[player -1][2]
def return_position(player):
    return player_stat[player - 1][3]
def return_health(player):
    return player_stat[player - 1][0]
def display_turn(player):
    return "Player {} it is your turn, please press enter.".format(player)
# these definition are made to make acesses the player_stats easier

level_1 = [
            'pass','pick a card','pass',10,'pick a card','pick a card',10,'pass','pick a card','pass',10,
            'pick a card','pick a card',10,'pass','pick a card',10,'pass','pick a card','pick a card'
            ]   
level_2 = [
	'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card',
	'pass',10,'Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,
	'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,
	'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,
	'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card',
	'pass',10,'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card',
	'Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'Pick a card',
	]
level_3 = [
    'pass', 'Pick a card','pass',10, 'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,
    'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,
    'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,
    'pass','Pick a card','pass',10,'Pick a card','Pick a card',10,'pass','Pick a card','pass',10,'Pick a card','Pick a card'
	]
# these are the consequences of each tile in each level

player = 0
try:
    max_players = int(n_player[0] + 1)
except IndexError:
    pass
while game:
    
    roll_dice = font_5.render('Dice: ' ,10,(0,0,0))
    run = False
    #pygame.time.delay(0)
    pygame.time.wait(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    rolled_number = [0] 
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_RETURN]:
        dicesound.play()
        num_thrown = dice()
        rolled_number.append(num_thrown)
        roll_dice = font_5.render('Dice: '+str(0+num_thrown),20,(0,0,0))
        run = True 
    
    
    if player % (max_players) == 0:

        player = 1
    else:
        player = (player) % (max_players)
    message.append(display_turn(player))
    if keys[pygame.K_SPACE]:
        levelup.play()
        change_level(player)
        change_position(player,0)
    if keys[pygame.K_UP]:
        updating_damage(player,10)
    if keys[pygame.K_DOWN]:
        updating_damage(player,0,10)
    if keys[pygame.K_LEFT]:
        updating_health(player,0,10)
    if keys[pygame.K_RIGHT]:
        updating_health(player,10)    

        # the heart of the game
    while run:
        
        if return_level(player) == 1: # this statement will be run when player_stat[the number of the player][3](which represents the level) will be one
            try:
                new_position = return_position(player) + int(rolled_number[-1])
                updating_position(player,new_position)
            
                if level_1[return_position(player)]== 15: # the condition when a player lands on a trap if this code is run it will subtract 15 from the totalhealth
                    message.append('Player {}, you landed on a trap.'.format(player))
                    updating_health(player,0,15)
            except IndexError:
                change_position(player,20)
            
            if return_health(player) <= 0:
                dead.play()
                change_health(player,100)
                change_position(player,0)
                message.append('Player {}, you died, you have been set back to the start.'.format(player))
            if return_position(player)>= 20:
                evillaugh.play()
                change_position(player,20)
                message.append('Player {}, you are in the Boss fight.'.format(player))
        
        if return_level(player) == 2:# this statement will be run when player_stat[the number of the player][3](which represents the level) will be two
            try:
                new_position = return_position(player) + int(rolled_number[-1])
                updating_position(player,new_position)
            
                if level_2[return_position(player)]== 15: 
                    message.append('Player {}, you landed on a trap.'.format(player))
                    updating_health(player,0,15)
            except IndexError:
                change_position(player,71)
            
            if return_health(player) <= 0: # this statement will be run if the players health reaches zero its health will be reset to 100 and its position to 0 of the level
                dead.play()
                change_health(player,100)
                change_position(player,0)
                message.append('Player {}, you died, you have been set back to the start.'.format(player))
            if return_position(player)>= 71: # this statement will be run if the players reaches the boss fight wich means reaching the last tile of the level
                evillaugh.play()
                change_position(player,71)
                message.append('Player {}, you are in the Boss fight.'.format(player)) 
        
        if return_level(player) == 3: # this statement will be run when player_stat[the number of the player][3](which represents the level) will be three
            try:
                new_position = return_position(player) + int(rolled_number[-1])
                updating_position(player,new_position)
            
                if level_3[return_position(player)]== 15:
                    message.append('Player {}, you landed on a trap.'.format(player))
                    updating_health(player,0,15)
            except IndexError:
                change_position(player,71)
            
            if return_health(player) <= 0:
                dead.play()
                change_health(player,100)
                change_position(player,0)
                message.append('Player {}, you died, you have been set back to the start.'.format(player))
            if return_position(player)>= 55:
                evillaugh.play()
                change_position(player,55)
                message.append('Player {}, you are in the Boss fight.'.format(player))    
        player += 1    
        break    
    message_display = font_3.render(message[-1],10,(0,0,0))
    win.blit(gb_1,(-200,0))
    win.blit(roll_dice,(700,550))
    win.blit(message_display,(10,550))
    win.blit(message_box,(10,500))
    if int(n_player[0]) ==  2:
        win.blit(player_1_,(10,20))
        win.blit(player_2_,(10,120))
        player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   Position: '+str(player_stat[0][3]),10,(0,0,0))
        player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   Position: '+str(player_stat[1][3]),10,(0,0,0))
    if int(n_player[0]) ==  3:
        win.blit(player_1_,(10,20))
        win.blit(player_2_,(10,120))
        win.blit(player_3_,(10,220))
        player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   Position: '+str(player_stat[0][3]),10,(0,0,0))
        player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   Position: '+str(player_stat[1][3]),10,(0,0,0))
        player_3_ = font_6.render('Player 3     '+'Health: ' + str(player_stat[2][0])+'  Damage:  ' + str(player_stat[2][1])+'    Level:  '+str(player_stat[2][2])+'   Position: '+str(player_stat[2][3]),10,(0,0,0))
    if int(n_player[0]) ==  4:
        win.blit(player_1_,(10,20))
        win.blit(player_2_,(10,120))
        win.blit(player_3_,(10,220))
        win.blit(player_4_,(10,320))
        player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   Position: '+str(player_stat[0][3]),10,(0,0,0))
        player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   Position: '+str(player_stat[1][3]),10,(0,0,0))
        player_3_ = font_6.render('Player 3     '+'Health: ' + str(player_stat[2][0])+'  Damage:  ' + str(player_stat[2][1])+'    Level:  '+str(player_stat[2][2])+'   Position: '+str(player_stat[2][3]),10,(0,0,0))
        player_4_ = font_6.render('Player 4     '+'Health: ' + str(player_stat[3][0])+'  Damage:  ' + str(player_stat[3][1])+'    Level:  '+str(player_stat[3][2])+'   Position: '+str(player_stat[3][3]),10,(0,0,0))
    if int(n_player[0]) ==  5:
        win.blit(player_1_,(10,20))
        win.blit(player_2_,(10,120))
        win.blit(player_3_,(10,220))
        win.blit(player_4_,(10,320))
        win.blit(player_5_,(10,420))
        player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   Position: '+str(player_stat[0][3]),10,(0,0,0))
        player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   Position: '+str(player_stat[1][3]),10,(0,0,0))
        player_3_ = font_6.render('Player 3     '+'Health: ' + str(player_stat[2][0])+'  Damage:  ' + str(player_stat[2][1])+'    Level:  '+str(player_stat[2][2])+'   Position: '+str(player_stat[2][3]),10,(0,0,0))
        player_4_ = font_6.render('Player 4     '+'Health: ' + str(player_stat[3][0])+'  Damage:  ' + str(player_stat[3][1])+'    Level:  '+str(player_stat[3][2])+'   Position: '+str(player_stat[3][3]),10,(0,0,0))
        player_5_ = font_6.render('Player 5     '+'Health: ' + str(player_stat[4][0])+'  Damage:  ' + str(player_stat[4][1])+'    Level:  '+str(player_stat[4][2])+'   Position: '+str(player_stat[4][3]),10,(0,0,0))
    if int(n_player[0]) ==  6:
        win.blit(player_1_,(10,20))
        win.blit(player_2_,(10,120))
        win.blit(player_3_,(10,220))
        win.blit(player_4_,(10,320))
        win.blit(player_5_,(10,420))
        win.blit(player_6_,(10,520))
        player_1_ = font_6.render('Player 1     '+'Health: ' + str(player_stat[0][0])+'  Damage:  ' + str(player_stat[0][1])+'    Level:  '+str(player_stat[0][2])+'   Position: '+str(player_stat[0][3]),10,(0,0,0))
        player_2_ = font_6.render('Player 2     '+'Health: ' + str(player_stat[1][0])+'  Damage:  ' + str(player_stat[1][1])+'    Level:  '+str(player_stat[1][2])+'   Position: '+str(player_stat[1][3]),10,(0,0,0))
        player_3_ = font_6.render('Player 3     '+'Health: ' + str(player_stat[2][0])+'  Damage:  ' + str(player_stat[2][1])+'    Level:  '+str(player_stat[2][2])+'   Position: '+str(player_stat[2][3]),10,(0,0,0))
        player_4_ = font_6.render('Player 4     '+'Health: ' + str(player_stat[3][0])+'  Damage:  ' + str(player_stat[3][1])+'    Level:  '+str(player_stat[3][2])+'   Position: '+str(player_stat[3][3]),10,(0,0,0))
        player_5_ = font_6.render('Player 5     '+'Health: ' + str(player_stat[4][0])+'  Damage:  ' + str(player_stat[4][1])+'    Level:  '+str(player_stat[4][2])+'   Position: '+str(player_stat[4][3]),10,(0,0,0))
        player_6_ = font_6.render('Player 6     '+'Health: ' + str(player_stat[5][0])+'  Damage:  ' + str(player_stat[5][1])+'    Level:  '+str(player_stat[5][2])+'   Position: '+str(player_stat[5][3]),10,(0,0,0))


    
    pygame.display.update()

    # pygame.quit()
    # quit()

# evillaugh: https://www.youtube.com/watch?v=9d3jQ03Ju8U
