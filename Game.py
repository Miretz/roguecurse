import urwid
from entities.Player import Player
from config import Config


class Game:
    def __init__(self):
        super().__init__()

        self.background = urwid.AttrMap(urwid.SolidFill(' '), 'bg')
        self.arena = urwid.AttrMap(urwid.SolidFill(' '), 'arena')
        self.player = Player(
            self.arena, Config.ARENA_WIDTH, Config.ARENA_HEIGHT)
        self.loop = urwid.MainLoop(self.__get_screen(),
                                   palette=Config.PALLETE,
                                   unhandled_input=self.handle_input)

    def __get_screen(self):
        return urwid.Overlay(self.player.render(), self.background, 'center', Config.ARENA_WIDTH, 'middle', Config.ARENA_HEIGHT)

    def refresh(self):
        self.loop.widget = self.__get_screen()

    def start(self):
        self.loop.run()

    def handle_input(self, key):
        if key in ('q', 'Q', 'esc'):
            raise urwid.ExitMainLoop()
        if key in ('w', 'W'):
            self.player.move("up")
            self.refresh()
        if key in ('s', 'S'):
            self.player.move("down")
            self.refresh()
        if key in ('a', 'A'):
            self.player.move("left")
            self.refresh()
        if key in ('d', 'D'):
            self.player.move("right")
            self.refresh()


if __name__ == "__main__":
    g = Game()
    g.start()
