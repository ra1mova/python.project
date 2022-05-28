import pygame, control
from gun import Gun
from pygame.sprite import Group
from alien import Alien
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((650, 700))
    pygame.display.set_caption("космические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    control.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)
    while True:
        control.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            control.update(bg_color, screen, stats, sc, gun, aliens, bullets)
            control.update_bullets(screen, stats, sc, aliens, bullets)
            control.update_aliens(stats, screen, sc, gun, aliens, bullets)


run()