'''''
PICKLE_FILE = "article_html.pkl"

def score_sentence_by_token(sentence, interesting_tokens):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
    if not tokens:
        return 0.0
    count = sum(1 for token in tokens if token in interesting_tokens)
    return count / len(tokens)

# Load article HTML and extract text
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)
soup = BeautifulSoup(article_html, "html.parser")
text = soup.get_text()

# Load spaCy pipeline and process text
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Get frequent tokens
tokens = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]
token_freq = Counter(tokens)
most_common_tokens = [token for token, _ in token_freq.most_common(5)]
'''

'''
PICKLE_FILE = "article_html.pkl"

def score_sentence_by_lemma(sentence, interesting_lemmas):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    lemmas = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_space]
    if not lemmas:
        return 0.0
    count = sum(1 for lemma in lemmas if lemma in interesting_lemmas)
    return count / len(lemmas)

# Load article HTML and extract text
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)
soup = BeautifulSoup(article_html, "html.parser")
text = soup.get_text()

# Load spaCy pipeline and process text
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Get frequent lemmas
lemmas = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]
lemma_freq = Counter(lemmas)
most_common_lemmas = [lemma for lemma, _ in lemma_freq.most_common(5)]
'''