import pygame
from pygame.sprite import Sprite
import random


class Zombie(Sprite):
    """This class creates a template for the zombies"""

    def __init__(self, settings):
        # Requirement ID: 8.0.0
        """This method initializes the settings for the zombies. """

        super(Zombie, self).__init__()
        self.screen = settings.screen
        self.settings = settings

        # Defines the probability of getting a given type of zombie
        rn = random.randint(0,100)
        self.image = settings.zombie_image1
        if rn < 40:
            self.image = settings.zombie_image2
        # Defines the probability of image being flipped
        if rn <= 50:
            self.image =   pygame.transform.flip(self.image, True, False)

        #Resize the image
        self.rect = self.image.get_rect()
        length = int(self.rect.width*.7*settings.zombie_size)
        height = int(self.rect.width*.7*settings.zombie_size)

        self.image = pygame.transform.smoothscale(self.image, (length, height))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

    def CenterZombie(self):
        # Requirement ID: 8.0.1
        """Center the zombies. With each new level the zombies are recentered. """

        self.center = self.screen_rect.centerx

    def ZombiesOnTheScreen(self):
        # Requirement ID: 8.0.2
        """Which direction the zombies are moving. If it hits the end of the screen, change directions"""

        if (self.rect.right) >= self.screen_rect.right:
            self.settings.fleet_direction *= -1

        if (self.rect.left) <= self.screen_rect.left:
            self.settings.fleet_direction *= -1

    def update(self):
        # Requirement ID: 8.0.3
        """Update the zombies on the screen. Create a random walk."""

        rn1 = (random.randint(1,101))
        if rn1 < 70 and self.rect.right < self.screen_rect.right - 10:
            self.rect.y += (rn1*1.000/25.000)

        rn2 = (random.randint(1,101))
        if rn2 <= 50 and self.rect.right < self.screen_rect.right - 10:
            self.rect.x += (rn2 / 90.0000) + 1

        if rn2 > 50 and self.rect.left > self.screen_rect.left + 10:
            self.rect.x -= ((100 - rn2) / 90.0000)

    def blitme(self):
        # Requirement ID: 8.0.4
        """Refresh the screen."""

        self.screen.blit(self.image, self.rect)



