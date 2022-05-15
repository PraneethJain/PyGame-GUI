import sys
from button import *


def handle_events(events: list) -> None:
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

button = Button("Play")
while True:
    handle_events(pg.event.get())

    screen.fill("darkblue")
    button.update()
    pg.display.flip()
