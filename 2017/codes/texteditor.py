""" Text Editor """
# import curses
from ch07.positional_list import PositionalList

text = """Introduction

Data science projects offer you a promising way to kick-start your analytics career. Not only you get to learn data science by applying, you also get projects to showcase on your CV. Nowadays, recruiters evaluate a candidate’s potential by his/her work, not as much by certificates and resumes. It wouldn’t matter, if you just tell them how much you know, if you have nothing to show them! That’s where most people struggle and miss out!
"""


class TextEditor:
    class _Char:
        __slots__ = '_char'

        def __init__(self, character):
            self._char = character

        def __str__(self):
            return self._char

    __slots__ = '_text'

    def __init__(self):
        self._text = PositionalList()

    def print(self):
        p = self._text.first()
        print(p.element(), end='')
        # print(type(p))
        while True:
            p = self._text.after(p)
            if (p is None):
                break
            print(p.element(), end='')

    def add(self, character):
        # print(self._Char(character))
        # self._text.add_last(self._Char(character))
        self._text.add_last(character)


if __name__ == '__main__':
    cursor = 'ù'
    te = TextEditor()
    for c in text:
        te.add(c)
    te.print()
    te.add(cursor)
    stdscr = curses.initscr()
    c = stdscr.getch()
