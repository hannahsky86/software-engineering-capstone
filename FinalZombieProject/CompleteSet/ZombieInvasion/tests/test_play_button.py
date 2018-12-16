import sys
sys.path.append("..")
from unittest import TestCase
import pygame.font
from zombie_invasion.settings import Settings
from zombie_invasion.playbutton import PlayButton

class TestPlayButton(TestCase):

    def test_init_play_display(self):
        # Requirement ID: 3.0.1

        # Assign
        pygame.init()
        settings = Settings()
        playbutton = PlayButton(settings)
        msg = "test play button"

        # Act
        playbutton.PlayDisplay(settings, msg)

        # Assert
        self.assertTrue(playbutton.settings.msg == "Play")
