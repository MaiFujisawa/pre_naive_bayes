#pythonでmecabを使い、単語の総数を数えて表示
import sys
import MeCab
import collections

file_name = sys.argv[1]
m = MeCab.Tagger ("-Owakati")


with open(file_name, 'r') as fp:
    sum = 0
    for line in fp:
        lines = (m.parse(line)).split()
        sum += len(lines)

    try:
        print(sum)
    except TypeError:
        print("error!")
