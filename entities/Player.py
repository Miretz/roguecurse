import urwid


class Player:

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    def __init__(self, arena_width, arena_height):
        super().__init__()
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.coords = (1, 1)
        txt = urwid.Text(('player', u"P"), align='center')
        map1 = urwid.AttrMap(txt, 'streak')
        self.fill = urwid.Filler(map1)

    def move(self, direction):
        change = Player.directions.get(direction, (0, 0))
        x = max(1, min(self.arena_width-1, self.coords[0] + change[0]))
        y = max(1, min(self.arena_height-1, self.coords[1] + change[1]))
        self.coords = (x, y)

    def render(self, arena):
        return urwid.Overlay(
            self.fill, arena, 'left', 1, 'top', 1, left=self.coords[0], top=self.coords[1])
