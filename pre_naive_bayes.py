# 全てのメールについてすべての文字の頻度を数える
import sys
import MeCab
m = MeCab.Tagger("-Owakati")


def file_reading(file_name):
    lines = []
    with open(file_name, 'r') as fp:
        for line in fp:
            line = line.rstrip('\n')
            lines.append(line)
    return lines

def file_writing(dict):
    with open("output.txt",'w') as fp:
        fp.write(dict)

def label_freq(sentence):
    words = []
    for sent in sentence:
        sent = list(sent)
        words.append(sent[0])
        #mail is list. word is the lead of list.

    label2freq = {}
    for label in words:
        label2freq[label] = label2freq.get(label, 0) + 1

    items = label2freq.items()
    for label,freq in sorted(label2freq.items(),key=lambda x: -x[1]):
        print(str(label) + ":" + str(freq))



def word_freq(lines):
    words = []
    for line in lines:
        word_list = m.parse(line).split(" ")
        words.extend(word_list)

    word2frequency = {}
    for word in words:
        word2frequency[word] = word2frequency.get(word, 0)+1

    items = word2frequency.items()
    for label, freq in sorted(items, key=lambda x: -x[1]):
        print(str(label) + ":" + str(freq))


def main():
    file_name = sys.argv[1]
    lines = file_reading(file_name)
    label_freq(lines)
    word_freq(lines)

main()
