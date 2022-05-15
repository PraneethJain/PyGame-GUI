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
        show_value=False,
        font=pg.font.Font("fonts/Roboto-Black.ttf", 16),
        font_color=(255, 255, 255),
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
        self.filled_rect = self.filled_image.get_rect(topleft=self.rect.topleft)
        self.pressed = False

        self.show_value = show_value
        if self.show_value:
            self.font = font
            self.font_color = font_color
            self.value_image = self.font.render(f"{self.value}", True, self.font_color)
            self.value_rect = self.value_image.get_rect(
                midleft=(self.rect.right + 20, self.rect.centery)
            )

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.filled_image, self.filled_rect.topleft)
        pg.draw.circle(
            screen,
            self.filled_color,
            (self.rect.left + self.value / self.max * self.width, self.rect.centery),
            8,
        )
        if self.show_value:
            screen.blit(self.value_image, self.value_rect.topleft)

    def update_value(self):
        x, y = pg.mouse.get_pos()
        if any(pg.mouse.get_pressed()):
            if self.rect.collidepoint(x, y):
                self.pressed = True
            if self.pressed:
                self.value = (x - self.rect.left) * self.max / self.width
                if x > self.rect.right:
                    self.value = self.max
                elif x < self.rect.left:
                    self.value = 0

            self.filled_image = pg.Surface(
                (self.value * self.width / self.max, self.height)
            )
            self.filled_image.fill(self.filled_color)
            self.filled_rect = self.filled_image.get_rect(topleft=self.rect.topleft)
            if self.show_value:
                self.value_image = self.font.render(
                    f"{self.value}", True, self.font_color
                )
                self.value_rect = self.value_image.get_rect(
                    midleft=(self.rect.right + 20, self.rect.centery)
                )

        else:
            self.pressed = False

    def update(self):
        self.update_value()
        self.draw()
