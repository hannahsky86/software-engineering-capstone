import pygame
from pygame.sprite import Sprite


class Shooter(Sprite):

    def __init__(self, settings):
        """This class controls the shooter"""
        # Requirement ID: 6.0.0

        super(Shooter, self).__init__()
        self.settings = settings
        self.image = settings.shooter_image
        self.rect = self.image.get_rect()
        self.orig_image = self.image
        self.orig_center = self.rect.center

        self.screen = settings.screen
        self.screen_rect = settings.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #checks which direction the sooter is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Requirement ID: 6.0.5
        #checks which angle the shooter is facing
        self.facing_angle = 0.0

    def CenterShooter(self):
        # Requirement ID: 6.0.1
        """This method recenters the shooter. With each new level, the shooter is recentered. """
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom

    def Rotate(self, angle):
        # Requirement ID: 6.0.2
        """This method rotates the shooter image on the screen"""

        self.image = pygame.transform.rotate(self.orig_image, angle)
        self.rect = self.image.get_rect(center=self.orig_center)
        self.facing_angle = angle

    def blitme(self):
        # Requirement ID: 6.0.3
        """This method refreshes the image """

        self.screen.blit(self.image, self.rect)

    def update(self):
        # Requirement ID: 6.0.4
        """Update the shooter location. """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.shooter_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.shooter_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.settings.shooter_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.shooter_speed

        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom  - 20
