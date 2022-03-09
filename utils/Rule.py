class Rule:
    def __init__(self, letter, status, position):
        """
        :param letter:
        :param status: the match result in the puzzle
                        -1 means gray, which means this letter doesn't exist in this word
                        0 means yellow, which means this letter exists in this word but was put in a wrong position
                        1 means green, which means this letter exists in this word and was put in the right position
        :param position:
        """
        self.letter = letter
        self.status = status
        self.position = position
