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
