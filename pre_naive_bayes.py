# pre_naive_bayes program
# halfway


import sys
import MeCab
m = MeCab.Tagger("-Owakati")


def file_reading(file_name):
    #output is str
    mails = ""
    with open(file_name, 'r') as fp:
        for line in fp:
            mails += line
    return mails



def make_mail_list(mail):
    # str->list
    mails = (mail.strip()).splitlines()
    return mails


def devide_label_and_sentence(sentence):
    #str->dist
    labels_and_sentences = sentence.split(',')
    label = labels_and_sentences[0]
    sentence = count_label2frequency(labels_and_sentences[1])
    label2sentence = {}
    label2sentence = {label:sentence}
    return label2sentence


def count_label2frequency(sentence):
    # str->dictionary
    sentence = wakati_sentence(sentence)
    word2frequency = count_sentence2frequency(sentence)
    return word2frequency


def count_sentence2frequency(sentence):
    # str->dictionary
    sentence2frequency = {}
    for sent in sentence:
        sentence2frequency[sent] = sentence2frequency.get(sent, 0) + 1
    return sentence2frequency


def count_label2sentence(sentences):
    #list->dict
    label = sentences[0]

    #sentence = sentences[1]
    #label2sentence = {label:sentence}
    #return label2sentence
    return label


def wakati_sentence(sentence):
    #str->list
    words = m.parse(sentence).split()
    return words



def main():
    file_name = sys.argv[1]
    mail_data = file_reading(file_name)

#count label2sentence
    #make_label2(word2frequency)
    # [{label,{word,frequency}}...]
    mails = make_mail_list(mail_data)
    all_mails_length = len(mails)
    all_mails = []
    for num in range(all_mails_length):
            label2sentence = devide_label_and_sentence(mails[num])
            all_mails.append(label2sentence)



#calc p(label)
    labels_str = []

    for num in range(all_mails_length):
        labels_and_sentences = (mails[num]).split(',')
        labels_str.append(labels_and_sentences[0])
        label2freq = count_sentence2frequency(labels_str)



    #calc p(word|label)
    # ラベルごとにメールをリストに格納する
    #メール内の単語の頻度を数える  


if __name__ == '__main__':
    main()



