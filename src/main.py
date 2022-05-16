import sys
from settings import *
from button import Button
from link import Link
from slider import Slider
from input_box import InputBox


class Window:
    def __init__(self):
        
        self.input_box = InputBox()
        
        self.r_slider = Slider(
            center=(180, 30),
            max=255,
            color="white",
            filled_color="red",
            show_value=True,
            show_label=True,
            label_text="R",
        )
        self.g_slider = Slider(
            center=(180, 60),
            max=255,
            color="white",
            filled_color="green",
            show_value=True,
            show_label=True,
            label_text="G",
        )
        self.b_slider = Slider(
            center=(180, 90),
            max=255,
            color="white",
            filled_color="blue",
            show_value=True,
            show_label=True,
            label_text="B",
        )
        self.r = 0
        self.g = 0
        self.b = 0

        self.reset_button = Button("Reset", (187, 150))

    def run(self):
        while True:
            screen.fill((self.r, self.g, self.b))
            self.handle_events(pg.event.get())

            self.input_box.update()
            
            pg.draw.rect(screen, "black", pg.Rect(5, 12, 375, 100), border_radius=5)
            pg.draw.rect(
                screen, "white", pg.Rect(5, 12, 375, 100), width=2, border_radius=5
            )

            self.r_slider.update()
            self.g_slider.update()
            self.b_slider.update()

            self.r = self.r_slider.value
            self.g = self.g_slider.value
            self.b = self.b_slider.value

            self.reset_button.update()

            if self.reset_button.unpressed:
                self.r_slider.reset()
                self.g_slider.reset()
                self.b_slider.reset()

            pg.display.update()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            self.input_box.handle_event(event)


def main():
    window = Window()
    window.run()


if __name__ == "__main__":
    main()
