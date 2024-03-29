'''
Run Following in Python Shell
---------------------------------
[--NLTK:---https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/stopwords.zip]]
>>> pip3 install nltk
>>> import nltk
>>> from nltk.corpus import stopwords
>>> nltk.download('stopwords')
>>> set(stopwords.words('english'))
>>> nltk.download('punkt')
---------------------------------------
'''


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print(word_tokens)
print(filtered_sentence)
