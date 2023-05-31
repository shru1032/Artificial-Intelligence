#Tokenization
import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
text = "Technology is a constantly evolving and pervasive force that has transformed the way we
live and work. It encompasses a wide range of innovations and advancements, including
computers, software, internet, artificial intelligence, machine learning, robotics, and more.
Technology has revolutionized industries, communication, education, healthcare, transportation,
entertainment, and virtually every aspect of our daily lives. From smartphones and smart homes
to cloud computing and big data, technology has opened up new possibilities, improved efficiency,
and enhanced convenience. It has also spurred innovation, created new job opportunities, and
accelerated the pace of globalization. With its rapid evolution and impact on society, technology
continues to shape our world and drive change at an unprecedented pace, paving the way for a
future that is increasingly connected, intelligent, and digitally-driven."
words = word_tokenize(text)
sentences = sent_tokenize(text)
print("Tokenized words: ", words)
print("Tokenized sentences: ", sentences)

#Stopword Removal
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if not word.lower() in stop_words]
print("Filtered words: ", filtered_words)

#Stemming
from nltk.stem import PorterStemmer
porter = PorterStemmer()
stemmed_words_porter = [porter.stem(word) for word in words]
print("Porter stemmed words: ", stemmed_words_porter)

#Lemmatization
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words_wordnet = [lemmatizer.lemmatize(word) for word in words]
print("WordNet lemmatized words: ", lemmatized_words_wordnet)

#POS Tagging
#import nltk
from nltk.tokenize import word_tokenize
sentence = "I saw the man with the telescope"
grammar = nltk.CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> DT N | DT JJ N | PRP | NP PP
 VP -> V | V NP | VP PP | V S
 DT -> "the"
 N -> "man" | "telescope"
 JJ -> "with"
 V -> "saw"
 P -> "with"
 PRP -> "I"
 """)
words = word_tokenize(sentence)
parser = nltk.ChartParser(grammar)
trees = parser.parse(words)
for tree in trees:
 tree.pretty_print()
