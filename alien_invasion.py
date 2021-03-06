import pygame
import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

clock = pygame.time.Clock()


def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion") 
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, stats, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, stats,sb,  ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update() 
            gf.update_bullets(ai_settings,screen,stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, aliens, ship,sb, bullets, screen, stats)   
        gf.update_screen(ai_settings, screen,stats, sb, ship, aliens, bullets, play_button)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        clock.tick(1440)  


run_game()

# availiable_space_x = ai_settings.screen_width -(2*alien_width)
