import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard():

    def __init__(self, ai_settings, screen, status):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.status = status

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.high_text_color = (255, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.font_middle = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 24)
        # 准备当前得分和最高得分图像
        self.prep_score()
        self.prep_highest_score()

        self.prep_level()

        self.prep_ships()

    def prep_score(self):
        """将得分转换为一副渲染图像"""
        rounded_score = int(round(self.status.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.status.highest_score, -1))
        high_score_str = "Highest: " + "{:,}".format(high_score)
        self.highest_score_iamge = self.font_middle.render(high_score_str, True, self.high_text_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.highest_score_iamge.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font_small.render("Level: " + str(self.status.level), True, self.text_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.status.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示当前得分和最高得分"""
        # 绘制飞船
        self.ships.draw(self.screen)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_iamge, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
