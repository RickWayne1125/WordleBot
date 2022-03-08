import pandas as pd
import numpy as np

# https://www.kaggle.com/rtatman/english-word-frequency
# This data was well sorted by frequency
raw_data_path = 'data/unigram_freq.csv'
data_path = 'data/data.csv'


def extract_5gram_words():
    """
    Extract the 5-gram-words from the raw data
    :return:
    """
    raw_data = pd.read_csv(raw_data_path)
    _5gram_word = []
    _5gram_count = []
    for index, row in raw_data.iterrows():
        if type(row['word']) == str and len(row['word']) == 5:
            _5gram_count.append(row['count'])
            _5gram_word.append(row['word'])
    df = pd.DataFrame({'word': _5gram_word, 'count': _5gram_count})
    print(df)
    df.to_csv(data_path)
    return


def get_sigmoid_frequency():
    """
    Calculate the word frequency after sigmoid smoothing and save
    :return:
    """
    data = pd.read_csv(data_path)
    length = data.__len__()
    mid = length / 2  # This decides where the middle point is
    ratio = 0.001  # This decides the zoom ration on the axis
    frequency = []
    for index, row in data.iterrows():
        x = (length - index - mid) * ratio
        smooth_frequency = 1 / (1 + np.exp(-x))
        frequency.append(smooth_frequency)
    data['frequency'] = frequency
    data.to_csv(data_path)


if __name__ == '__main__':
    # extract_5gram_words()
    get_sigmoid_frequency()
