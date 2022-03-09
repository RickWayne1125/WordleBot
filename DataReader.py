import pandas as pd
import numpy as np


class DataReader:
    def __init__(self, raw_data_path='data/unigram_freq.csv', data_path='data/data.csv'):
        # https://www.kaggle.com/rtatman/english-word-frequency
        # This dataset was well sorted by frequency
        self.raw_data_path = raw_data_path
        self.data_path = data_path

    def extract_5gram_words(self):
        """
        Extract the 5-gram-words from the raw data
        :return:
        """
        raw_data = pd.read_csv(self.raw_data_path)
        _5gram_word = []
        _5gram_count = []
        for index, row in raw_data.iterrows():
            if type(row['word']) == str and len(row['word']) == 5:
                _5gram_count.append(row['count'])
                _5gram_word.append(row['word'])
        df = pd.DataFrame({'word': _5gram_word, 'count': _5gram_count})
        print(df)
        df.to_csv(self.data_path)
        return

    def get_sigmoid_frequency(self):
        """
        Calculate the word frequency after sigmoid smoothing and save the result
        :return:
        """
        data = pd.read_csv(self.data_path)
        length = data.__len__()
        mid = length / 2  # This decides where the middle point is
        ratio = 0.001  # This decides the zoom ration on the axis
        frequency = []
        for index, row in data.iterrows():
            x = (length - index - mid) * ratio
            smooth_frequency = 1 / (1 + np.exp(-x))
            frequency.append(smooth_frequency)
        data['frequency'] = frequency
        data.to_csv(self.data_path)

    def get_information_entropy(self):
        """
        Calculate the information entropy and save the result
        :return:
        """
        


if __name__ == '__main__':
    # extract_5gram_words()
    DataReader.get_sigmoid_frequency()
