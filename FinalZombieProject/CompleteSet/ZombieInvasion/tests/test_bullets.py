import sys
sys.path.append("..")
from unittest import TestCase
from zombie_invasion.bullet import Bullet
from zombie_invasion.settings import Settings
from zombie_invasion.shooter import Shooter


class TestBullets(TestCase):

    def test_update(self):

        # Assign
        settings = Settings()
        shooter = Shooter(settings)
        bullet = Bullet(settings, shooter)

        bullet.circle.x = 500
        bullet.circle.y = 500
        shooter.rect.top = 500
        bullet.pos = [500,500]

        #Act
        bullet.update()

        # Assert
        self.assertTrue(bullet.circle.x == 500 and bullet.circle.y == 481)

    def test_bullets_on_the_screen(self):

        # Assign
        settings = Settings()
        shooter = Shooter(settings)
        bullet = Bullet(settings, shooter)

        settings.bullet_color = settings.green
        bullet.circle.x = 500
        bullet.circle.y = 500
        bullet.bullet_size = 20

        # Act
        bullet.Draw()

        # Assert
        self.assertTrue(bullet.bullet_color == (0, 0, 0) and bullet.circle.x == 500 and bullet.circle.y == 500
                        and bullet.bullet_size == 20)

