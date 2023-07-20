


class Counter():
    def __init__(self, number=0):
        self.value = number

    def reset(self):
        self.value = 0

    def add(self, number=1):
        self.value += number

    def rest(self, number=1):
        self.value -= number

    def get(self):
        return self.value
    
    def set(self, number):
        self.value = number