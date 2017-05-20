# from pyspark import SparkContext, SparkConf
# from pyspark.sql import SQLContext, Row
# from pyspark.ml.feature import HashingTF, IDF, Tokenizer
# from pyspark.ml.feature import StringIndexer, VectorIndexer
# from pyspark.ml.classification import NaiveBayes
# from pyspark.mllib.regression import LabeledPoint
# from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
# from pyspark.mllib.linalg import Vectors
# from pyspark.mllib.util import MLUtils
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import sys
import csv
import re
import string
import nltk
import preprocessor as p
import tweepy #https://github.com/tweepy/tweepy
import csv
import os

#Twitter API credentials
consumer_key = "tU7YSCsf8goc3JX83tEZs9BHu"
consumer_secret = "Q6vH7bytmT0QDRvjf3Q11mcdkwAsYOXlL1BmaDbub1wFqJ0jB8"
access_key = "71742290-2lBYzAj5uH9V6Mdp9j7qAtZFrcwKgvnRORxv2OKOC"
access_secret = "1HhkvayxMacRKGda1cDnyLbshtZjS1eh5rtaINdXjZ62K"

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0 and len(alltweets) < 200:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('tweet.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

input_file = sys.argv[1]

if __name__ == '__main__':
	get_all_tweets(input_file)

#########################################

stemmer = PorterStemmer()
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION, p.OPT.SMILEY, p.OPT.NUMBER, p.OPT.RESERVED)
printable = set(string.printable)
cachedStopWords = stopwords.words("english")
apos = {"amp" : "", "'ll" : " will", "'m" : " am", "won't" : "will not", "'s" : " is", "'re" : " are", "'ve" : " have", "w/" : "with"}
i = 0
with open('tweet.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		tweet = row['text']
		tweet = re.sub(r"http\S+", "", tweet).translate(None, ':.!$?();&|-,"*+#')
		tweet = p.clean(tweet)
		tweet = filter(lambda x: x in printable, tweet)
		tweet = " ".join(re.findall('[A-Z][^A-Z]*', tweet)).lower()
		for word in apos:
			tweet = tweet.replace(word, apos.get(word))
		tweet = re.sub(r"'", "", tweet)
		tweet = re.sub(r"/", " ", tweet)
		tweet = re.sub(r'\d+', '', tweet)
		tweet = ' '.join([word for word in tweet.split() if word not in cachedStopWords and len(word) > 2])
		tweet = ' '.join([stemmer.stem(word) for word in tweet.split()])
		if len(tweet.split())>10:
			with open("tweet.txt", "a") as file:
				file.write("{}\n".format(str(tweet)))

# os.system("hdfs dfs -put tweet.txt")

# conf = SparkConf().setAppName('Twitter Classification')
# sc = SparkContext(conf=conf)
# sqlContext = SQLContext(sc)

# tweet = sc.textFile("tweet.txt")
# tweetRDD = tweet.map(lambda p: Row(tweet=p, label=float(-1)))
# tweetDF = sqlContext.createDataFrame(tweetRDD)
# tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
# wordsData = tokenizer.transform(tweetDF)
# hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="rawFeatures")
# featurizedData = hashingTF.transform(wordsData)
# idf = IDF(inputCol="rawFeatures", outputCol="features")
# idfModel = idf.fit(featurizedData)
# rescaledData = idfModel.transform(featurizedData)
# labeled = rescaledData.map(lambda row: LabeledPoint(row.label, row.features))

# model = NaiveBayesModel.load(sc, "model_akurasi_x")
# prediction = labeled.map(lambda p: (model.predict(p.features)))
# prediction = predictionAndLabel.filter(lambda (x, v): x == v).count() / testData.count()
# print accuracy







