from typing import List

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('omw-1.4')
# nltk.download('brown')

lemmatizer = WordNetLemmatizer()
domain = wordnet.synset('cinema.n.01')


# print(domain.similar("actor"))


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


def normalize_words(word: str, pos: str) -> str:
    return lemmatizer.lemmatize(word, pos=get_wordnet_pos(pos))


def get_normalize_nouns(text: str) -> List[str]:
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'

    tokenized = nltk.word_tokenize(text)
    nouns = [normalize_words(word, pos) for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    return nouns


def get_normalize_verbs(text: str) -> List[str]:
    # function to test if something is a verb
    is_verb = lambda pos: pos[:2] == 'VB'

    tokenized = nltk.word_tokenize(text)
    verbs = [normalize_words(word, pos) for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    return verbs


def parse_text(text):
    noun = get_normalize_nouns(text)[0]
    verb = get_normalize_verbs(text)[0]
    return noun, verb


if __name__ == '__main__':
    local_text = "I want to know sothing about my favourite actress 'Camila Ban' "

    var = get_normalize_nouns(local_text)[0]
    print(get_normalize_nouns(local_text))
    print(get_normalize_verbs(local_text))

    var_syn = wordnet.synset(var + ".n.01")
    print(domain.wup_similarity(var_syn))


