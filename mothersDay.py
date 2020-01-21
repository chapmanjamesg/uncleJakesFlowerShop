from arrangement import Arrangement
from flowers import Daisy, Babbys_Breath, Poppies

class MothersDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self):
        self.__flowers.append(Daisy, Babbys_Breath, Poppies)