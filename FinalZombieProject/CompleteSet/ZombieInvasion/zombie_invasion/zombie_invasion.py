import sys
sys.path.append("..")
import pointsdisplay as points
import playbutton as button
import stats as stat
import shooter as shoot
import methods as functions
import settings as set
import pygame


def StartGame():
    # Requirement ID: 9.0.0
    """This method initializes the game settings. It also starts and ends the game."""

    pygame.init()
    clock = pygame.time.Clock()
    settings = set.Settings()
    pygame.display.set_caption("Zombie Invasion")
    background = settings.short_grass.convert()
    background = pygame.transform.scale(background, (settings.screen_width, settings.screen_height))
    stats = stat.Stats(settings)
    display = points.PointsDisplay(settings, stats)
    shooter = shoot.Shooter(settings)
    zombies = pygame.sprite.Group()
    functions.ZombieCollection(settings, shooter, zombies)
    bullets = pygame.sprite.Group()

    # Game starts when the play button is pushed.
    play = button.PlayButton(settings)

    #Keep playing so long as level is less than or equal to win level
    while stats.level <= settings.number_of_levels:

        functions.EventCheck(bullets, play, display, settings, stats,
                             shooter, zombies)
        if stats.game_active:
            shooter.update()
            functions.UpdateObjects(bullets, display, settings, stats,
                                    shooter, zombies)
            #check for win
            functions.CheckForWin(stats, settings, button, zombies, bullets,
                                  shooter)
        #Update the screen.
        functions.UpdateScreen(background, bullets, play, display, settings,
                               stats, shooter, zombies)
        clock.tick(100)

StartGame()
