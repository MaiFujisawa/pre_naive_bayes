# 全てのメールについてすべての文字の頻度を数える

import sys
import re
import MeCab

m = MeCab.Tagger("-Owakati")
from collections import Counter


def file_reading(file_name):
    lines = []
    with open(file_name, 'r') as fp:
        for line in fp:
            line = line.rstrip('\n')
            # lines.append(line)
    return line


def count_word2freq_perLabel(sentence):
    # count word's frequency per mail
    word_str = m.parse(sentence)
    words = re.split('[,. ]',word_str)
    counter = Counter(words)
    return (counter)


def count_label_frequency(sentences):
    labels = sentences.split(',')
    return labels[0]


def make_label2word2freq(sentences,word2freq):   
    sentences = sentences.split(',')   
    # sentences is label's list   
    label2word2freq = {}   

    for sent in sentences:   
        label2word2freq[sent] = label2word2freq.get(sent, {})   
        label2word2freq = word2freq(sent, label2word2freq)   
    return(label2word2freq)   

    # word2total = {}   
    # word2total.keys = label2frequency['S']   
    # word2total.values = word2frequency{word}   
    # print(word2total)  

def calc_pLabel(l2f, last):   
    label2calc = {}   
    for label in l2f.keys():   
        label2calc[label] = l2f[label] /last
    return label2calc   




def main():
    file_name = sys.argv[1]
    line = file_reading(file_name)
    lines = []
    lines.append(line)
    last_sentence = len(lines)

    for label in range(0, last_sentence):
        word2freq = count_word2freq_perLabel(lines[label])
        word2freq = dict(word2freq)

    label2word2freq = make_label2word2freq(line,word2freq)
    print(label2word2freq)
main()

