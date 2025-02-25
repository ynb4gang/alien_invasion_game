import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Загружаем изображение
        original_image = pygame.image.load(r"images\UFO.bmp")
        
        # Указываем новые размеры (например, 50x50 пикселей)
        new_width = 100
        new_height = 45
        
        # Масштабируем изображение до новых размеров
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        
        # Получаем прямоугольник для изображения
        self.rect = self.image.get_rect()
        
        # Устанавливаем начальные координаты
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Сохраняем точное положение по горизонтали
        self.x = float(self.rect.x)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x