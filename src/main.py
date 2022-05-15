import sys
from settings import *
from button import Button
from link import Link


class Window:
    def __init__(self):
        self.link = Link("Open google", "www.google.com")

    def run(self):
        while True:
            screen.fill((0, 0, 0))
            self.handle_events(pg.event.get())

            self.link.update()

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
