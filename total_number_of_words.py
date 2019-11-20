#pythonでmecabを使い、単語の総数を数えて表示
import sys
file_name = sys.argv[1]
import MeCab

import collections

m = MeCab.Tagger ("-Owakati")

with open(file_name, 'r') as fp:

    sum = 0
    for line in fp:
        line = m.parse(line)
        result = line.split()
        print(result)
        result = len(result)
        #resultは各メール中の単語の数
        sum += result

    try:
        print(sum)
    except TypeError:
        print("error!")