import numpy as np
import pygame
import sys

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

rows = 6
cols = 7

BG = pygame.image.load("Dots_BG.jpeg")
BG = pygame.transform.scale(BG, res)

#Text
pygame.font.init()
header_font = pygame.font.SysFont('markerfelt', 120)
game_font = pygame.font.SysFont('arial', 35)
rules_font = pygame.font.SysFont('freesansbold', 35)
rules_title_font = pygame.font.SysFont('freesansbold',100)

title = header_font.render('Connect  F  o  u  r', True, "white")
#Button
single_option = game_font.render("Single Player", True, "white")
single_hover = game_font.render("Single Player", True, DARK_WHITE)
multi_option = game_font.render("Multiplayer", True, "white")
multi_hover = game_font.render("Multiplayer", True, DARK_WHITE)
rules_option = game_font.render("Rules", True, "white")
rules_hover = game_font.render("Rules", True, DARK_WHITE)
quit_option = game_font.render('Quit', True, "black")

if width > height:
    RADIUS = int(height/15)
else:
    RADIUS = int(width/15)


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
        screen.fill(LIGHT_BLUE)

        rulestext = rules_title_font.render("RULES",True,WHITE,LIGHT_BLUE)

        text1 = rules_font.render("The rules of this game are simple. Players take turns dropping chips into the 6 by 7",True, WHITE,LIGHT_BLUE)
        text2 = rules_font.render("grid layout and their goal to winning the game is to get four chips in a row.",True, WHITE,LIGHT_BLUE)
        text3 = rules_font.render("Players can get four in a row in a variety of patterns: horizontally, vertically, or diagonally.",True,WHITE,LIGHT_BLUE)
        text4 = rules_font.render("There is a possibility of a tie occurring in the game if no players get four in a row.", True, WHITE, LIGHT_BLUE)

        screen.blit((rulestext),(525,80))

        screen.blit(text1, (150,250))
        screen.blit(text2, (200,280))
        screen.blit(text3, (100,350))
        screen.blit(text4, (150,380))

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
                if single_x <= mouse[0] <= single_x + 210  and single_y <= mouse[1] <= single_y + 40:
                    single()
                elif multi_x <= mouse[0] <= multi_x + 170 and multi_y <= mouse[1] <= multi_y + 40:
                    multi()
                elif rules_x <= mouse[0] <= rules_x + 95 and rules_y <= mouse[1] <= rules_y + 40:
                    rules()
                elif quit_x-10 <= mouse[0] <= quit_x+76 and quit_y <= mouse[1] <= quit_y + 40:
                    pygame.quit()

        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        #if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        #    pygame.draw.rect(screen, LIGHT_WHITE, [width / 2 - 100, height / 2, 140, 40])
        #else:
        #    pygame.draw.rect(screen, DARK_WHITE, [width / 2 - 100, height / 2, 140, 40])

        #Title
        pygame.draw.circle(screen, "red", (692, 80), 58)
        pygame.draw.circle(screen, "yellow", (805, 90), 48)
        pygame.draw.circle(screen, "red", (910, 90), 48)
        pygame.draw.circle(screen, "yellow", (1015, 90), 48)

        screen.blit(title,(220,20))

        #Single button
        single_x = width/2 - 100
        single_y = height/2 - 90
        screen.blit(single_option,(single_x, single_y))
        if single_x <= mouse[0] <= single_x + 210 and single_y <= mouse[1] <= single_y + 40:
            screen.blit(single_hover, (single_x, single_y))

        #Multi button
        multi_x = width/2 - 80
        multi_y = height/2 - 40
        screen.blit(multi_option,(multi_x, multi_y))
        if multi_x <= mouse[0] <= multi_x + 170 and multi_y <= mouse[1] <= multi_y + 40:
            screen.blit(multi_hover, (multi_x, multi_y))

        #Rules Button
        rules_x = width/2 - 40
        rules_y = height/2 + 10
        screen.blit(rules_option, (rules_x, rules_y))
        if rules_x <= mouse[0] <= rules_x + 95 and rules_y <= mouse[1] <= rules_y + 40:
            screen.blit(rules_hover, (rules_x, rules_y))

        #Quit Button
        quit_x = width/2 - 30
        quit_y = height/2 + 70
        pygame.draw.rect(screen, LIGHT_WHITE, [quit_x-10, quit_y, 86, 40])
        if quit_x-10 <= mouse[0] <= quit_x+76 and quit_y <= mouse[1] <= quit_y + 40:
            pygame.draw.rect(screen, DARK_WHITE, [quit_x - 10, quit_y, 86, 40])
        screen.blit(quit_option, (quit_x, quit_y))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main_menu()
