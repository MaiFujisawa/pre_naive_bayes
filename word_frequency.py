# pre_naive_bayes program
# halfway


import sys
import MeCab
m = MeCab.Tagger('-Owakati')


def road_file(file_name):
    with open(file_name, 'r') as fp:
        mails = []
        for sentence in fp:
            sentences = (sentence.rstrip()).split(',')
            mails.append(sentences)
    return mails


def wakati_sentence(sentence):
    # str->list
    words = m.parse(sentence).split()
    return words


def count_string(string, sentence2frequency={}):
    # str->dictionary
    for character in string:
        sentence2frequency[character] = sentence2frequency.get(character, 0) + 1
    return sentence2frequency


def main(textfile_name):
    mails = road_file(textfile_name)
    number_of_mails = len(mails)

    for mail in mails:
        for sentence in mail:
            words = wakati_sentence(sentence)
            word2frequency = count_string(string=words)
            for key in word2frequency:
                word2frequency[key] = word2frequency.get(key, 0) / number_of_mails
            print(word2frequency)

if __name__ == '__main__':
    textfile_name = sys.argv[1]
    main(textfile_name)

