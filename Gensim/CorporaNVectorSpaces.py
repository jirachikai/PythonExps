from gensim import corpora, models, similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
            for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] >1] for text in texts]

from pprint import pprint
pprint(texts)

dictionary = corpora.Dictionary(texts)
#dictionary.save("dictionary")
#print dictionary.token2id

new_doc = "human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
#print new_vec

corpus = [dictionary.doc2bow(text) for text in texts]

hdp = models.HdpModel(corpus,id2word=dictionary)
hdp.print_topics(topics=20, topn=10)


#
#lsi = models.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=3)
#corpus_lsi = lsi[corpus_tfidf]
#lsi.print_topics(2)
#
## similarity between two documents in lsi space
#doc = "Human computer interaction"
#vec_bow = dictionary.doc2bow(doc.lower().split())
#vec_lsi = lsi[vec_bow] # convert the query to LSI space
#print(vec_lsi)
#
#index = similarities.MatrixSimilarity(lsi[corpus])
#sims = index[vec_lsi]
#sims = sorted(enumerate(sims),key = lambda item:-item[1])
#print (sims)