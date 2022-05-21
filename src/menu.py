from settings import *


class Menu:
    
    selected_index = 0
    
    def __init__(
        self,
        menu_items: list[str] = ["First thing", "Second Thing", "Third Thing"],
        font=pg.font.Font("fonts/Roboto-Black.ttf", 20),
    ) -> None:
        self.font = font
        self.menu_items = menu_items
        self.length = len(self.menu_items)
        self.menu_item_images = [self.font.render(menu_item, True, "white") for menu_item in self.menu_items]
        self.menu_item_rects = [image.get_rect(topleft = (50, 250 + 50*i)) for i, image in enumerate(self.menu_item_images)]
        self.selected_image = pg.Surface((150, 40))
        self.selected_image.set_alpha(100)
        self.selected_image_rect = self.selected_image.get_rect(midleft = (self.menu_item_rects[0].midleft[0]-10, self.menu_item_rects[0].midleft[1]))
        
    def add_menu_item(self, menu_item: str):
        self.menu_items.append(menu_item)
        self.length += 1
        self.menu_item_images.append(self.font.render(menu_item, True, "white"))
        self.menu_item_rects.append(self.menu_item_images[-1].get_rect(topleft = (50, self.menu_item_rects[-1].y+50)))

    def draw(self):
        screen.blit(self.selected_image, self.selected_image_rect)
        for i in range(self.length):
            screen.blit(self.menu_item_images[i], self.menu_item_rects[i])

    def handle_event(self, event):
        if event is not None and event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            for i, rect in enumerate(self.menu_item_rects):
                if rect.collidepoint(x, y):
                    Menu.selected_index = i
                    self.selected_image_rect = self.selected_image.get_rect(midleft = (self.menu_item_rects[Menu.selected_index].midleft[0]-10, self.menu_item_rects[Menu.selected_index].midleft[1]))
    def update(self):
        self.draw()
        print(self.selected_index)