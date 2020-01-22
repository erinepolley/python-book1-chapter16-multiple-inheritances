from . import Flower
from . import Irando

class Rose(Flower, Irando):
    def __init__(self, color):
        Flower.__init__(self)
        Irando.__init__(self, "random!")
        self.color = color
        

