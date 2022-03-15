import pandas as pd
import math
from utils import View
from utils.Rule import Rule
from time import perf_counter
import pandas as pd
from itertools import product
from typing import List, Tuple
from multiprocessing.dummy import Pool


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
    # View.title_bar('Filtering Data by Rules...')
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
        # View.progress_bar(index, length, start)
    # print()
    new_data = pd.DataFrame({'word': new_words, 'frequency': new_frequency})
    return new_data


def generate_all_situation():
    match = [-1, 0, 1]
    res = [i for i in product(match, match, match, match, match)]
    return res


def get_information_entropy(situation, word, data):
    rules = []
    entropy = 0
    for i in range(5):
        rule = Rule(word[i], situation[i], i)
        rules.append(rule)
    filtered_data = filter_all_rules(rules, data)
    # Recalculate the possibility
    sum_frequency = filtered_data['frequency'].sum()
    for _index, _row in filtered_data.iterrows():
        possibility = _row['frequency'] / sum_frequency
        entropy += possibility * math.log(1 / possibility, 2)
    return entropy


def get_all_information_entropy(all_situation: List[Tuple[int]], data: pd.DataFrame):
    """
    Calculate the information entropy and save the result
    :data:
    :return:
    """
    res = []
    start = perf_counter()
    length = data.__len__()
    View.title_bar('Calculating Information Entropy...')
    for index, row in data.iterrows():
        entropy = 0
        pool = Pool(300)
        params = []
        for situation in all_situation:
            entropy += pool.apply(get_information_entropy, (situation, row['word'], data))
        pool.close()
        pool.join()
        View.progress_bar(index, length, start)
        res.append(entropy)
    return res


# TEST MODULE
if __name__ == '__main__':
    all_situation = generate_all_situation()
    data = pd.read_csv('data/data.csv')
    entropy = get_all_information_entropy(all_situation, data)
    data['entropy'] = entropy
    View.title_bar('Saving Results...')
    data.to_csv('data/data.csv', index=False)
    # rules = [Rule('c', 1, 0), Rule('r', -1, 1), Rule('a', 0, 2), Rule('k', -1, 3), Rule('e', -1, 4)]
    # data = pd.read_csv('../data/data.csv')
    # print(filter_all_rules(rules, data))
    # print('=' * 50)
