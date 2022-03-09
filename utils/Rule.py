import pandas as pd
from time import perf_counter, sleep


def progress_bar(index, length, start):
    ratio = 50.0 / length
    progress = (index / length) * 100
    finished = '*' * int(index * ratio)
    remained = '.' * (50 - int(index * ratio))
    dur = perf_counter() - start
    print("\r{:^.0f}%[{}->{}]{:.2f}s".format(progress, finished, remained, dur), end="")


class Rule:
    def __init__(self):
        self.rules = []

    def __add__(self, letter, status, position):
        self.rules.append({'letter': letter, 'status': status, 'position': position})

    def filter(self, data: pd.DataFrame):
        length = len(data)
        ratio = 50.0 / length
        start = perf_counter()
        new_words = []
        new_frequency = []
        for index, row in data.iterrows():
            flag = True
            for rule in self.rules:
                if rule['status'] == -1:  # If the letter doesn't exist in this word
                    if row['word'].find(rule['letter']) != -1:
                        flag = False
                        break
                elif rule['status'] == 0:  # If the letter was put in a wrong position
                    if row['word'][rule['position']] == rule['letter'] or row['word'].find(rule['letter']) == -1:
                        flag = False
                        break
                elif rule['status'] == 1:  # If the letter was put in the right position
                    if row['word'][rule['position']] != rule['letter']:
                        flag = False
                        break
            if flag:
                new_words.append(row['word'])
                new_frequency.append(row['frequency'])
            progress_bar(index, length, start)
        print()
        new_data = pd.DataFrame({'word': new_words, 'frequency': new_frequency})
        return new_data

    def show(self):
        print(self.rules)


# TEST MODULE
if __name__ == '__main__':
    rules = Rule()
    rules.__add__('c', 1, 0)
    rules.__add__('r', -1, 1)
    rules.__add__('a', 0, 2)
    rules.__add__('k', -1, 3)
    rules.__add__('e', -1, 4)
    data = pd.read_csv('../data/data.csv')
    print(rules.filter(data))
    print('----------------------------------')
