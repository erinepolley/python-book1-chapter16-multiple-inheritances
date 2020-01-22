from . import Flower
from . import Irando

class Lilly(Flower, Irando):
    def __init__(self):
        self.lilly_blah = ""
        Flower.__init__(self)
        Irando.__init__(self,"WHAAT")
        
      