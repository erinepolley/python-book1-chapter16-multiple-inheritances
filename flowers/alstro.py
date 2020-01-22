from . import Flower
from . import Irando

class Alstro(Flower):
    def __init__(self):
        Flower.__init__(self)
        Irando.__init__(self,"heeeeyyyy")
        self.alstro_blah = ""