
class Settings():
    """ A class to store all settings for NRA Aline Inversion"""

    def __init__(self):
        """ Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (130,220,230)

#       Ship setting
        self.ship_speed_factor = 1.5

#        Bullet setting
        self.bullet_speed_factor =1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5


