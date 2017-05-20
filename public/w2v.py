import sys
import gensim
twit = []
with open('kumpulankatatwit.txt') as f:
	for a in f:
		twit.append(a.strip('\n'))
input_file = sys.argv[1]
model = gensim.models.Word2Vec.load("review_word2vec") 
if input_file in twit:
	print "Kata terdapat di Twitter"
else:
	print " "
try:
    hasil = model.similar_by_word(input_file, topn=10, restrict_vocab=None)
    for a in hasil:
		print str(a[0]) + ' (' + str(a[1]) + ')'
except KeyError, e:
    print "Pemetaan kata tidak ditemukan :)"
