import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船，并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像，并获得其外接矩形
        self.image = pygame.image.load(
            'D:\\程序\\Python3\\learn-python3\\alien_invasion\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一艘新飞船放在屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
