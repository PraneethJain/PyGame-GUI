import sys
from settings import *
from button import Button


class Window:
    def __init__(self):
        self.button = Button("Click me")

    def run(self):
        while True:
            screen.fill((0, 128, 128))
            self.handle_events(pg.event.get())
            self.button.update()
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
