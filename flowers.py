class Flower:
    def __init__(self, stem_length, organic):
        self.stem_length = stem_length
        self.organic = organic


class Rose(Flower): 
    def __init__(self, color):
        super.__init__(stem_length, organic)
        self.color = color

class Daisy(Flower):
    def __init__(self):
        super.__init__(stem_length, organic)

class Babbys_Breath():
    def __init__(self):
        self.stem_length = 0
        self.organic = ""

class Poppies():
    def __init__(self):
        self.stem_length = 0
        self.organic = ""

class Lillies():
    def __init__(self):
        self.stem_length = 0
        self.organic = ""

class Alstroemeria():
    def __init__(self):
        self.stem_length = 0 
        self.organic = ""

