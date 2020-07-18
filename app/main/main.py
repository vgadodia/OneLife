import pickle

tfidf_vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
clf = pickle.load(open("model.pickle", "rb"))

def predict(k):
    return clf.predict(tfidf_vectorizer.transform([k]))[0]

def process(k):
    x = k.lower()
    final = ""

    for i in x:
        if i.isalpha() == False and i != " ":
            if i == "'":
                continue
            else:

                final += " "
        else:
            final += i 

    return final 

def get_raw_text(k):
    final = ""
    for i in k.splitlines():
        final += process(i) + " "

    return final



