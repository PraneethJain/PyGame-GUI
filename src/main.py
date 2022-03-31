import sys
from button import *


def handle_events(events: list) -> None:
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


while True:
    handle_events(pg.event.get())

    screen.fill("darkblue")

    pg.display.flip()
