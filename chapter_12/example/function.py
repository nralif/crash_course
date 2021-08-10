import sys
import pygame

def event_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass

def update_screen(ai_setting,screen,hero):
    screen.fill(ai_setting.bg_color)
    hero.blitme()
    pygame.display.flip()


