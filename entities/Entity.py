import urwid
import random


class Entity:
    def __init__(self, arena_width, arena_height):
        super().__init__()
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.coords = (random.randint(1, arena_width),
                       random.randint(1, arena_height))
        txt = urwid.Text(('enemy', u"E"), align='center')
        map1 = urwid.AttrMap(txt, 'streak')
        self.fill = urwid.Filler(map1)

    def update(self):
        step = random.choice([-1, 1])
        if random.choice([True, False]):
            self.coords = (self.coords[0], self.coords[1] + step)
        else:
            self.coords = (self.coords[0] + step, self.coords[1])

    def render(self, arena):
        return urwid.Overlay(
            self.fill, arena, 'left', 1, 'top', 1, left=self.coords[0], top=self.coords[1])
