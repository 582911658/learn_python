import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('第一个python游戏')

    # 创建第一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        # 监视键盘鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
