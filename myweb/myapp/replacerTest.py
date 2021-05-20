from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from .models import PositiveTraining,NegativeTraining,NeutralTraining

from myapp.models import *


import re


def replaceTest():
	# p = Positive()
	test_title = Article.objects.all()
	# s_n = []
	# for i in positive_title:
	# 	s_n.append(i.s_no)
	# positive_s_no = Positive.objects.only("s_no")
	
	# negative_title = NegativeTraining.objects.all()
	# neutral_title = NeutralTraining.objects.all()
	def replace(news_list):
		# news_list = list(news_list)
		replacement_patterns = [
		(r'isn\'t', 'is not'),
		(r'wasn\'t', 'was not'),
		(r'weren\'t', 'were not'),
		(r'aren\'t', 'are not'),

		(r'hasn\'t', 'has not'),
		(r'haven\'t', 'have not'),
		(r'hadn\'t','had not'),

		(r'won\'t', 'will not'),
		(r'can\'t', 'cannot'),
		(r'wouldn\'t','would not'),
		(r'shouldn\'t', 'should not'),
		(r'mustn\'t','mustnot'),
		(r'couldn\'t', 'could not'),


		(r'don\'t', 'do not'),
		(r'doesn\'t', 'does not'),
		(r'didn\'t','did not'),

		(r'needn\'t', 'need not'),
		(r'mightn\'t', 'might not'),
		(r'daren\'t','dare not'),
		]

		patterns = [(re.compile(regex), repl) for (regex, repl) in replacement_patterns]
		# s_n = []
		# for i in news_list:
		# 	s_n.append(i.id)
	
		


		count = 0
		if len(testNews.objects.all())==0:
			for i in news_list:
			# print(i)

				i = str(i) 
				result = i
				r = testNews(s_no = count,title =result)
				r.save()
				count +=1
				

			# for (pattern, repl) in patterns:

				# print("I will fixed it!")

				# if re.search(pattern,i):
				# 	result = (re.sub(pattern, repl, i))
				# 	# news_list.pop(count)
				# 	# tokenised_news_after_replacer.append(result)
				# 	# news_list.title = result
				# 	# r = testNews.objects.filter(s_no=s_n[count]).delete()
				# 	r = testNews(s_no = count,title =result)
				# 	r.save()
				# 	break #after finding requried pattern out of loop #kada
				# else:
				# 	result = i
				# 	r = testNews(s_no = count,title =result)
				# 	r.save()
				# 	break
					
					# tokenised_news_after_replacer.append(result)
			 
		else:
			test_news = testNews()
			test_news = testNews.objects.all()
			s_n = []
			for i in test_news:
				s_n.append(i.s_no)
		
		test_news = testNews.objects.all()
			
		count = 0
		for i in test_news:
			# print(i)

			i = str(i) 	
			for (pattern, repl) in patterns:

				# print("I will fixed it!")

				if re.search(pattern,i):
					result = (re.sub(pattern, repl, i))
					# news_list.pop(count)
					# tokenised_news_after_replacer.append(result)
					# news_list.title = result
					r = testNews.objects.filter(s_no=s_n[count]).delete()
					r = testNews(s_no = s_n[count],title =result)
					r.save()
					break #after finding requried pattern out of loop #kada
				# else:
				# 	result = i
				# 	r = testNews(s_no = count,title =result)
				# 	r.save()
				# 	break
					
					# tokenised_news_after_replacer.append(result)
			count +=1 
		
			

		# for i in news_list:
		# 	print(i)
		# for i in tokenised_news_after_replacer:
			# print(i)
		# print("sure u did it!")
		# print("No of  news ",len(news_list))
		# print("No of news after replacer function",len(tokenised_news_after_replacer))
		# return(news_list)

	test_news_after_replacer = replace(test_title)
	