import pygame.font


class PlayButton:

    """Class for the play button"""
    def __init__(self, settings):
        # Requirement ID: 3.0.0
        """This method initializes the play settings. """

        self.screen = settings.screen
        self.settings = settings
        self.button_color = settings.black
        self.screen_rect = settings.screen.get_rect()
        self.rect = pygame.Rect(0, 0, settings.play_button_width, settings.play_button_height)
        self.rect.center = self.screen_rect.center
        self.PlayDisplay(settings, settings.msg)

    def PlayDisplay(self, settings, msg):
        # Requirement ID: 3.0.1
        """Defines the font, color and box for the play message"""

        self.font = pygame.font.SysFont(None, settings.play_message_font)
        self.msg_image = self.font.render(msg, True, settings.text_color, settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def PlayButton(self):
        # Requirement ID: 3.0.2
        """Play button"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)




