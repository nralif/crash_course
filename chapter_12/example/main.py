# 12.1
import sys
import pygame

from settings import Settings
import function as fun
from hero import Hero

def run_game():

    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height)
    )
    pygame.display.set_caption('Blue display')

    hero = Hero(screen)

    while True:
        fun.event_check()
        fun.update_screen(ai_setting,screen,hero)
run_game()

