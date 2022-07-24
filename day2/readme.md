# Natural Langauge Processing || Day2 || Text Preprocessing

Natural Language Processing (NLP) is a branch of Data Science which deals with Text data. Apart from numerical data, Text data is available to a great extent which is used to analyze and solve business problems. But before using the data for analysis or prediction, processing the data is important.
To prepare the text data for the model building we perform text preprocessing. It is the very first step of NLP projects. Some of the preprocessing steps are:

- Removing punctuations like . , ! $( ) \* % @
- Removing URLs
- Removing Stop words
- Lower casing
- Tokenization
- Stemming
- Lemmatization

## 1. Lowercasing

Converting a word to lower case (NLP -> nlp).
Words like Book and book mean the same but when not converted to the lower case those two are represented as two different words in the vector space model (resulting in more dimensions).

```
   import pandas as pd
   import numpy as np

   df = pd.read_csv('./IMDB Dataset.csv')
   df['review'].str.lower()
```

## 2. Removing HTML Tags

```
import re
def remove_html_tags(text):
    pattern = re.compile('<.*?>')
    return pattern.sub(r'',text)

df['review'].apply(remove_html_tags)
```

## 3. Remove URLs

```
def remove_url(text):
    pattern = re.compile(r'https://\S+|www\.\S+')
    return pattern.sub(r'',text)
text1 = 'https://www.youtube.com hello'
remove_url(text1)
```

## 4. Remove Punctuations

```
import string

exclude = string.punctuation #'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|~'
def remove_punc1(text):
    return text.translate(str.maketrans('','',exclude))
remove_punc1(text2)
```

## 5. Chat Word Treatment

```
chat_words = {
  "AFK": "away from keyboard",
  "B4": "before",
  "IC": "I see"
}

def chat_conversion(text):
    new_text = []
    for w in text.split():
        if w.upper() in chat_words:
            new_text.append(chat_words[w.upper()])
        else:
            new_text.append(w)
    return " ".join(new_text)
chat_conversion('Why are you AFK B4 game begin, IC you are')
```

## 6. Spelling Correction

```
from textblob import TextBlob

incorrect_text = 'ceertain conditionas duriing seveal ggenerations aree moodified in the saame maner.'
textBlb = TextBlob(incorrect_text)
textBlb.correct().string
```

## 7. Removing Stop Words

Stop words are very commonly used words (a, an, the, etc.) in the documents. These words do not really signify any importance as they do not help in distinguishing two documents.

```
from nltk.corpus import stopwords
stopwords.words('english')

def remove_stopwords(text):
    new_text = []
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    x = new_text[:]
    new_text.clear()
    return " ".join(x)
remove_stopwords('i me myself hello world')
```

## 7. Handeling Emojis

```
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
remove_emoji("Loved the movie. It was 😘😘")

import emoji
print(emoji.demojize('Python is 🔥'))
```

## 8. Tokenization

Splitting the sentence into words.

> ### 8.1 Using the split function

```
# word tokenization
sent1 = 'I am going to delhi'
sent1.split()

# sentence tokenization
sent2 = 'I am going to delhi. I will stay there for 3 days. Let\'s hope the trip to be great'
sent2.split('.')

# Problems with split function
sent3 = 'I am going to delhi!'
sent3.split()

sent4 = 'Where do think I should go? I have 3 day holiday'
sent4.split('.')
```

> ### 8.2 Regular Expression

```
import re
sent3 = 'I am going to delhi!'
tokens = re.findall("[\w']+", sent3)
tokens

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry?
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book."""
sentences = re.compile('[.!?] ').split(text)
sentences
```

> ### 8.3 NLTK

```
from nltk.tokenize import word_tokenize,sent_tokenize
sent1 = 'I am going to visit delhi!'
word_tokenize(sent1)

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry?
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book."""
sent_tokenize(text)
```

> ### 8.4 Spacy

```
import spacy
nlp = spacy.load("en_core_web_sm")

sent6 = "We're here to help! mail us at nks@gmail.com"
doc2 = nlp(sent6)

for token in doc2:
    print(token)
```

## 9. Stemming

It is a process of transforming a word to its root form.

```
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])
sample = "walk walks walking walked"
stem_words(sample)
```

## 10. Lemmatization

Unlike stemming, lemmatization reduces the words to a word existing in the language.
Stemmer is easy to build than a lemmatizer as the latter requires deep linguistics knowledge in constructing dictionaries to look up the lemma of the word
**Lemmatization is preferred over Stemming because lemmatization does a morphological analysis of the words.**

```
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos='v')))
```

[regrex](https://regex101.com/)
