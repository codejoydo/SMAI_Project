import ujson
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import sys

def eprint(msg):
    sys.stderr.write(msg)

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
#p_stemmer = PorterStemmer()

eprint("loading corpus ...\n")

with open('data.json') as data_file:
	data = ujson.load(data_file)

doc_set = []

for key in data.keys():
	for itemkey in data[key].keys():
		doc_content_list = []
		for item in data[key][u'captions']:
			doc_content_list.append(item)
		for item in data[key][u'text']:
			doc_content_list.append(item)
		doc_set.append(' '.join(doc_content_list))

#texts = []

eprint("processing documents ...\n")

for i in doc_set:
	raw = i.lower()
	#tokens = tokenizer.tokenize(raw)
	#stopped_tokens = [i for i in tokens if not i in en_stop]
	#stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
	#texts.append(stemmed_tokens)
	#texts.append(stopped_tokens)

eprint("creating dictionary ...\n")

with open('dictnet_vgg_labels.txt') as data_file:
	dict_data = data_file.readlines()
dict_data = [[unicode(item.strip(),"utf-8")] for item in dict_data]
print type(dict_data),len(dict_data)
#print dict_data[0]

dictionary = corpora.Dictionary(dict_data)
print type(dictionary), "words in dictionary"
print dictionary

eprint("generating corpus in bow format ...\n")

corpus = [dictionary.doc2bow(text) for text in texts]

eprint("generating LDA model ...\n")

lda = gensim.models.ldamodel.LdaModel(corpus, num_topics=10)

eprint("generating topic distribution for documents ...\n")

for document in corpus:
	print lda[document]

eprint("done\n")