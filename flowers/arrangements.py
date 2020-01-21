class Arrangement():

    def __init__(self, stem_size, refrigerated):
        self.__flowers = []
        self.stem_size_inches = stem_size
        self.refrigerated = refrigerated

    def enhance(self, flower):
        self.__flowers.append(flower)