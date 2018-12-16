class Stats:

    def __init__(self, settings):
        """This method initializes the score. """
        # Requirement ID: 7.0.0

        self.settings = settings
        self.ResetScore()
        self.game_active = False
        self.high_score = 0
        self.number_of_mega_bullets = settings.number_of_mega_bullets
        self.shot_bullets = 0
        self.remaining_bullets = settings.number_of_mega_bullets

    def ResetScore(self):
        # Requirement ID: 7.0.1
        """This method resets the score. """

        self.shot_bullets = 0
        self.number_of_mega_bullets = self.settings.number_of_mega_bullets
        self.remaining_bullets = self.settings.number_of_mega_bullets
        self.lives = self.settings.lives
        self.score = 0
        self.level = 1
