import sys
sys.path.append("..")
from unittest import TestCase
from zombie_invasion.shooter import Shooter
from zombie_invasion.settings import Settings

class TestShooter(TestCase):

    def test_center_shooter(self):

        # Assign
        settings = Settings()
        shooter = Shooter(settings)

        shooter.centerx = 5
        shooter.centery = 5

        #Act
        shooter.CenterShooter()

        # Assert
        self.assertTrue(shooter.centerx == 600 and shooter.bottom == 600)

    def test_rotate(self):
        # Assign
        settings = Settings()
        shooter = Shooter(settings)

        rotate = 45

        # Act
        shooter.Rotate(rotate)

        #Assert
        self.assertTrue(shooter.facing_angle == 45)

    def test_shooter_update(self):

        # Assign
        settings = Settings()
        shooter = Shooter(settings)

        shooter.moving_right = True
        shooter.rect.centerx = 550
        shooter.rect.bottom = 500

        # Act
        shooter.update()

        self.assertTrue(shooter.rect.centerx == 615 and shooter.rect.bottom == 580)

