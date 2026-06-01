from math import ceil

from Core.settings import TERM_W, STD_PAGE_SIZE

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

    def display_current(self):
        for i in self.data:
            print(i)

    def selector_mode(self):
        if self.page_amount == 0:
            print("No data")
            return

        for idx, i in enumerate(self.pages[self.current]):
            txt = i
            if idx == self.cursor: txt = "-->  " + txt
            print(txt)

        page_index = f"{self.current+1}/{self.page_amount}"
        print(page_index.center(TERM_W))
