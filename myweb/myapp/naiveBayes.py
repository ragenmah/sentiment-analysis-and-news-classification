from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from .models import PositiveTraining,NegativeTraining,NeutralTraining
# from .models import tokenisePositiveTraining,tokeniseNegativeTraining,tokeniseNeutralTraining
# from .models import stemmedVerbNeutralTraining,stemmedVerbPositiveTraining,stemmedVerbNegativeTraining


from myapp.models import *


import re

import nltk
# import pandas as pd
import csv


class NaiveBayes:
    positive_count = 0
    negative_count = 0
    neutral_count  = 0
    total_count = 0

    po_list = []       	#un = po
    ne_list = []		#ow = ne
    nu_list = []		#n = nu
    total_list = []

    poHash = {}
    neHash = {}
    nuHash={}

    total_positive_words = 0
    total_negative_words = 0
    total_neutral_words = 0
    unique_words = 0

    prior_positive = 0
    prior_negative = 0
    prior_neutral = 0
    # test_data = ['nepal','nepal','nepal','tokyo','japan']
    test_data = []
    test_news = []
    # test_data = [[],['moscow','bangal','hongkong'],['nepal','nepal','nepal','tokyo','japan'],['india'],['why','so','serious'],['i','love','u'
    # ]]
    likelihood = {}
    # positive_conditional_probability = {}
    # negative_conditional_probability = {}
    # neutral_conditional_probability  =  {}

    positive_likelihood = {}
    negative_likelihood = {}
    neutral_likelihood  = {}
# 
    positive_likelihood = []
    negative_likelihood = []
    neutral_likelihood  = []

    positive_news = []
    negative_news = []
    neutral_news  = []
    error_data =    []
    # test_data = ['japan']
    
    def testing(self,verb,title):
            test_data1 = list(verb) #test_data = test verbs of test new

            for i in test_data1:
                print(i)

                i = str(i)
                token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
                regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
                token = regex_wt.tokenize(i)   #tokens ---list objec
                self.test_data.append(token)
                # print(self.test_data)
        

            self.test_news = list(title) #test_news = full news article headlines
            print("ok")
              
            for i in self.test_data:
                print(i)
            print("\n-----------------------------------------")
            print("\n-----------------------------------------")
          
            for i in self.test_news:
                print(i)
            # self.test_article = list(article) #test_news = full news headlines
            
            # print(self.test_data)




    def __init__(self):
        pass
    
    def train(self,po,ne,nu):

        self.po_list = po
        # print(self.po_list)
        # for i in self.po_list:
        #         print(i)
        print("\n-----------------------------------------")
        print("\n-----------------------------------------")
        count =0
        for i in self.po_list:
                count +=1
        self.positive_count = count
        
            
        # self.positive_count = len(self.po_list)
        
        print("count po:",self.positive_count)

        
            
            
        self.ne_list = ne

        count =0
        for i in self.ne_list:
                count +=1
        self.negative_count = count
        


        # self.negative_count = len(self.ne_list)
        print("count neg:",self.negative_count)


        # for i in self.ne_list:
        #         print(i)
        # print("\n-----------------------------------------")
        # print("\n-----------------------------------------")
        

        self.nu_list = nu
        self.neutral_count = len(self.nu_list)
        print("count ne:",self.neutral_count)

        # for i in self.nu_list:
        #         print(i)
        # print("\n-----------------------------------------")
        # print("\n-----------------------------------------")
        

        

        
        print("--------------- Training data :\n")
        
        self.total_count = self.positive_count+self.negative_count+self.neutral_count
        print(self.total_count)
        # print("\n-----------------------------------------")
        # print("\n-----------------------------------------")
       
            # print("Prior Probabilities: \n")
        self.prior_neutral = self.neutral_count/self.total_count
        self.prior_positive = self.positive_count/self.total_count
        self.prior_negative = self.negative_count/self.total_count

        print("\n\nPrior=================)")   
        # print(self.total_count)
        # print(self.prior_positive)
        # print(self.po_list)

        print("pri po  :",self.prior_positive)
        print("pri neg  :",self.prior_negative)
        print("pri neu  :",self.prior_neutral)
       
        

            # print(self.total_count)
        self.total_list = self.po_list + self.ne_list+ self.nu_list
        # print(self.total_list)
        self.poHash =self.generateHash(self.po_list,1)
        print("\n--------------------")
        # for i in self.poHash:
        # print(self.poHash)
       
            # print("ok")
        # print(self.poHash)
        self.neHash =self.generateHash(self.ne_list,-1)
        # print("\n--------------------")
        # for i in self.neHash:
        #     print(self.neHash)
        
        # print(self.neHash)
        self.nuHash =self.generateHash(self.nu_list,0)
        # print("\n--------------------")
        # for i in self.nuHash:
        #     print(self.nuHash)
        
        # print(self.nuHash)
            
        self.unique_words = self.total_distinct_word(self.nuHash,self.neHash,self.poHash)


        print("Total number of positive words : ",self.total_positive_words)
        print("\nTotal number of negative words : ",self.total_negative_words)
        print("\nTotal number of neutral words : ",self.total_neutral_words)
        print("\nTotal number of distinct words : ",self.unique_words)
           

        self.positive_conditional_probability = self.find_conditional_probability(self.poHash,self.test_data,self.total_positive_words)
        self.negative_conditional_probability = self.find_conditional_probability(self.neHash,self.test_data,self.total_negative_words)
        self.neutral_conditional_probability = self.find_conditional_probability(self.nuHash,self.test_data,self.total_neutral_words)

        self.test(self.test_data)

        self.classify(self.test_data,self.test_news,self.positive_likelihood,self.negative_likelihood,self.neutral_likelihood)

         

   
        #to find total number distinct words in training data
    def total_distinct_word(self,dict1,dict2,dict3):
        # dict1,dict2,dict3 = self.adjustValue(dict1,dict2,dict3)
        # total_dic = {}
        distinct_word = []
        for i in dict1:
            if i not in distinct_word:
                distinct_word += [i]
            
        for j in dict2:
            if j not in distinct_word:
                distinct_word += [j]
            
        for k in dict3:
            if k not in distinct_word:
                distinct_word += [k]
        result = len(distinct_word) 
        # print(distinct_word)
        return result


    # def generateHash(self,word_list):
    #     word_frequencies = []
    #     unique_words = []
    #     dict_unique_word = {}

    #     for x in word_list:
    #       if x not in unique_words:
    #           unique_words += [x]

    #     for x in unique_words:
    #       word_frequencies += str(word_list.count(x))
    #       print(word_frequencies)

    #     print("\n")
    #     dist_word = len(unique_words)
    #     # unique_words = str(unique_words)
    #     print(type(unique_words))
    #     print("i am here")
    #     print(len(unique_words))
    #     print(unique_words)
    #     for i in range(dist_word):

    #         print("\nlets watch here")
    #         dict_unique_word[unique_words[i]] = word_frequencies[i]
            

    #     print("\n now daam here")
    #     print(dict_unique_word)   
    #     return dict_unique_word 


# to count number of words in document
    def generateHash(self,lists,number):
        dic = {}
        new_list = []
        for i in lists:
            new_list +=[i]
        # print(new_list)
        # new = {}
        # new = dict(lists)

        lists = str(lists)
        token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
        regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
        tokens = regex_wt.tokenize(lists)    #tokens ---list objec
        print ("\n")
        # for token in tokens:
        #     print(token)
        if number is 1:
            self.total_positive_words = len(tokens)
        elif number is -1:
            self.total_negative_words =len(tokens)
        else:
            self.total_neutral_words =len(tokens)


        # print("total number of words: ",len(tokens))
        # to count number of  distinct  that words in each positive, negative, neutral news( training data)
        for x in tokens:
            if x not in  dic:
                dic[x] = 1
            else:
                dic[x] +=1  
        
        return dic



    #dict = count of words in positive or negative or neutral training data   
    #data = testdata
    #total_words = total-- positive or negative or neutral words
    def find_conditional_probability(self,dict,data,total_words):
        conditional_probability_dict = {}
        dic = {}
        conditional_probability = 0

        # for i in data:
        #     if i not in dic:
        #         dic[i] = 1
        #     else:
        #         dic[i] += 1
        # print(data[1])
        print(type(data))
       
        for x in data:
            # print(x)
            x = str(x)
            token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
            regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
            tokens = regex_wt.tokenize(x)    #tokens ---list objec
            # print(tokens)
        

            # if (x == positive_conditional_probability.key()):
            # x =list(x)
            # print(type(data))
            # x = str(x)
            # x.split()
            for i in tokens:
                # print(x[0])
                for y in dict:
                    if i == y :
                        # print("uffff....")
                        conditional_probability_dict[i] = (dict[y] + 1)/(total_words + self.unique_words)
                        break    #yo break dherai kadha ho
                    else:
                        # print("come on man!!!")
                        conditional_probability_dict[i] = 1/(total_words + self.unique_words)

        
        print("hello rice killer\n")
        print(conditional_probability_dict)
        return conditional_probability_dict


    #function to process test data
    def test(self,data):
        dic = {}
        # conditional_probability = 1
        score = {}
        # print(data[1])
        i = 0

        # for x in data1:
        #     # print(x)
        #     x = str(x)
        #     token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
        #     regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
        #     data = regex_wt.tokenize(x)    #tokens ---list objec
        
        for i  in range(len(data)):

            # to calculate likelihood and store in respective dictionary
           # self.positive_likelihood.append(self.calculate_likelihood(data[i],self.positive_conditional_probability,"positive"))
           print("--------------")
           # data[i] = str(x)
           # token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
           # regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
           # tokens = regex_wt.tokenize(x)    #tokens ---list objec
           

           print(data[i])
           self.positive_likelihood.append(self.calculate_likelihood(data[i],self.positive_conditional_probability,"positive"))
           
           self.negative_likelihood.append(self.calculate_likelihood(data[i],self.negative_conditional_probability,"negative"))
           self.neutral_likelihood.append(self.calculate_likelihood(data[i],self.neutral_conditional_probability,"neutral"))
           i = i + 1

           # self.positive_likelihood[i] = self.calculate_likelihood(data[i],self.positive_conditional_probability,"positive")
           # self.negative_likelihood[i] = self.calculate_likelihood(data[i],self.negative_conditional_probability,"negative")
           # self.neutral_likelihood[i]  = self.calculate_likelihood(data[i],self.neutral_conditional_probability,"neutral")
        

           # data = one list of testData
           # passed_conditional_probability = positive, negative neutral --- conditional probability
           # sentiment = positive , negative, neutral word
    def calculate_likelihood(self,data,passed_conditional_probability,sentiment):
        conditional_probability = 1
        dic = {}
        for i in data:
            if i not in dic: #dic = count of each unique word
                dic[i] = 1
            else:
                dic[i] += 1
        # print(dic)
        # print("oi rice killer")
        # # print(self.positive_conditional_probability) \


        for x in dic:
            # print(x)
            # if (x == positive_conditional_probability.key()):
            for y in passed_conditional_probability:
                if x == y :
                    # print("uffff....")
                    # print(positive_conditional_probability[y])
                    conditional_probability *= (passed_conditional_probability[y]**dic[x])
                    
                    #  print("::::::::::::::::;",conditional_probability)
            conditional_probability *= 10000
        # conditional_probability *= 10000  #value of conditional_probability is very small so , multiplied by 1000
        # print("\nhey bhagawan")
        # print("Conditional Probability : ", conditional_probability)

        likelihood_probability = conditional_probability * self.prior_positive
        # print("\n")
        # print(sentiment)
        # print("likelihood probability : ",likelihood_probability)
        # print("\nohoooo...hait")
        return likelihood_probability

        #to caculate likelihood of each news and news classification
        #testData = collection of verbs of newsheadline
        # testNews = collection of news headlines

    def classify(self,testData,testNews,positive_likelihood,negative_likelihood,neutral_likelihood):
        # print("Positive_likelihood : ",positive_likelihood)
        # print("\nNegative_likelihood : ",negative_likelihood)
        # print("\nNeutral likelihood : ",neutral_likelihood) 
       
        # for x in positive_likelihood, negative_likelihood, neutral_likelihood:
        #     j = i
        #     k = i
        #     if (positive_likelihood[i] > negative_likelihood[i]) and (positive_likelihood[i] > neutral_likelihood[i]):
        #         print("\npositive")
        #     elif negative_likelihood[j] > neutral_likelihood[k]:
        #         print("\nnegative")
        #     elif positive_likelihood[i] > negative_likelihood[j]:
        #         print("\nneutral")
        #     else:
        #         print("\nError: Cannot be classified  ")
        #     i = i + 1
        # print("\n")
        # print("--------Test Data :")
        # for i in testNews:
        #     print(i)
        # print("No. of news = ", len(testNews))
       
        # print("\n")
        # print("\n---------------Sentiment Analysis of News    :")
        # for i in range(len(testData)):
        #     if (positive_likelihood[i] > negative_likelihood[i]) and (positive_likelihood[i] > neutral_likelihood[i]):
        #         # print("positive")
        #         self.positive_news.append(testData[i])
        #         self.positive_news.append(testNews[i])
                
        #         # print(self.positive_news)

        #     elif (negative_likelihood[i] > neutral_likelihood[i]) and (negative_likelihood[i] > positive_likelihood[i]):
        #         # print("negative")
        #         self.negative_news.append(testData[i])
        #         self.negative_news.append(testNews[i])
                
        #         # print(self.negative_news)

        #     elif (neutral_likelihood[i] > negative_likelihood[i]) and (neutral_likelihood[i] > positive_likelihood[i]):
        #         # print("neutral")
        #         # self.neutral_news.append(testData[i])
        #         self.neutral_news.append(testNews[i])
                
        #         # print(self.neutral_news)
        #     else:
        #         # print(testData[i])
        #         # self.error_data.append(testData[i])
        #         self.error_data.append(testNews[i])
                
                # print("Error: Cannot be classified  ")
        p = []
        for i in testNews:
            p.append(i.pk)

        t= []
        for i in testNews:
            t.append(i.title)

        des = []
        for i in testNews:
            des.append(i.description)

        a = []
        for i in testNews:
            a.append(i.article)

        u = []
        for i in testNews:
            u.append(i.url)

        iu = []
        for i in testNews:
            iu.append(i.image_url)

        pd = []
        for i in testNews:
            pd.append(i.pubDate)

        variable1 = len(naivePositiveClassified.objects.all())
        variable2 = len(naiveNegativeClassified.objects.all())
        variable3 = len(naiveNeutralClassified.objects.all())

        # PositiveClassified.objects.all().delete()
        # NegativeClassified.objects.all().delete()
        # NeutralClassified.objects.all().delete()
        
                
        count =0
        len(testNews)
        for i in range(len(testData)):
            if (variable1 >0) and (variable2>0) and (variable3>0):
                break
            else:
                if (positive_likelihood[i] > negative_likelihood[i]) and (positive_likelihood[i] > neutral_likelihood[i]):
                # print("positive")
                # self.positive_news.append(testData[i])

                    self.positive_news.append(testNews[i])
                    r = naivePositiveClassified(s_no = p[i],title =  t[i],description =des[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                    r.save()
               
                

                # while len(testNews)>=variable1:
                    # r = PositiveClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                #     r.save()
                #     variable1 +=1

                
                # count+=1
                # n = newsType(sentiment == positive)
                # a = Article()
                # t = classifiedNews(newsType=Positive,Article)
                
                # print(self.positive_news)

                elif (negative_likelihood[i] > neutral_likelihood[i]) and (negative_likelihood[i] > positive_likelihood[i]):
                # print("negative")
                # self.negative_news.append(testData[i])
                    self.negative_news.append(testNews[i])
                    r = naiveNegativeClassified(s_no = p[i],title =  t[i],description =des[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                #     
                # NegativeClassified.objects.all().delete()
                
                    r.save()
               
              
               
                # if len(NegativeClassified.objects.all())==0:
                    # NegativeClassified.objects.all().delete()
                # while len(testNews)>=variable2:
                #     r = NegativeClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                #     r.save()
                #     variable2 +=1

                # count+=1
                
                
                # print(self.negative_news)

                elif  (neutral_likelihood[i] > negative_likelihood[i]) and (neutral_likelihood[i] > positive_likelihood[i]):
                # print("neutral")
                # self.neutral_news.append(testData[i])
                    self.neutral_news.append(testNews[count])
                # r = NeutralClassified(s_no = p[count],title =  t[count],article = a[count],url = u[count],image_url  = iu[count],pubDate = pd[count])
                    r = naiveNeutralClassified(s_no = p[count],title =  t[count],description =des[i],article = a[count],url = u[count],image_url  = iu[count],pubDate = pd[count])
                
                    r.save()

                else:
                     self.error_data.append(testNews[i])
               
                # print(testData[i])
                # self.error_data.append(testData[i])
               

            count +=1
               

                # if len(NeutralClassified.objects.all())==0:
                # while len(testNews)>=variable3:
                #     r = NeutralClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                #     r.save()
                #     variable3 +=1
        



        print("List of positive news:")
        for i in self.positive_news:
            print(i)
        print("No. of positive news = ", len(self.positive_news))
        print("\n")
        print("List of negative news:")
        for i in self.negative_news:
            print(i)
        print("No. of negative news = ", len(self.negative_news))
        
        print("\n")
        print("List of neutral news:") 
        for i in self.neutral_news:
            print(i)
        print("No. of neutral news = ", len(self.neutral_news))
        
        print("\n")
        print("List of error news:")
        for i in self.error_data:
            print(i)






        #to caculate likelihood of each news and news classification
        #testData = collection of verbs of newsheadline
        # testNews = collection of news headlines
    # def classify(self,testData,testNews,positive_likelihood,negative_likelihood,neutral_likelihood):
        # print("Positive_likelihood : ",positive_likelihood)
        # print("\nNegative_likelihood : ",negative_likelihood)
        # print("\nNeutral likelihood : ",neutral_likelihood) 
       
        # for x in positive_likelihood, negative_likelihood, neutral_likelihood:
        #     j = i
        #     k = i
        #     if (positive_likelihood[i] > negative_likelihood[i]) and (positive_likelihood[i] > neutral_likelihood[i]):
        #         print("\npositive")
        #     elif negative_likelihood[j] > neutral_likelihood[k]:
        #         print("\nnegative")
        #     elif positive_likelihood[i] > negative_likelihood[j]:
        #         print("\nneutral")
        #     else:
        #         print("\nError: Cannot be classified  ")
        #     i = i + 1
        # print("\n")
        # print("--------Test Data :")
        # # for i in testNews:
        #     print(i)
        # print("\n")
        # p = []
        # for i in testNews:
        #     p.append(i.pk)

        # t= []
        # for i in testNews:
        #     t.append(i.title)

        # a = []
        # for i in testNews:
        #     a.append(i.article)

        # u = []
        # for i in testNews:
        #     u.append(i.url)

        # iu = []
        # for i in testNews:
        #     iu.append(i.image_url)

        # pd = []
        # for i in testNews:
        #     pd.append(i.pubDate)
        
        

        # # count = 0
        # print("\n---------------Sentiment Analysis of News    :")
        # for i in range(len(testData)):
        #     if (positive_likelihood[i] > negative_likelihood[i]) and (positive_likelihood[i] > neutral_likelihood[i]):
        #         # print("positive")
        #         # self.positive_news.append(testData[i])
        #         self.positive_news.append(testNews[i])
        #         r = PositiveClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
        #         r.save()
        #         # count+=1
        #         # n = newsType(sentiment == positive)
        #         # a = Article()
        #         # t = classifiedNews(newsType=Positive,Article)
                
        #         # print(self.positive_news)

        #     elif (negative_likelihood[i] > neutral_likelihood[i]) and (negative_likelihood[i] > positive_likelihood[i]):
        #         # print("negative")
        #         # self.negative_news.append(testData[i])
        #         self.negative_news.append(testNews[i])
        #         r = NegativeClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
        #         r.save()
        #         # count+=1
                
                
        #         # print(self.negative_news)

        #     elif  (neutral_likelihood[i] > negative_likelihood[i]) and (neutral_likelihood[i] > positive_likelihood[i]):
        #         # print("neutral")
        #         # self.neutral_news.append(testData[i])
        #         self.neutral_news.append(testNews[i])
        #         r = NeutralClassified(s_no = p[i],title =  t[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
        #         r.save()
        #         # count+=1
                
                # print(self.neutral_news)
            # else:
            #     # print(testData[i])
            #     # self.error_data.append(testData[i])
            #     self.error_data.append(testNews[i])
            #     # count+=1
                
                # print("Error: Cannot be classified  ")
        # print("List of positive news:")
        # for i in self.positive_news:
        #     print(i)
        # print("No. of positive news = ", len(self.positive_news))
        # print("\n")
        # print("List of negative news:")
        # for i in self.negative_news:
        #     print(i)
        # print("No. of negative news = ", len(self.negative_news))
        
        # print("\n")
        # print("List of neutral news:") 
        # for i in self.neutral_news:
        #     print(i)
        # print("No. of neutral news = ", len(self.neutral_news))
        
        # print("\n")
        # print("List of error news:")
        # for i in self.error_data:
        #     print(
