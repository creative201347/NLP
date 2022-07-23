import nltk

sentence = """Hello!! It's introduction.
Getting started in Natural Language Processing!!"""
tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
