# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect

from .forms import *
from django.db.models import Q
# from .models import Article, MyModel

from myapp.models import *
from django.utils import timezone
import operator

from .image_replacer import img_replacer

from .replacerTest import replaceTest
from .replacerTraining import replacers
from .user_input_classify_replacer import userReplace


from .tokenizationTest import tokenizeTest
from .tokenizationTraining import tokenize
from .user_input_tokenization import user_tokenise

from .naiveBayes import NaiveBayes
from .tf_idf_classifier import tf_idf
from .user_input_tfidf import user_tfidf



from .porter import PorterStemmer
import nltk
from functools import reduce

# Create your views here.

def article(request):

	return render(request,'myapp/index.html',{})

def article_list(request):
	# articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# articles = Article.objects.order_by('pubDate')
	articles = Article.objects.all()
	return render(request, 'myapp/index.html', {'articles':articles})




def test_list(request):
	tests = MyModel.objects.all()
	return render(request, 'myapp/test_list.html', {'tests':tests})


def tpositive_detail(request, pk):
	positive= tfidfPositiveClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(tfidfPositiveClassified, pk=pk)
	return render(request, 'myapp/tpositive.html', {'article':article, 'positive':positive})



def tnegative_detail(request, pk):
	negative= tfidfNegativeClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(tfidfNegativeClassified, pk=pk)
	return render(request, 'myapp/tnegative.html', {'article':article, 'negative':negative})



def tneutral_detail(request, pk):
	neutral= tfidfNeutralClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(tfidfNeutralClassified, pk=pk)
	return render(request, 'myapp/tneutral.html', {'article':article, 'neutral':neutral})
    # return render(request, 'myapp/article_detail.html', {'article':article})



def positive_detail(request, pk):
	positive= naivePositiveClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(naivePositiveClassified, pk=pk)
	return render(request, 'myapp/positive.html', {'article':article, 'positive':positive})



def negative_detail(request, pk):
	negative= naiveNegativeClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(naiveNegativeClassified, pk=pk)
	return render(request, 'myapp/negative.html', {'article':article, 'negative':negative})



def neutral_detail(request, pk):
	neutral= naiveNeutralClassified.objects.all().order_by('pubDate')
	article = get_object_or_404(naiveNeutralClassified, pk=pk)
	return render(request, 'myapp/neutral.html', {'article':article, 'neutral':neutral})
    # return render(request, 'myapp/article_detail.html', {'article':article})

   


def visualization(request):
	naivebayespos = NaiveCount.objects.values('positive').filter(pk=1)[0]['positive']
	naivebayesneg = NaiveCount.objects.values('negative').filter(pk=1)[0]['negative']
	naivebayesneu = NaiveCount.objects.values('neutral').filter(pk=1)[0]['neutral']

	tfidfpos = TfidfCount.objects.values('positive').filter(pk=1)[0]['positive']
	tfidfneg = TfidfCount.objects.values('negative').filter(pk=1)[0]['negative']
	tfidfneu = TfidfCount.objects.values('neutral').filter(pk=1)[0]['neutral']
	return render(request, 'myapp/visualization.html', {'naivebayespos':naivebayespos,'naivebayesneg':naivebayesneg,'naivebayesneu':naivebayesneu,'tfidfpos':tfidfpos,'tfidfneg':tfidfneg,'tfidfneu':tfidfneu,})


def sentiment(request):
	if request.method == "POST":
		form = ClassifiedTextForm(request.POST)
		if form.is_valid():
			classified = form.save(commit=False)
			classified.save()
			return redirect('classified_text', pk=classified.pk)
	else:
		form = ClassifiedTextForm()
		#form = ClassifiedTextForm()
		return render(request, 'myapp/sentiment.html', {'form':form})



def result(request, pk):

	
	search = get_object_or_404(Search, pk=pk)
	query = ""
	article = []
	text = search.text
	print(text)
	text = str(text)
	a = text.split()
	print(a)
	print(type(text))

	tpositive = tfidfPositiveClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))
	tnegative = tfidfNegativeClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))
	tneutral = tfidfNeutralClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))


	positive = naivePositiveClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))
	negative = naiveNegativeClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))
	neutral = naiveNeutralClassified.objects.filter(Q(title__contains=a)|reduce(operator.or_,(Q(title__contains=x) for x in a)))

	# tokens_text =[]
	# for i in text:
	# 	i = str(i)
	# 	tokens_pattern = r'\w+'
	# 	regex_wt = nltk.RegexpTokenizer(pattern= tokens_pattern, gaps= False)
	# 	tokens_text.append(regex_wt.tokenize(i))
	# print(tokens_text)


	

        

	# for item in a:
	# 	if item!=[]:
	# 		print(item)
	# 		print(type(item))
	# 		query=query+"Q(title__contains='"+item+"')|"
 #    	else:
 #    		query=query[:-1]
 #    		query=str(query)
 #    	print(query)
	# print(query)	

	# article = Article.objects.filter(query )
	return render(request, 'myapp/result.html', {'search':search,'tnegative':tnegative,'tpositive':tpositive,'tneutral':tneutral, 'negative':negative, 'positive':positive, 'neutral':neutral})


def classified_text(request, pk):
	classified = get_object_or_404(ClassifiedText, pk=pk)

	a= classified.text
	print(a)
	replacer_result = userReplace(a)
	print("hi")
	print(replacer_result)
	tokenise_result = user_tokenise(replacer_result)
	print("oh ho")
	print(tokenise_result)
	tfidf_result = user_tfidf(tokenise_result,a)
	print("aah ha")
	print(tfidf_result)
	b={"Result":tfidf_result}
	Sentiment = tfidf_result[0]
	Positiveness = tfidf_result[1]
	Negativeness = tfidf_result[2]
	Neutralness = tfidf_result[3]





	text=ClassifiedText.objects.all()
	return render(request, 'myapp/textclassified.html', {'classified':classified, 'text':text,'Sentiment':Sentiment,'Positiveness':Positiveness,'Negativeness':Negativeness,'Neutralness':Neutralness})

def training_news(request):
	# positive_news = Positive.objects.all()
	# negative_news = Negative.objects.all()
	# neutral_news = NeutralTraining.objects.all()
	
	return HttpResponse("lets begin")

def index(request):
	img_replacer()
	# replacers()
	replaceTest()


	tokenizeTest()
	# tokenize()
	
	naivebayes = NaiveBayes()

	test = []
	test_verb = stemmedVerbTestNews.objects.all()
	test_title =Article.objects.all()
	for i in test_verb:
		test.append(i.stemmedVerb)
	
	positive_news = []
	negative_news = []
	neutral_news = []

	positive_title = stemmedVerbPositiveTraining.objects.all()
	for i in positive_title:
		positive_news.append(i.stemmedVerb)


	negative_title = stemmedVerbNegativeTraining.objects.all()
	for i in negative_title:
		negative_news.append(i.stemmedVerb)

	neutral_title = stemmedVerbNeutralTraining.objects.all()
	for i in neutral_title:
		neutral_news.append(i.stemmedVerb)

	naivebayes.testing(test,test_title)
	naivebayes.train(positive_news,negative_news,neutral_news)

	positive = naivePositiveClassified.objects.all().order_by('pubDate')

	negative = naiveNegativeClassified.objects.all().order_by('pubDate')
	neutral = naiveNeutralClassified.objects.all().order_by('pubDate')

	tf_idf()



	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.save(commit=False)
			search.save()
			return redirect('result', pk=search.pk)
	else:
		form = SearchForm()
		return render(request, 'myapp/index.html', {'form':form, 'positive':positive, 'negative':negative, 'neutral':neutral})
   
	
	# for i in positive_title:
	# 	positive_news.append(i.title)
    # naivebayes.testing("test_verbs.csv","test_data.csv")
    # naivebayes.testing(test_title)
    # naivebayes.train(positive_title,negative_title,neutral_title)

    
        
	
	# if request.method == "POST":
	# 	form = SearchForm(request.POST)
	# 	if form.is_valid():
	# 		search = form.save(commit=False)
	# 		search.save()
	# 		return redirect('result', pk=search.pk)
	# else:
	# 	form = SearchForm()
	# 	return render(request, 'myapp/index.html', {'form':form, 'positive':positive, 'negative':negative, 'neutral':neutral})

	
	# return render(request,'myapp/index.html',{'positive':positive, 'negative':negative, 'neutral':neutral})

