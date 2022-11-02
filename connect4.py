import numpy as np
import sys
from Button import *

pygame.init()

#colors
LIGHT_BLUE=(0,102,255)
LIGHT_WHITE = (170, 170, 170)
DARK_WHITE = (100, 100, 100)
WHITE = (255,255,255)

#Screen
width = 1280
height = 720
res = (width,height)
screen = pygame.display.set_mode(res)

BG = pygame.image.load("Dots.jpeg")
BG = pygame.transform.scale(BG, res)
rules_font = pygame.font.SysFont('freesansbold', 35)
rules_title_font = pygame.font.SysFont('freesansbold',100)
back_option = rules_font.render("Back", True, "white")
back_hover = rules_font.render("Back", True, DARK_WHITE)

#chips ratio to screen
if width > height:
    RADIUS = int(height/15)
else:
    RADIUS = int(width/15)

rows = 6
cols = 7

def single():
    while True:
        screen.fill(LIGHT_BLUE)

        board=board_gen()
        board_gen_gui(screen)

        pygame.display.update()

def multi():
    while True:
        screen.fill("blue")

        board=board_gen()
        board_gen_gui(screen)

        pygame.display.update()

def rules():
    while True:
        for backchoice in pygame.event.get():
            if backchoice.type == pygame.QUIT:
                pygame.quit()

            if backchoice.type == pygame.MOUSEBUTTONDOWN:
                if back_x <= clicker[0] <= back_x + 210 and back_y <= clicker[1] <= back_y + 40:
                    main_menu()

        screen.fill(LIGHT_BLUE)

        rulestext = rules_title_font.render("RULES", True, WHITE, LIGHT_BLUE)

        text1 = rules_font.render(
            "The rules of this game are simple. Players take turns dropping chips into the 6 by 7", True, WHITE,
            LIGHT_BLUE)
        text2 = rules_font.render("grid layout and their goal to winning the game is to get four chips in a row.", True,
                                  WHITE, LIGHT_BLUE)
        text3 = rules_font.render(
            "Players can get four in a row in a variety of patterns: horizontally, vertically, or diagonally.", True,
            WHITE, LIGHT_BLUE)
        text4 = rules_font.render(
            "There is a possibility of a tie occurring in the game if no players get four in a row.", True, WHITE,
            LIGHT_BLUE)

        screen.blit((rulestext), (530, 80))

        screen.blit(text1, (130, 250))
        screen.blit(text2, (180, 280))
        screen.blit(text3, (100, 350))
        screen.blit(text4, (150, 380))

        clicker = pygame.mouse.get_pos()

        back_x = 620
        back_y = 550
        screen.blit(back_option, (back_x, back_y))
        if back_x <= clicker[0] <= back_x + 210 and back_y <= clicker[1] <= back_y + 40:
            screen.blit(back_hover, (back_x, back_y))

        pygame.display.update()
def board_gen_gui(screen):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(screen, "white", (int((c * height/rows) + 1.5*RADIUS), int((r * height/rows) + 1.5*RADIUS)),
                                   RADIUS)

    pygame.display.update()

def board_gen():
    board=np.zeros((rows,cols))
    return board

def main_menu():
    while True:
        for choice in pygame.event.get():
            if choice.type == pygame.QUIT:
                pygame.quit()

            if choice.type == pygame.MOUSEBUTTONDOWN:
                if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (single_y - (button_height / 2)) <= mouse[1] <= (single_y + (button_height / 2)):
                    single()
                elif (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                             and (multi_y - (button_height/2)) <= mouse[1] <= (multi_y + (button_height/2)):
                    multi()
                elif (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                             and (rules_y - (button_height/2)) <= mouse[1] <= (rules_y + (button_height/2)):
                    rules()
                elif (button_x - (quit_width/2)) <= mouse[0] <= (button_x + (quit_width/2)) \
                             and (quit_y - (quit_height/2)) <= mouse[1] <= (quit_y + (quit_height/2)):
                    pygame.quit()

        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        #Button size
        button_width = width/5
        button_height = height/15
        button_x = width/2

        #buttons
        #single player button
        single_y = height/2.7
        single_button = Button(button_x, single_y, button_width, button_height)
        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (single_y - (button_height/2)) <= mouse[1] <= (single_y + (button_height/2)):
            single_button.draw(screen, DARK_WHITE, 0, 10, 'arial', 35, 'white', 'One-Player')
        single_button.draw(screen, "white", 1, 10, 'arial', 35, 'white', 'One-Player')

        #two player button
        multi_y = height / 2.2
        multi_button = Button(button_x, multi_y, button_width, button_height)
        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (multi_y - (button_height/2)) <= mouse[1] <= (multi_y + (button_height/2)):
            multi_button.draw(screen, DARK_WHITE, 0, 10, 'arial', 35, 'white', 'Two-Player')
        multi_button.draw(screen, "white", 1, 10, 'arial', 35, 'white', 'Two-Player')

        #rules button
        rules_y = height/1.85
        rules_button = Button(button_x, rules_y, button_width, button_height)
        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (rules_y - (button_height/2)) <= mouse[1] <= (rules_y + (button_height/2)):
            rules_button.draw(screen, DARK_WHITE, 0, 10, 'arial', 35, 'white', 'Rules')
        rules_button.draw(screen, "white", 1, 10, 'arial', 35, 'white', 'Rules')

        #quit button
        quit_y = height/1.55
        quit_width = width/15
        quit_height = height/18
        quit_button = Button(button_x, quit_y, quit_width, quit_height)
        quit_button.draw(screen, LIGHT_WHITE, 0, 10, 'arial', 35, 'black', 'Quit')
        if (button_x - (quit_width/2)) <= mouse[0] <= (button_x + (quit_width/2)) \
                and (quit_y - (quit_height/2)) <= mouse[1] <= (quit_y + (quit_height/2)):
            quit_button.draw(screen, DARK_WHITE, 0, 10, 'arial', 35, 'white', 'Quit')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main_menu()