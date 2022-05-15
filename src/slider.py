from settings import *


class Slider:
    def __init__(
        self,
        center=(WIDTH / 2, HEIGHT / 2),
        max=100,
        width=250,
        height=5,
        color=(255, 255, 255),
        filled_color=(0, 128, 128),
    ) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.filled_color = filled_color
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=center)
        self.max = max
        self.value = max
        self.filled_image = pg.Surface(
            (self.value * self.width / self.max, self.height)
        )
        self.filled_image.fill(self.filled_color)
        self.filled_rect = self.filled_image.get_rect(topleft = self.rect.topleft)
        
        self.pressed = False

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.filled_image, self.filled_rect.topleft)
        pg.draw.circle(screen, self.filled_color, (self.rect.left + self.value/self.max*self.width, self.rect.centery), 8)
    
    def update_value(self):
        x, y = pg.mouse.get_pos()
        if any(pg.mouse.get_pressed()):
            if self.rect.collidepoint(x, y):
                self.pressed = True
            if self.pressed:
                self.value = (x-self.rect.left)*self.max/self.width
                if x > self.rect.right:
                    self.value = self.max
                elif x < self.rect.left:
                    self.value = 0
                    
            self.filled_image = pg.Surface((self.value*self.width/self.max, self.height))
            self.filled_image.fill(self.filled_color)
            self.filled_rect = self.filled_image.get_rect(topleft = self.rect.topleft)
        
        else:
            self.pressed = False
    
    def update(self):
        self.update_value()
        self.draw()