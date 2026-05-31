def to_number(x):
    try:
        x = int(x)
    finally:
        return x

def is_number(x: str):
    return x.isnumeric()
