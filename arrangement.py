class Arrangement:
    def __init__(self, name):
        self.__flowers = []
        self.name = name
        

    def enhance(self, flower):
        self.__flowers.append(flower)