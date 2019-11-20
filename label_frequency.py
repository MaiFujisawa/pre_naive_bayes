# 全てのメールの最後のメールについてすべての文字の頻度を数える
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
    # 全文を一気に読み込み、辞書に渡して頻度を計算させる
    words = []
    for sent in sentence:
        sent = m.parse(sent).split(" ")
        words.append(sent)

    label2frequency = {}
    words = str(words)
    for label in words:
        label2frequency[label] = label2frequency.get(label, 0) + 1

    items = label2frequency.items()
    for label,freq in sorted(label2frequency.items(),key=lambda x: -x[1]):
        print(str(label) + ":" + str(freq))

def main():
    file_name = sys.argv[1]
    lines = file_reading(file_name)
    label_freq(lines)

main()
