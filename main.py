import spacy

nlp = spacy.load("el_core_news_lg")
file = open('stopwords.txt', encoding="utf8")
contents = file.read()
search_word = input("enter a word you want to search in file: ")
x = search_word.lower().split()


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + ' '

        # return string
    return str1


phrase = []
i = 0
for i in x:

    if i in contents:
        continue
    else:
        phrase.append(i)

o = 0
doc = nlp(listToString(phrase))
for i in doc:
    if doc[o].pos_ == 'VERB':
        phrase[o], phrase[len(phrase) - 1] = phrase[len(phrase) - 1], phrase[o]
    if o > len(phrase):
        continue
    elif doc[o].pos_ == 'ADJ' and doc[o + 1].pos_ == 'NOUN':
        phrase[o], phrase[o + 1] = phrase[o + 1], phrase[o]
    o += 1
print(phrase)
