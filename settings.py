class Settings:
    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (250,240,240)

        #ship settings
        self.ship_limit = 1

        #bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 20

        #Alien settings
        self.fleet_drop_speed = 20
        self.speedup_scale = 1.5
        self.intialize_dynamic_settings()

    def intialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 2
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
    
