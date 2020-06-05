import urwid
from entities.Player import Player
from entities.Entity import Entity
from config import Config
import os


class Game:
    def __init__(self):
        super().__init__()

        self.background = urwid.AttrMap(urwid.SolidFill(' '), 'bg')
        self.player = Player(Config.ARENA_WIDTH, Config.ARENA_HEIGHT)
        self.entities = [
            Entity(Config.ARENA_WIDTH, Config.ARENA_HEIGHT)
            for _ in range(Config.ENEMIES)]

        self.loop = urwid.MainLoop(self.__get_screen(),
                                   palette=Config.PALLETE,
                                   unhandled_input=self.handle_input)

    def __get_screen(self):
        arena = urwid.AttrMap(urwid.SolidFill(' '), 'arena')
        arena = self.player.render(arena)
        for e in self.entities:
            arena = e.render(arena)
        return urwid.Overlay(arena, self.background, 'center', Config.ARENA_WIDTH, 'middle', Config.ARENA_HEIGHT)

    def refresh(self):
        for e in self.entities:
            e.update()
        self.loop.widget = self.__get_screen()

    def start(self):
        self.loop.run()

    def handle_input(self, key):
        if key in ('q', 'Q', 'esc'):
            raise urwid.ExitMainLoop()
        if key in ('w', 'W', 'up'):
            self.player.move("up")
            self.refresh()
        if key in ('s', 'S', 'down'):
            self.player.move("down")
            self.refresh()
        if key in ('a', 'A', 'left'):
            self.player.move("left")
            self.refresh()
        if key in ('d', 'D', 'right'):
            self.player.move("right")
            self.refresh()


if __name__ == "__main__":
    g = Game()
    g.start()
    os.system('clear')
