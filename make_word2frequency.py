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
    for character in string:
        sentence2frequency[character] = sentence2frequency.get(character, 0) + 1
    return sentence2frequency


def count_probability_of_labels(w2f,number_of_mails,word2probability={}):
    for key in w2f:
        word2probability[key] = word2probability.get(key, 0) / number_of_mails
    return word2probability


def main(textfile_name):
    labels_and_sentences = road_file(textfile_name)
    number_of_mails = len(labels_and_sentences)

    for label_and_sentence in labels_and_sentences:
        for sentence in label_and_sentence:
            words = wakati_sentence(sentence)
            word2frequency = count_string(string=words)
            print(word2frequency)
            prob_label = count_probability_of_labels(word2frequency,number_of_mails)
            

if __name__ == '__main__':
    textfile_name = sys.argv[1]
    main(textfile_name)
