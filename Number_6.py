from re import sub
from string import punctuation
import numpy as np


class FileSplitter:
    def __init__(self):
        self.splitted_text = ''

    def split_file(self, file_name):
        file_reader = open(file_name, 'r')
        file_text = file_reader.read()
        self.splitted_text = sub('[' + punctuation + '0123456789-]', '', file_text).split()
        return self.splitted_text


class WordPredictor:
    def __init__(self, book):
        self.book = [(i.lower()) for i in book]  # to lower case
        self.predicted_words = []

    def predict(self, prefix, predict_counter=1):
        result = []
        prefix_size = len(prefix)
        if prefix_size < 2:
            second_element = False
            current_predict = prefix
        else:
            current_predict = prefix[-2:]
            second_element = True

        # predict
        ready = False
        for j in range(predict_counter):
            for i in range(len(self.book)-1):
                if ready and not second_element:
                    self.predicted_words.append(self.book[i])
                    ready = False
                elif ready and second_element and self.book[i] == current_predict[1]:
                    self.predicted_words.append(self.book[i + 1])
                    ready = False
                elif not ready and self.book[i] == current_predict[0]:
                    ready = True
                else:
                    ready = False

            if len(self.predicted_words) != 0:
                result.append(np.random.choice(self.predicted_words))
                current_predict = [current_predict[-1], result[-1]]
                second_element = True
                self.predicted_words = []
                ready = False

        return result


# split text
fileSplitter = FileSplitter()
bookText = fileSplitter.split_file('Library.txt')

# input
print('Введите префикс: ')
prefix = input().lower().split()
print('Введите число слов для предсказывания: ')
predict_counter = int(input())

# predict words
wordPredictor = WordPredictor(bookText)
predicted = wordPredictor.predict(prefix=prefix, predict_counter=predict_counter)
print(prefix + predicted)
