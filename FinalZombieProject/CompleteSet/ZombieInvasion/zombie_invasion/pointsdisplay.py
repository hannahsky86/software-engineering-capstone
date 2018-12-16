import pygame.font
from pygame.sprite import Group
import shooter as shootr


class PointsDisplay:
    """Displays points on the screen"""
    # Requirement ID: 4.0.0

    def __init__(self, settings, stats):
        self.screen = settings.screen
        self.screen_rect = settings.screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.text_color = settings.black
        self.font = pygame.font.SysFont(None, 42)
        self.InitScore()
        self.Level()
        self.Shooters()
        self.Bullets()

    def InitScore(self):
        # Requirement ID: 4.0.1
        """Displays the current score"""

        score = self.stats.score
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.display_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def Level(self):
        # Requirement ID: 4.0.2
        """Displays the current level"""

        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.settings.display_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def Bullets(self):
        # Requirement ID: 4.0.3
        """Displays the number of bullets remaining """

        self.bullet_image = self.font.render(str(self.stats.remaining_bullets), True,
                                             self.text_color, self.settings.display_color)

        self.bullet_rect = self.bullet_image.get_rect()
        self.bullet_rect.right = self.score_rect.right
        self.bullet_rect.top = self.score_rect.bottom + 55

    def Shooters(self):
        # Requirement ID: 4.0.4
        """Displays the shooter lives. Display one image per life remaining."""

        self.shooters = Group()
        for number in range(self.stats.lives):
            shooter = shootr.Shooter(self.settings)
            shooter.rect.x = 10 + number * shooter.rect.width
            shooter.rect.y = 10
            self.shooters.add(shooter)

    def Display(self):
        # Requirement ID: 4.0.5
        """Blits image"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.bullet_image, self.bullet_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.shooters.draw(self.screen)
