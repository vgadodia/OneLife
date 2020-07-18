from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle 

data = pd.read_csv("data.csv")

X = data.text 
y = data.label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 53)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')

tfidf_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_test = tfidf_vectorizer.transform(X_test)

clf = MultinomialNB()
clf.fit(tfidf_train, y_train)

with open("model.pickle", "wb") as f:
	pickle.dump(clf, f)

with open("vectorizer.pickle", "wb") as g:
	pickle.dump(tfidf_vectorizer, g)

pred = clf.predict(tfidf_test)
print(pred)
score = accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)
