URL = "https://web.archive.org/web/20210327165005/https://hackaday.com/2021/03/22/how-laser-headlights-work/"
PICKLE_FILE = "article_html.pkl"

# Fetch the page
response = requests.get(URL)
response.raise_for_status()

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the article HTML
article = soup.find("article")
article_html = str(article) if article else None

# Dump to pickle file
with open(PICKLE_FILE, "wb") as f:
    pickle.dump(article_html, f)

print(f"Article HTML extracted and saved to {PICKLE_FILE}")

PICKLE_FILE = "article_html.pkl"

# Load the article HTML from the pickle file
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)

# Parse the HTML and print its text
if article_html:
    soup = BeautifulSoup(article_html, "html.parser")
    print(soup.get_text())
else:
    print("No article HTML found in the pickle file.")

   PICKLE_FILE = "article_html.pkl"

# Load the article HTML from the pickle file
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)

# Parse the HTML and extract text
soup = BeautifulSoup(article_html, "html.parser")
text = soup.get_text()

# Load a trained spaCy pipeline
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Filter tokens: remove stopwords, punctuation, and whitespace
tokens = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]

# Count token frequencies
token_freq = Counter(tokens)
most_common = token_freq.most_common(5)

# Print results
print("Top 5 most frequent tokens:")
for token, freq in most_common:
    print(f"Token: '{token}' - Frequency: {freq}")

print("\nAll token frequencies:")
for token, freq in token_freq.items():
    print(f"Token: '{token}' - Frequency: {freq}")

     PICKLE_FILE = "article_html.pkl"

# Load the article HTML from the pickle file
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)

# Parse the HTML and extract text
soup = BeautifulSoup(article_html, "html.parser")
text = soup.get_text()

# Load a trained spaCy pipeline 
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Filter tokens: remove stopwords, punctuation, and whitespace, then get lemmas
lemmas = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]

# Count lemma frequencies
lemma_freq = Counter(lemmas)
most_common = lemma_freq.most_common(5)

# Print results
print("Top 5 most frequent lemmas:")
for lemma, freq in most_common:
    print(f"Lemma: '{lemma}' - Frequency: {freq}")

print("\nAll lemma frequencies:")
for lemma, freq in lemma_freq.items():
    print(f"Lemma: '{lemma}' - Frequency: {freq}")

    PICKLE_FILE = "article_html.pkl"

def score_sentence_by_token(sentence, interesting_tokens):
    """
    Returns the number of times any interesting token appears in the sentence,
    divided by the number of words in the sentence.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
    if not tokens:
        return 0.0
    count = sum(1 for token in tokens if token in interesting_tokens)
    return count / len(tokens)

def score_sentence_by_lemma(sentence, interesting_lemmas):
    """
    Returns the number of times any interesting lemma appears in the sentence,
    divided by the number of words in the sentence.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    lemmas = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_space]
    if not lemmas:
        return 0.0
    count = sum(1 for lemma in lemmas if lemma in interesting_lemmas)
    return count / len(lemmas)

# --- Test the functions ---

# Load article HTML and extract text
with open(PICKLE_FILE, "rb") as f:
    article_html = pickle.load(f)
soup = BeautifulSoup(article_html, "html.parser")
text = soup.get_text()

# Load spaCy pipeline and process text
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Get sentences
sentences = list(doc.sents)
first_sentence = sentences[0].text if sentences else ""

# Get frequent tokens and lemmas from previous question
tokens = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]
token_freq = Counter(tokens)
most_common_tokens = [token for token, _ in token_freq.most_common(5)]

lemmas = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space
]
lemma_freq = Counter(lemmas)
most_common_lemmas = [lemma for lemma, _ in lemma_freq.most_common(5)]

# Score the first sentence
token_score = score_sentence_by_token(first_sentence, most_common_tokens)
lemma_score = score_sentence_by_lemma(first_sentence, most_common_lemmas)

print(f"First sentence: {first_sentence}")
print(f"Score by frequent tokens: {token_score}")
print(f"Score by frequent lemmas: {lemma_score}")

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

# Get sentences
sentences = list(doc.sents)

# Score each sentence
scores = [score_sentence_by_token(sent.text, most_common_tokens) for sent in sentences]

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=10, edgecolor='black')
plt.title("Histogram of Sentence Scores by Frequent Tokens")
plt.xlabel("Score")
plt.ylabel("Number of Sentences")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Most common range of scores appears to be 0.0–0.1 (most sentences
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

# Get sentences
sentences = list(doc.sents)

# Score each sentence by lemma
scores = [score_sentence_by_lemma(sent.text, most_common_lemmas) for sent in sentences]

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(scores, bins=10, edgecolor='black')
plt.title("Histogram of Sentence Scores by Frequent Lemmas")
plt.xlabel("Score")
plt.ylabel("Number of Sentences")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Most common range of scores appears to be 0.0–0.1 (most sentences
tokens = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space and token.pos_ == "NOUN"
]
lemmas = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct and not token.is_space and token.pos_ == "NOUN"
]
def plot_top_items(freq_dict, title, top_n=10, color="skyblue"):
    items = freq_dict.most_common(top_n)
    labels, values = zip(*items)
    
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color=color)
    plt.title(title)
    plt.xlabel("Tokens/Lemmas")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_top_items(token_freq, "Top 10 Tokens", color="skyblue")
plot_top_items(lemma_freq, "Top 10 Lemmas", color="teal")