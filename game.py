import random
import string

class Game :

    def __init__(self):

        # self.grid = ["A","B","C","D","E","F","G","H","G"]*
        self.grid= random.choices (string.ascii_uppercase, k=9)


    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
