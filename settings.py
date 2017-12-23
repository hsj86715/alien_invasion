class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 外星人设置
        self.fleet_drop_speed = 4
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 👽点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = self.screen_width / 100
        self.bullet_speed_factor = self.screen_height / 50
        self.alien_speed_factor = self.ship_speed_factor / 2
        self.bullets_allowed = 5
        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        if self.ship_speed_factor < self.screen_width / 20:
            self.ship_speed_factor *= self.speedup_scale
        if self.bullet_speed_factor < self.screen_height / 20:
            self.bullet_speed_factor *= self.speedup_scale
        # 子弹无上限，每次升级都增加1限额
        self.bullets_allowed += 1
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.score_scale
        print("\nShip speed:" + str(self.ship_speed_factor))
        print("Bullet speed:" + str(self.bullet_speed_factor))
        print("Bullet limit:" + str(self.bullets_allowed))
        print("Alien speed:" + str(self.alien_speed_factor))
