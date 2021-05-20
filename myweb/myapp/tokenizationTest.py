from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from .models import PositiveTraining,NegativeTraining,NeutralTraining
# from .models import tokenisePositiveTraining,tokeniseNegativeTraining,tokeniseNeutralTraining
# from .models import stemmedVerbNeutralTraining,stemmedVerbPositiveTraining,stemmedVerbNegativeTraining
from myapp.models import *


import re

import nltk
from nltk.corpus import stopwords
from .porter import PorterStemmer

eng_stop = set(stopwords.words('english'))



def tokenizeTest():
	test_title = testNews.objects.all()
	# s_n = []
	# for i in positive_title:
	# 	s_n.append(i.s_no)
	# positive_s_no = Positive.objects.only("s_no")
	
	
	#sentiment = positive/ negative/ neutral news
	#tokeniseSentiment = tokenised positive/ negative/ neutral news
	def tokenised(news):
		tokenised_news =[]
		bag_of_verb = []
		bag_of_words_without_stopwords =[]
	# bag_of_positive_verb = []
		bag_of_stemmed_verb = []
		bag_of_distinct_stemmed_verb = []

		smallCase_tokenised_news = []
		Utagged_words = []
	# news = str(news)
	# news = re.sub(r'\d+','', news) #remove digits in news title
	# token_pattern = r'\w+'
	# pattern = r"[?|.|,|']"
	# pattern = r"[?|.|,|'|;|:|{|}|-|(|)|&|%|$|!|\|/|]"
	# news = re.sub(token_pattern,'',news)
	# news.split()

	# print(news.split())
	

	# small w represent [a-zA-Z0-9 _ ]
	
	
	# regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False)
	# news = list(news)
	# print(type(news))
		s_n = []
		# t_title =[]
		for i in news:
			s_n.append(i.s_no)
			# t_title.append(i.title)
		count =0
		for i in news:
		# x=0
		# print(i[x])
			i = str(i)
	# 	if i.lower() not in eng_stop:
	# 		smallCase_tokenised_news.append(i.lower())
	# 	# x = x+1
	
	# for i in smallCase_tokenised_news:
	# 	# print(i[0])
	# 	i = str(i)s

			i = re.sub(r'\d+','',i.lower()) #remove digits in news title
			token_pattern = r'\w+'
			regex_wt = nltk.RegexpTokenizer(pattern = token_pattern)# #haven't==havent
			
			# title = sentimentTraining.objects.get(s_no = s_n[count])
			# neutral,negative,positive  = title chuta chutai leknu parxa
			# so test data ko garda hos garnu
			# t = tokeniseSentiment(neutral=title,s_no=s_n[count],lowerTokenisedWord=regex_wt.tokenize(i))
			# t.save()

			tokenised_news.append(regex_wt.tokenize(i))
			count +=1

	# smallCase_tokenised_positive_news = tokenised(positive_title,PositiveTraining,tokenisePositiveTraining)
	# smallCase_tokenised_negative_news = tokenised(negative_title,NegativeTraining,tokeniseNegativeTraining)
	# smallCase_tokenised_neutral_news  = tokenised(neutral_title,NeutralTraining,tokeniseNeutralTraining)


		# if tokenised_news not in eng_stop:
		# 	smallCase_tokenised_news.append(tokenised_news)
	# print(tokenised_news)
	# x = 0
	# tokenised_news =str(tokenised_news)

	# to remove stopwords
		for i in tokenised_news:
	# 	words_without_stopwords =[]
	# 	x= 0
	# 	while x<len(i):
	# 		if i[x] not in eng_stop:
	# 			words_without_stopwords.append(i[x])
	# 		x +=1
	# 	bag_of_words_without_stopwords.append(words_without_stopwords)

	# for i in bag_of_words_without_stopwords:
	# 	if i not in eng_stop:
	# 		smallCase_tokenised_news.append(i)
	# print(smallCase_tokenised_news)
	

			Utagged_words.append(nltk.pos_tag(i,tagset = 'universal'))
		# print(Utagged_words)
		# if Utagged_words[1]=="ADJ" and i[1]=="ADV" and i[1]=="VERB":
		# 	print(i)
		# 	# bag_of_verb.append(i)
		# 	bag_of_verb.append(i[0])
		# x = x +1 
		# if x >10:
		# 	break
	# print(Utagged_words)
	# a =0
	# dic ={}
	# list_of_list = []
	


		p1 = PorterStemmer()
		
		for i in Utagged_words:
			words_without_stopwords =[]
			x= 0
			while x<len(i):
				if i[x] not in eng_stop:
					words_without_stopwords.append(i[x])
				x +=1
			bag_of_words_without_stopwords.append(words_without_stopwords)




		for i in bag_of_words_without_stopwords:
		# print(i)
			# verbs_of_each_headline = []
			stemmed_verbs_of_each_headline =[]
		#print(i)
			x= 0
			while x<len(i):
			# if i[x][1] not in eng_stop:
			# 	smallCase_tokenised_news.append(i)
				if (i[x][1])=="VERB" or i[x][1]=="ADV" or i[x][1]=="ADJ":
					# verbs_of_each_headline.append(i[x][0])
					stemmed_verbs_of_each_headline.append(p1.stem(i[x][0],0,len(i[x][0])-1))
		# 		print(i[x][0])
		# 		# dic[a] += i[x][0]

				x +=1
					# no verbs and adverb,so empty 
			if stemmed_verbs_of_each_headline == []:
				stemmed_verbs_of_each_headline.append("cannot be classified")
				# continue


			# bag_of_verb.append(verbs_of_each_headline)
			bag_of_stemmed_verb.append(stemmed_verbs_of_each_headline)

			# title = sentimentTraining.objects.get(s_no = s_n[count])
			# neutral,negative,positive  = title chuta chutai leknu parxa
			# so test data ko garda hos garnu
			# t = stemmedVerbSentimentTraining(s_no=s_n[count],stemmedVerb=stemmed_verbs_of_each_headline)
			# t.save()
			# count +=1


	# smallCase_tokenised_positive_news = tokenised(positive_title,PositiveTraining,stemmedVerbPositiveTraining)
	# smallCase_tokenised_negative_news = tokenised(negative_title,NegativeTraining,stemmedVerbNegativeTraining)
	# smallCase_tokenised_neutral_news  = tokenised(neutral_title,NeutralTraining,stemmedVerbNeutralTraining)


	
	
	# print(bag_of_verb)
	# print("\n")
	# print(bag_of_stemmed_verb)

	# print("\n---------Tokenised verbs and adverbs of",sentiment," news after removing stopword and stemming")
	
		# for i in bag_of_stemmed_verb:
		# # if i == []:
		# # 	continue
		# # print(i)
		# 	if i not in bag_of_distinct_stemmed_verb:
		# 		bag_of_distinct_stemmed_verb.append(i)

	# bag_of_distinct_stemmed_verb = str(bag_of_distinct_stemmed_verb
	# print(", ".join(bag_of_distinct_stemmed_verb))

	# print(",".join( repr(i) for i in bag_of_distinct_stemmed_verb))
	# i = 1
		a = []
		
		for i in bag_of_stemmed_verb:
		# i = str(i)
			a.append(",".join( str(x) for x in i))
			# t = stemmedVerbSentimentTraining(s_no=s_n[count],stemmedVerb = (",".join( str(x) for x in i)))
			# t.save()
		count = 0

		print("stemmed verb")	
		for i in a:
			# print(i)
			s = stemmedVerbTestNews(s_no= s_n[count],stemmedVerb = i)
			s.save()
			count +=1



		# print(",".join(i))
		# print(i)



	# 	i.replace('[','').replace(']','')
	# # 	# i = re.sub(r'[']', r'', sentence)
	# 	i = i + 1
	# 	if i > 10:
	# 		break

	# print("Number of stemmed",sentiment," headlines :", len(bag_of_stemmed_verb))
	# print("Number of distinct stemmed",sentiment," headlines :", len(bag_of_distinct_stemmed_verb))


	# print("k ho para")
	# # return smallCase_tokenised_news
	# return bag_of_stemmed_verb
	# print("Tait..teri matuk ne")
	stemmed_test_news = stemmedVerbTestNews.objects.all()
	if len(stemmed_test_news) == 0:
		smallCase_tokenised_test_news = tokenised(test_title)
	
	