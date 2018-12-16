import pygame.font
from unittest import TestCase

from zombie_invasion import shooter as sho, bullet as bul, \
    stats as stat, settings as set, methods
import pygame


class TestMethods(TestCase):

    def test_shoot_mega_bullets(self):

        # Assign
        settings = set.Settings()
        shooter = sho.Shooter(settings)
        stats = stat.Stats(settings)
        bullets = pygame.sprite.Group()

        settings.IsMegaBullet = True
        stats.shot_bullets = 4
        settings.number_of_mega_bullets = 5
        stats.level = 3

        # Act
        methods.ShootMegaBullets(stats, settings, shooter, bullets)

        # Assert
        self.assertTrue(len(bullets) == 1 and stats.remaining_bullets == 1 and stats.shot_bullets == 5)
    #
    def test_shoot_bullets(self):

        # Assign
        settings = set.Settings()
        shooter = sho.Shooter(settings)
        bullets = pygame.sprite.Group()
        bullets.bullet_size = 10
        bullets.bullet_color = settings.supernova

        # Act
        methods.ShootBullet(settings, shooter, bullets)

        # Assert
        self.assertTrue(len(bullets) == 1)

    def test_remove_bullets(self):
        # Assign
        settings = set.Settings()
        shooter = sho.Shooter(settings)
        bullets = pygame.sprite.Group()
        bullet1 = bul.Bullet(settings,shooter)
        bullet2 = bul.Bullet(settings, shooter)
        bullet3 = bul.Bullet(settings, shooter)

        bullets.add(bullet1)
        bullets.add(bullet2)
        bullets.add(bullet3)
        bullet1.rect = bullet1.circle
        bullet1.rect.bottom = -1

        # Act
        methods.RemoveBullets(bullets)

        # Assert
        self.assertTrue(len(bullets) == 2)

    def test_increment_score(self):

        # Assign
        settings = set.Settings()
        shooter = sho.Shooter(settings)
        stats = stat.Stats(settings)
        bullet1 = bul.Bullet(settings,shooter)
        bang = True

        crashed = {}
        crashed[bullet1] = bang

        # Act
        methods.IncrementScore(crashed, stats, None)

        # Assert
        self.assertTrue(stats.score == 1)


    def test_initialize_bullet_settings(self):

        # Assign
        settings = set.Settings()
        shooter = sho.Shooter(settings)
        bullet = bul.Bullet(settings, shooter)
        bullet.bullet_size = 10
        bullet.bullet_color = settings.supernova
        stats = stat.Stats(settings)
        stats.level = 0

        # Act
        methods.InitializeBulletSettings(stats, settings)

        # Assert
        self.assertTrue(settings.bullet_color== (255, 140, 0) and settings.bullet_size == 15)

