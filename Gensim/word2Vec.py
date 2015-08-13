 # import modules & set up logging
import gensim
sentences = [['first', 'second'], ['one', 'two']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)
print model.most_similar(positive=['first', 'one'], negative=['second'], topn=1)