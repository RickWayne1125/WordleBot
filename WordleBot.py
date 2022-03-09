import numpy as np
import pandas as pd
from utils import Rule, View
from time import perf_counter
from typing import List


class WordleBot:
    def __init__(self, data_path='data/data.csv'):
        self.data = pd.read_csv(data_path)

    def get_open_word(self):
        res = ''

        return res

    def get_one_word(self):
        return


def filter_all_rules(rules: List[Rule], data: pd.DataFrame):
    length = len(data)
    ratio = 50.0 / length
    start = perf_counter()
    new_words = []
    new_frequency = []
    View.title_bar('Filtering Data by Rules...')
    for index, row in data.iterrows():
        flag = True
        for rule in rules:
            if rule.status == -1:  # If the letter doesn't exist in this word
                if row['word'].find(rule.letter) != -1:
                    flag = False
                    break
            elif rule.status == 0:  # If the letter was put in a wrong position
                if row['word'][rule.position] == rule.letter or row['word'].find(rule.letter) == -1:
                    flag = False
                    break
            elif rule.status == 1:  # If the letter was put in the right position
                if row['word'][rule.position] != rule.letter:
                    flag = False
                    break
        if flag:
            new_words.append(row['word'])
            new_frequency.append(row['frequency'])
        View.progress_bar(index, length, start)
    print()
    new_data = pd.DataFrame({'word': new_words, 'frequency': new_frequency})
    return new_data


# TEST MODULE
if __name__ == '__main__':
    rules = [Rule('c', 1, 0), Rule('r', -1, 1), Rule('a', 0, 2), Rule('k', -1, 3), Rule('e', -1, 4)]
    data = pd.read_csv('../data/data.csv')
    print(filter_all_rules(rules, data))
    print('=' * 50)
