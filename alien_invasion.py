import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_status import GameStatus
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    status = GameStatus(ai_settings)
    sb = ScoreBoard(ai_settings, screen, status)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, status, sb, play_button, ship, aliens, bullets)
        if status.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, status, sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, status, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, status, sb, ship, aliens, bullets, play_button)


run_game()
