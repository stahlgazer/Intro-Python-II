# Write classes for the following class hierarchy:
#
#  [Tool]->[DrawingUtensil]->[Pencil]
#      |                |
#      v                v
# [EatingUtensil]      [Pen]
#   |       |
#   v       v
# [Fork]  [Spoon]

class Tool:
    def __init__(self):
        super().__init__()

class DrawingUtensil(Tool):
    def __init__(self):
        super().__init__()

class Pencil(DrawingUtensil):
    def __init__(self):
        super().__init__()

class Pen(DrawingUtensil):
    def __init__(self):
        super().__init__()
        
class EatingUtensil:
    def __init__(self):
        super().__init__()

class Fork(EatingUtensil):
    def __init__(self):
        super().__init__()

class Spoon(EatingUtensil):
    def __init__(self):
        super().__init__()