# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from jsonfield import JSONField
from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200, null=False)
	description = models.CharField(max_length=200, null=False)
	article = models.TextField(null=False)
	url = models.URLField(null = False)
	image_url = models.URLField(null = False)
	pubDate = models.CharField(max_length=20)
	# published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	

class Feed(models.Model):
	site = models.CharField(max_length=100, null=True)
	title = models.CharField(max_length=200,null=True)
	description = models.TextField(null=True)
	url = models.CharField(max_length=200, null=True)
	pubDate = models.CharField(max_length=200, null=True)
 


	def __str__(self):
		return self.title

class TestField(models.Model):
	name = models.CharField(max_length=35)


class MyModel(models.Model):
	title = models.CharField(max_length=200)
	json = JSONField()

	def __str__(self):
		return self.title


class PositiveTraining(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)

    # def __str__(self):
    #     return str(self.s_no)+" " + self.title

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)

 
class NegativeTraining(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)


 
class NeutralTraining(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class stemmedVerbPositiveTraining(models.Model):
    # news_type = models.ForeignKey(newsType,on_delete=models.CASCADE,null =True)  
    # positive = models.ForeignKey(PositiveTraining,on_delete=models.CASCADE,null =True)
    s_no = models.IntegerField(default = 0,unique = True)  
    stemmedVerb = models.CharField(max_length=500)
    
    def __str__(self):
        return self.stemmedVerb
        
class stemmedVerbNegativeTraining(models.Model):
    # news_type = models.ForeignKey(newsType,on_delete=models.CASCADE,null =True)  
    # news_class = models.ForeignKey(newsClass,on_delete=models.CASCADE,null =True)  
    # negative = models.ForeignKey(NegativeTraining,on_delete=models.CASCADE,null =True)  
    s_no = models.IntegerField(default = 0,unique =True)
    stemmedVerb = models.CharField(max_length=500)
    
    def __str__(self):
        return self.stemmedVerb

class stemmedVerbNeutralTraining(models.Model):
    # news_type = models.ForeignKey(newsType,on_delete=models.CASCADE,null =True)  
    # news_class = models.ForeignKey(newsClass,on_delete=models.CASCADE,null =True)  
    # neutral = models.ForeignKey(NeutralTraining,on_delete=models.CASCADE,null =True)  
    s_no = models.IntegerField(default = 0,unique =True)
    stemmedVerb = models.CharField(max_length=500)
    
    def __str__(self):
        return self.stemmedVerb


class testNews(models.Model):
    s_no = models.IntegerField(default = 0,unique= False)
    title = models.CharField(max_length=255,null = True)
    # article = models.ForeignKey(Article,on_delete=models.CASCADE,null =True)  
    
    # def save(self, *args, **kwargs):
    #     try:
    #         self.article
    #     except:
    #         self.article = Article.objects.first()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)



class stemmedVerbTestNews(models.Model):
    # news_type = models.ForeignKey(newsType,on_delete=models.CASCADE,null =True)  
    # news_class = models.ForeignKey(newsClass,on_delete=models.CASCADE,null =True)  
    # neutral = models.ForeignKey(NeutralTraining,on_delete=models.CASCADE,null =True)  
    s_no = models.IntegerField(default = 0,unique =True)
    # title = models.ForeignKey(testNews,on_delete=models.CASCADE,null =True)
    stemmedVerb = models.CharField(max_length=500)

    def __str__(self):
    	return self.stemmedVerb

# class newsType(models.Model):
#     sentiment = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title



# class classifiedNews(models.Model):
#     news_type = models.ForeignKey(newsType,on_delete=models.CASCADE,null =True)  
#     article = models.ForeignKey(Article,on_delete=models.CASCADE,null =True)  
   
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
    
class naivePositiveClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    

    # def __str__(self):
    #     return str(self.s_no)+" " + self.title

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)

 
class naiveNegativeClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.title

    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)


 
class naiveNeutralClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title

class tfidfPositiveClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    

    # def __str__(self):
    #     return str(self.s_no)+" " + self.title

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)

 


class tfidfNegativeClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.title

    # def __str__(self):
    #     return "{0} {1}".format(self.s_no, self.title)


 
class tfidfNeutralClassified(models.Model):
    s_no = models.IntegerField(default = 0,unique =True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200, null=False)
    article = models.TextField(null=False)
    url = models.URLField(null = False)
    image_url = models.URLField(null = False)
    pubDate = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title




class NaiveCount(models.Model):
    positive = models.IntegerField()
    negative = models.IntegerField()
    neutral = models.IntegerField()


class TfidfCount(models.Model):
    positive = models.IntegerField()
    negative = models.IntegerField()
    neutral = models.IntegerField()

class Search(models.Model):
    text=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ClassifiedText(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title