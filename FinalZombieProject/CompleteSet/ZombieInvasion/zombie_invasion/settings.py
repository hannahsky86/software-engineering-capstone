import pygame


class Settings():
    """Defines the settings"""

    def __init__(self):

        # Screen dimensions
        self.screen_width = 1200
        self.screen_height = 600
        self.display_color = (230, 230, 230)

        # Requirement ID: 5.0.0
        # The shooter should have four total lives
        self.lives = 3

        # Colors
        self.black = 0, 0, 0
        self.red = 255, 140, 0
        self.fireball = 230, 0, 0
        self.megafireball = 255, 0, 0
        self.supernova = 124, 252, 0
        self.green = (0, 255, 0)
        self.white = 245, 245, 245

        # Bullets
        self.bullet_size = 7
        self.bullet_color = self.black
        self.IsMegaBullet = False
        #  Requirement ID: 5.0.1
        self.number_of_mega_bullets = 5

        # Mega Bullet Settings
        self.mega_bullet_level = (7, 11, 13)
        self.cnt_mega_bullets = (5, 6, 7, 8)
        self.size_of_mega_bullet = (15, 17, 19)

        # Speed Changes
        self.speedup_scale = 1
        self.zombie_size = 1

        self.SetSpeed()

        # Requirement ID: 5.0.2
        # number of levels in the game
        self.number_of_levels = 16

        # Play Button
        self.play_message_font = 52
        self.play_button_width = 500
        self.play_button_height = 100
        self.button_color = self.black
        self.text_color = self.green
        self.msg = "Play"

        # Image imports
        self.shooter_image = pygame.image.load("../images/top-shooter.png")
        self.zombie_image1 = pygame.image.load("../images/zombie_cartoon_5cm_2.png")
        self.zombie_image2 = pygame.image.load("../images/zombie_cartoon_5cm.png")
        self.short_grass = pygame.image.load("../images/background-grass-short.png")

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def SetSpeed(self):
        # Requirement ID: 5.0.3
        """Sets the initial speed settings. """

        self.shooter_speed = 15
        self.bullet_speed = 19
        self.zombie_speed = .7
        self.points = 1
        self.fleet_direction = 1

    def ResizeZombies(self):
        # Requirement ID: 5.0.4
        """This method resizes the zombies and is called with each new level. """

        self.zombie_size *= 0.94
