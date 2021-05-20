from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from .models import PositiveTraining,NegativeTraining,NeutralTraining

from myapp.models import *


import re


def img_replacer():
	# p = Positive()
	test_title = Article.objects.all()
	
	s_no =[]
	news =[]
	desp =[]
	artic =[]
	ur =[]
	img_ur =[]
	pub =[]


	for i in test_title:
		s_no.append(i.pk)
		news.append(i.title)
		desp.append(i.description,)
		artic.append(i.article)
		ur.append(i.url)
		img_ur.append(i.image_url)
		pub.append(i.pubDate)

	new_img_ur= []
	for i in img_ur:
		i = str(i)
		new_img_ur.append(re.sub("320","660",i))

	count = 0
	for i in new_img_ur:
		# r = Article.get_object_or_404
		# my_object = get_object_or_404(Article, pk=s_no[count])
		# my_object_copy = my_object
		my_object = get_object_or_404(Article, pk=s_no[count]).delete()
		my_object = Article(title = news[count],description= desp[count],article=artic[count],url=ur[count],image_url=new_img_ur[count],pubDate=pub[count])
		my_object.save()
		count +=1