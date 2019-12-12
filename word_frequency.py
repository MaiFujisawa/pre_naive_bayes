# pre_naive_bayes program
#word2frequency
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


def count_label2frequency(sentence):
    # str->dictionary
    sentence = wakati_sentence(sentence)
    word2frequency = count_sentence2frequency(sentence)
    return word2frequency


def wakati_sentence(sentence):
    # str->list
    words = m.parse(sentence).split()
    return words

def count_sentence2frequency(sentence):
    # str->dictionary
    sentence2frequency = {}
    for sent in sentence:
        sentence2frequency[sent] = sentence2frequency.get(sent, 0) + 1
    return sentence2frequency


def main(textfile_name):
    mails = road_file(textfile_name)
    number_of_mails = len(mails)
    #print(mails[0][0]) N
    #print(mails[0][1]) （重複して...ただくこともあります．

    # make word2frequency per labels
    # split label and sentence

    labels = []
    words_labels = []
    mails_list = []
    for mail in mails:
        labels.append(mail[0])
        for sentence in mail:
            for label in labels:
                words = wakati_sentence(sentence)
                word2frequency = count_sentence2frequency(words)
            word_label2freq = count_sentence2frequency(words_labels)
    print(word2frequency/len(word_label2freq))


if __name__ == '__main__':
    textfile_name = sys.argv[1]
    main(textfile_name)

