def get_all_status():
    all_status = []
    return all_status


class Status:
    def __init__(self, status=[0, 0, 0, 0, 0]):
        """
        :param status: Each element in this array stands for the match result in the puzzle
        -1 means gray, which means this letter doesn't exist in this word
        0 means yellow, which means this letter exists in this word but was put in a wrong position
        1 means green, which means this letter exists in this word and was put in the right position
        """
        self.status = status
