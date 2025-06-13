#!/usr/bin/env python3

import gzip as gz
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

def spam_detection(random_state=0, fraction=1.0):
    with gz.open("src/ham.txt.gz") as nonspam:
        ham_d = nonspam.readlines()
        lc = int(len(ham_d) * fraction)

    ham_d = ham_d[:lc]

    with gz.open("src/spam.txt.gz") as spam:
        spam_d = spam.readlines()
        lc = int(len(spam_d) * fraction)

    spam_d = spam_d[:lc]

    data = ham_d + spam_d

    f_mat = CountVectorizer()
    X = f_mat.fit_transform(data)
    y = [0 for _ in range(len(ham_d))] + [1 for _ in range(len(spam_d))]

    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.75,random_state=random_state)

    model = MultinomialNB()
    # Train with training data
    model.fit(X_train,y_train)
    # Predict with test data
    y_pred = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)

    return accuracy, len(y_test), int((1-accuracy) * len(y_test))

def main():
    if True:
        accuracy, total, misclassified = spam_detection()
        print("Accuracy score:", accuracy)
        print(f"{misclassified} messages miclassified out of {total}")
    else:
        print(spam_detection())

if __name__ == "__main__":
    main()
