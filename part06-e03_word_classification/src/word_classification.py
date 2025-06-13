#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    counts = np.zeros((len(a),len(alphabet)),dtype=int)
    for i, word in enumerate(a):
        counter = Counter(word)
        for j, char in enumerate(alphabet):
            counts[i,j] = counter[char]
    return counts

def contains_valid_chars(s):
    # all() returns true if all are true
    return all(char in alphabet_set for char in s)

def get_features_and_labels():
    finnish = [word.lower() for word in load_finnish() if contains_valid_chars(word.lower())]
    english = [word.lower() for word in load_english() if contains_valid_chars(word[0]) and contains_valid_chars(word.lower())]
    X = get_features(np.array(finnish+english))
    y = np.array([0 for _ in range(len(finnish))] + [1 for _ in range(len(english))])
    return X, y


def word_classification():
    X,y = get_features_and_labels()
    model = MultinomialNB()
    kfold_param = model_selection.KFold(n_splits=5,shuffle=True,random_state=0)
    # model, x, y, kfold
    accuracy = cross_val_score(model,X,y,cv=kfold_param)
    return accuracy


def main():
    #print(get_features_and_labels())
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
