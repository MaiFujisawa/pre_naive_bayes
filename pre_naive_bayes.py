# pre_naive_bayes program
#print word2frequency per mail
#print label's frequency in whole sentences
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
 
 
 
def main(textfile_name): 
    mails = road_file(textfile_name) 
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
                for key in word2frequency: 
                    word_label = key + '_'+label 
                    words_labels.append(word_label) 
        word_label2freq = count_sentence2frequency(words_labels) 
        mails_list.append(word_label2freq) 
    print(mails_list) 
 
 
    # mails_list = [{word_label,frequency},{word_label,frequency}...] 
 
 
    # calc p(label) 
    labels = [] 
    number_of_mails = len(mails) 
    for mail in mails: 
        labels.append(mail[0]) 
        label2freq = count_sentence2frequency(labels) 
        for key in label2freq: 
            label2freq[key] = label2freq.get(key,0)/number_of_mails 
    print(label2freq) 
 
 
    # calc p(word|label) 
    #count len(word2frequency_per_label) 
    #calculate word2frequency/len(word2frequency_per_label) 
 
 
if __name__ == '__main__': 
    textfile_name = sys.argv[1] 
    main(textfile_name) 
