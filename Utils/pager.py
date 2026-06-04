from math import ceil
import curses

from rich import print

from Data.settings import *
from Utils.display import *

class Pager:
    def __init__(self, data, start=0, page_size=None):
        self.data = data[:]
        self.current = start
        self.cursor = 0
        self.page_size = page_size or STD_PAGE_SIZE
        self.page_amount = ceil(len(data) / self.page_size)
        self.pages = []
        self.init_pages()

    def init_pages(self):
        if self.page_amount == 0: return
        elif self.page_amount == 1:
            self.pages.append(self.data)
        else:
            for i in range(self.page_amount):
                start = i * self.page_size
                end = (i+1) * self.page_size
                page = self.data[start:end]
                self.pages.append(page)

    def next_page(self):
        self.current += 1
        if self.current >= self.page_amount:
            self.current = 0

    def back_page(self):
        self.current -= 1
        if self.current < 0:
            self.current = self.page_amount - 1

    def cursor_up(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = len(self.pages[self.current]) - 1

    def cursor_down(self):
        self.cursor += 1
        if self.cursor >= len(self.pages[self.current]):
            self.cursor = 0

    def is_empty(self):
        return self.page_amount == 0

    def display_current(self):
        if self.page_amount == 0:
            stdscr.addstr("No data\n")
            return

        for i in self.pages[self.current]:
            stdscr.addstr(i + "\n")

    def selector_mode(self, ctx, selection_key):
        if self.page_amount == 0:
            stdscr.addstr("No data\n")
            return

        while True:
            stdscr.erase()

            display_title("Selection Mode")

            for idx, i in enumerate(self.pages[self.current]):
                txt = i
                if idx == self.cursor: txt = "-->  " + txt
                stdscr.addstr(txt + "\n")

            page_index = f"{self.current+1}/{self.page_amount}"
            stdscr.addstr(
                    stdscr.getyx()[0],
                    W//2-len(page_index)//2,
                    page_index + "\n"
            )

            line()
            stdscr.addstr("Enter 'w' or 's' to move the cursor\n")
            stdscr.addstr("Enter 'a' or 'd' to move the pages\n")

            options = ["Select", "Back"]
            option_menu(options)

            key = stdscr.getch()
            if key == ord("1") and self.page_amount > 0:
                ctx.dm.add(
                    selection_key,
                    self.pages[self.current][self.cursor])
                break
            if key == ord("2"):
                ctx.sm.go_back()
                break
            if key == ord("a") and self.page_amount > 0:
                self.back_page()
            if key == ord("d") and self.page_amount > 0:
                self.next_page()
            if key == ord("w") and self.page_amount > 0:
                self.cursor_up()
            if key == ord("s") and self.page_amount > 0:
                self.cursor_down()

