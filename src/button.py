from settings import *


class Button:
    def __init__(
        self,
        text: str,
        center: tuple[int, int] = (WIDTH // 2, HEIGHT // 2),
        font: pg.font.Font = pg.font.Font("fonts/Roboto-Black.ttf", 32),
        color="lightgray",
    ) -> None:
        """Initialize a new button

        Args:
            text : Text to show on button.
            center : Coordinates of center of the button. Defaults to center of screen).
            font : Font for the text on the button. Defaults to pg.font.Font("fonts/Roboto-Black.ttf", 32).
            color : Color of the text on the button. Defaults to light gray.
        """
        self.text = text
        self.font = font
        self.image = self.font.render(self.text, True, color)
        self.image_rect = self.image.get_rect(center=center)
        self.selected = f"<{text}>"
        self.selected_surf = self.font.render(self.selected, True, color)
        self.selected_rect_uninflated = self.selected_surf.get_rect(center = center)
        self.selected_rect = self.selected_rect_uninflated.inflate(25, 25)
        self.selected_rect_surf = pg.Surface((self.selected_rect.w, self.selected_rect.h))
        self.selected_rect_surf.set_alpha(100)
        self.rect = self.image.get_rect(center=center).inflate(25, 25)
        self.hovering = False
        self.pressed = False
        self.unpressed = False

    def hover(self) -> None:
        """Handles the mouse hovering over the button"""
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.hovering = True
            self.unpressed = False
            screen.blit(self.selected_rect_surf, self.selected_rect.topleft)
            if any(pg.mouse.get_pressed()):
                self.pressed = True
            else:
                if self.pressed:
                    self.unpressed = True
                self.pressed = False
        else:
            self.hovering = False
            self.pressed = False
            self.unpressed = False

    def draw(self) -> None:
        """Draws the text of the button"""
        if self.hovering:
            screen.blit(self.selected_surf, self.selected_rect_uninflated.topleft)
        else:
            screen.blit(self.image, self.image_rect.topleft)

    def update(self) -> None:
        """Update the button"""
        self.hover()
        self.draw()
