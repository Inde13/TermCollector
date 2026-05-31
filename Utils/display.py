from Core.settings import TERM_W, STD_LINE_CHAR

def option_menu(options):
    for idx, opt in enumerate(options):
        print(f"[{idx+1}] - {opt}")

def clr():
    from os import system
    system('clear')

def line(n=TERM_W, char=STD_LINE_CHAR):
    print(char*n)

def table(titles=None, cols=None, template=None):
    if cols is None or not cols:
        print("Empty...")
        return

    sizes = [max([len(str(i)) for i in col]) for col in cols]
    template = template or "|".join(
            [" {"+f"{sizes.index(s)}:<"+f"{s+2}"+"}"
             for s in sizes])
    print(template.format(*titles))
    line()
    for row in zip(*cols):
        print(template.format(*row))

def display_container(container, order=None, id=False,
                      name=True, quantity=True):
    if container.is_empty():
        table()
        return
    order = order or [
                "id" if id else None,
                "name" if name else None,
                "quantity" if quantity else None
            ]
    order = [i for i in order if i is not None]

    cols = []
    for key in order: # Invert later for better performance
        cols.append([])
        idx = len(cols)-1
        for item in container.get():
            cols[idx].append(getattr(item, key))

    table([i.title() for i in order], cols)


