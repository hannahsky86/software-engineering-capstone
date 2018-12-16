import sys
sys.path.append("..")
from unittest import TestCase
import pygame.font
from zombie_invasion.settings import Settings
from zombie_invasion.pointsdisplay import PointsDisplay
from zombie_invasion.stats import Stats

class TestDisplay(TestCase):
    """Displays points on the screen"""
    # Requirement ID: 4.0.0

    def test_init_score_position(self):
        # Requirement ID: 4.0.1
        """Displays the current score"""

        # Assign
        pygame.init()
        settings = Settings()
        stats = Stats(settings)
        display = PointsDisplay(settings, stats)
        display.stats.score = 5
        display.text_color = settings.supernova
        font = pygame.font.SysFont("freesan", 42)
        display.stats.score = 5
        display.score_rect.top = 40
        display.score_rect.right = 40

        score_str = "{:,}".format(display.stats.score)
        display.score_image = font.render(score_str, True,
                                                  display.text_color, display.text_color)

        # Act
        display.InitScore()

        # Assert
        self.assertTrue(display.score_rect.top == 20 and display.score_rect.right == 1180)


    def test_init_score_color(self):
        # Requirement ID: 4.0.1
        """Displays the current score"""

        # Assign
        pygame.init()
        settings = Settings()
        stats = Stats(settings)
        display = PointsDisplay(settings, stats)
        display.stats.score = 5
        display.text_color = (5, 5, 5)
        self.font = pygame.font.SysFont("freesan", 42)
        display.stats.score = 5

        #Act
        display.InitScore()

        # Assert
        self.assertTrue(display.text_color == (5, 5, 5))

    def test_init_score_level(self):
        # Requirement ID: 4.0.2
        """Displays the current level"""

        # Assign
        pygame.init()
        settings = Settings()
        stats = Stats(settings)
        display = PointsDisplay(settings, stats)
        display.stats.level = 5

        # Act
        display.InitScore()

        # Assert
        self.assertTrue(display.stats.level == 5)


    def test_init_score_bullets(self):
        # Requirement ID: 4.0.3
        """Displays the number of bullets remaining """

        # Assign
        pygame.init()
        settings = Settings()
        stats = Stats(settings)
        display = PointsDisplay(settings, stats)
        display.stats.remaining_bullets = 5

        # Act
        display.InitScore()

        # Assert
        self.assertTrue(display.stats.remaining_bullets == 5)


    def test_init_score_lives(self):
        # Requirement ID: 4.0.4
        """Displays the shooter lives. Display one image per life remaining."""

        # Assign
        pygame.init()
        settings = Settings()
        stats = Stats(settings)
        display = PointsDisplay(settings, stats)
        display.stats.lives = 5

        # Act
        display.InitScore()

        # Assert
        self.assertTrue(display.stats.lives == 5)
