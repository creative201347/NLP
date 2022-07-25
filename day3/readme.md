# Natural Langauge Processing || Day3 || Text Representation

Feature Extraction is a general term that is also known as a text representation of text vectorization which is a process of converting text into numbers. we call vectorization because when text is converted in numbers it is in vector form.

- `Corpus(C)` ~ The total number of combinations of words in the whole dataset is known as Corpus. In simple words concatenating all the text records of the dataset forms a corpus.
- `Vocabulary(V)` ~ a total number of distinct words which form your corpus is known as Vocabulary.
- `Document(D)` ~ There are multiple records in a dataset so a single record or review is referred to as a document.
- `Word(W)` ~ Words that are used in a document are known as Word.

## Techniques for Feature Extraction

### 1. One-Hot Encoding

One hot encoding means converting words of your document in a V-dimension vector and by combining all this we get a single document so at the end we have a two-dimensional array. This technique is very intuitive means it is simple and you can code it yourself.

#### Disadvantages

1. Sparsity – You can see that only a single sentence creates a vector of n\*m size where n is the length of sentence m is a number of unique words in a document and 80 percent of values in a vector is zero.
2. No fixed Size – Each document is of a different length which creates vectors of different sizes and cannot feed to the model.
3. Does not capture semantics – The core idea is we have to convert text into numbers by keeping in mind that the actual meaning of a sentence should be observed in numbers that are not seen in one-hot encoding.

### 2. Bag Of Words

It is one of the most used text vectorization techniques. It is mostly used in text classification tasks. Bag of words is a little bit similar to one-hot encoding where we enter each word as a binary value and in a Bag of words we keep a single row and entry the count of words in a document. So we create a vocabulary and for a single document, we enter one entry of which words occur how many times in a document.

#### Advantages

1. Simple and intuitive – Only a few lines of code are required to implement the technique.
2. Fix size vector – The problem which we saw in one-hot encoding where we are unable to feed data the data to machine learning model because each sentence forms a different size vector but here It ignores the new words and takes only words which are vocabulary so creates a vector of fix size.

#### Disadvantages

1. Out of vocabulary situation – It keeps count of vocabulary words so if new words come in a sentence it simply ignores it and tracks the count of the words that are in vocabulary. But what if the words it ignores are important in predicting the outcome so this is a disadvantage, only benefit is it does not throw an error.
2. Sparsity – when we have a large vocabulary, and the document contains a few repeated terms then it creates a sparse array.
3. Not considering ordering is an issue – It is difficult to estimate the semantics of the document.

### 3. N-Grams

The technique is similar to Bag of words. All the techniques till now we have read it is made up of a single word and we are not able to use them or utilize them for better understanding. So N-Gram technique solves this problem and constructs vocabulary with multiple words. When we built an N-gram technique we need to define like we want bigram, trigram, etc. So when you define N-gram and if it is not possible then it will throw an error. In our case, we cannot build after a 4 or 5-gram model.

#### Advantages

1. Able to capture semantic meaning of the sentence – As we use Bigram or trigram then it takes a sequence of sentences which makes it easy for finding the word relationship.
2. Intuitive and easy to implement – implementation of N-Gram is straightforward with a little bit of modification in Bag of words.

#### Disadvantages

1. As we move from unigram to N-Gram then dimension of vector formation or vocabulary increases due to which it takes a little bit more time in computation and prediction
2. no solution for out of vocabulary terms – we do not have a way another than ignoring the new words in a new sentence.

### 4.TF-IDF (Term Frequency and Inverse Document Frequency)

#### Advantages

1. Simple, easy to understand & interpret implementation
2. Builds over CountVectorizer to penalise highly frequent words & low frequency terms in a corpus. So in a way, IDF achieves in reducing noise in our matrix.

#### Disadvantages

1. Positional information of the word is still not captured in this representation
2. TF-IDF is highly corpus dependent. A matrix representation generated out of cricket data cannot be used for football or volleyball. Therefore, there is a need to have high quality training data
