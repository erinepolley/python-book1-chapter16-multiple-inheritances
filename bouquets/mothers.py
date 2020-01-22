from . import Arrangement

class MothersDay(Arrangement):
    def __init__(self):
        super().__init__(4, False)


    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added