import sys
from settings import *
from button import Button
from link import Link
from slider import Slider


class Window:
    def __init__(self):
        self.slider = Slider(max=500, color="red", filled_color="blue")

    def run(self):
        while True:
            screen.fill((0, 0, 0))
            self.handle_events(pg.event.get())

            self.slider.update()
            print(self.slider.value)

            pg.display.update()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


def main():
    window = Window()
    window.run()


if __name__ == "__main__":
    main()
