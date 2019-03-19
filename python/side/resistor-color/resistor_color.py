_COLORS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

def color_code(color):
    return _COLORS.get(color)

def colors():
    return [k[0] for k in sorted(_COLORS.items(), key=lambda x: x[1])]
