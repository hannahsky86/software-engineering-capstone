import pygame
import math
import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    """This is the bullet class."""

    def __init__(self, settings, shooter):
        # Requirement ID: 1.0.0
        """This method initializes the bullet settings. """

        super(Bullet, self).__init__()
        self.screen = settings.screen
        self.settings = settings
        # self.stats = stats
        self.bullet_size = settings.bullet_size
        self.bullet_color = settings.bullet_color
        self.circle = pygame.draw.circle(self.screen, self.bullet_color, (124, 24), self.bullet_size, self.bullet_size)
        self.circle.top = shooter.rect.top

        pos_x = float(shooter.rect.centerx)
        pos_y = float(shooter.rect.centery)

        self.pos = [pos_x, pos_y]
        self.speed = settings.bullet_speed
        # This determines the direction of the bulllet.
        direction_x = math.cos(math.radians(shooter.facing_angle + 90)) * self.speed
        direction_y = math.sin(math.radians(shooter.facing_angle - 90)) * self.speed

        self.direction = [direction_x, direction_y]

    def update(self):
        # Requirement ID: 1.0.1
        """This method updates the bullets location on the screen."""

        self.pos[0] += self.direction[0]
        self.pos[1] += self.direction[1]
        self.circle.x = self.pos[0]
        self.circle.y = self.pos[1]

    def Draw(self):
        # Requirement ID: 1.0.2
        """This method draws the bullet on the screen"""

        pygame.draw.circle(self.screen, self.bullet_color,
                           (self.circle.x, self.circle.y),
                           self.bullet_size, self.bullet_size)
