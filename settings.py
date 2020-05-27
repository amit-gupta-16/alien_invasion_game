class Settings:
    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (250,240,240)
        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 20
        #Alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

