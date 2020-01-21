from arrangement import Arrangement
from flowers import Rose, Lillies, Alstroemeria

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self):
        self.__flowers.append(Rose, Lillies, Alstroemeria)
