class Settings:
    # This class of settings for Alien Invasion

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,100,230)

        
        # Ship properties
        self.ship_speed = 5.0

        # Bullet properties
        self.bullet_speed = 2.0
        self.bullet_width = 3.0
        self.bullet_height = 15.0
        self.bullet_color = (60,60,60)