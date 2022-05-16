from settings import *


class InputBox:
    def __init__(
        self,
        center=(WIDTH / 2, HEIGHT / 2),
        width=200,
        height=50,
        text="",
        font=pg.font.Font("fonts/Roboto-Black.ttf", 20),
        inactive_color="lightskyblue3",
        active_color="dodgerblue2",
    ):
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect(center=center)
        self.text = text
        self.font = font
        self.color = self.inactive_color
        self.text_image = self.font.render(text, True, self.color)
        self.text_rect = self.text_image.get_rect(midleft = (self.rect.left+5, self.rect.centery))
        self.active = False
        self.cursor_image = pg.Surface((1,30))
        self.cursor_image.fill((255, 255, 255))
        self.cursor_rect = self.cursor_image.get_rect(center = self.text_rect.midright)

    def handle_event(self, event):
        if any(pg.mouse.get_pressed()):
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.active = not self.active

            else:
                self.active = False

        self.color = self.active_color if self.active else self.inactive_color

        if event.type == pg.KEYDOWN and self.active:
            if event.key == pg.K_RETURN:
                self.text = ""
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

            self.text_image = self.font.render(self.text, True, self.color)
            self.text_rect = self.text_image.get_rect(topleft = self.text_rect.topleft)
            self.cursor_rect = self.cursor_image.get_rect(center = self.text_rect.midright)

    def draw(self):
        screen.blit(self.text_image, self.text_rect.topleft)
        pg.draw.rect(screen, self.color, self.rect, 2)
        if self.active:
            screen.blit(self.cursor_image, self.cursor_rect.topleft)

    def update(self):
        self.draw()
