import sys
sys.path.append("..")
from unittest import TestCase
from zombie_invasion.zombie import Zombie
from zombie_invasion.settings import Settings

class TestZombies(TestCase):

    def test_center_zombies(self):

        # Assign
        settings = Settings()
        zombie = Zombie(settings)

        zombie.centerx = 5
        zombie.centery = 5

        #Act
        zombie.CenterZombie()

        # Assert
        self.assertTrue(zombie.center == 600)

    def test_zombies_on_the_screen(self):
        # Assign
        settings = Settings()
        zombie = Zombie(settings)

        # zombie.moving_right = True

        zombie.rect.right = 550
        zombie.screen_rect.right = 500
        settings.fleet_direction = -1

        # Act
        zombie.ZombiesOnTheScreen()

        # Assert
        self.assertTrue(settings.fleet_direction == 1)

