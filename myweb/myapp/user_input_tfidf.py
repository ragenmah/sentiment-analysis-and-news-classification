from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from .models import PositiveTraining,NegativeTraining,NeutralTraining
# from .models import tokenisePositiveTraining,tokeniseNegativeTraining,tokeniseNeutralTraining
from myapp.models import *


import re
import nltk
import csv
import math

def user_tfidf(user_input,input_text):
    test_news = [] #verbs of test data
    test = []

    test_verb = user_input #stemmedVerbTestNews.objects.all()
    print(test_verb)
    # for i in test_verb:
    #     test.append(i)
    # # test_data1 = test_verb #test_data = test verbs of test new

    # for i in test:
    #     print(i)
    i =test_verb
    i = str(i)
    token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
    regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
    token = regex_wt.tokenize(i)   #tokens ---list objec
    test_news =token
    
    print("Hello babay")
    print(test_news)
    # test_t = Article.objects.all()
    test_title = list(input_text) #test news titlw

           
    
    positive1 = []
    negative1 = []
    neutral1 = []

    positive = []
    negative = []
    neutral = []


    positive_title = stemmedVerbPositiveTraining.objects.all()
    for i in positive_title:
        positive1.append(i.stemmedVerb)

    for i in positive1:
        print(i)

        i = str(i)
        token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
        regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
        token = regex_wt.tokenize(i)   #tokens ---list objec
        positive.append(token)
           
    


    negative_title = stemmedVerbNegativeTraining.objects.all()
    for i in negative_title:
        negative1.append(i.stemmedVerb)

    for i in negative1:
        print(i)

        i = str(i)
        token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
        regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
        token = regex_wt.tokenize(i)   #tokens ---list objec
        negative.append(token)


           
    

    neutral_title = stemmedVerbNeutralTraining.objects.all()
    for i in neutral_title:
        neutral1.append(i.stemmedVerb)

    for i in neutral1:
        print(i)

        i = str(i)
        token_pattern = r'\w+'  # small w represent [a-zA-Z0-9 _ ]
        regex_wt = nltk.RegexpTokenizer(pattern = token_pattern,gaps=False) #haven't==haven t
        token = regex_wt.tokenize(i)   #tokens ---list objec
        neutral.append(token)

    

    word_belongs_to_class =1
    dict_distinct_words = {}
    distinct_word = []

    

    positive_words =[]
    negative_words =[]
    neutral_words =[]
    test_words =[]
    positive_news = []
    negative_news = []
    neutral_news = []
    error_data = []

    for i in positive:
        positive_words.extend(i)


    # print(positive_words)
    # print("positive\n")

    for i in negative:
        negative_words.extend(i)
    # print(negative_words)
    # print("negative\n")


        

    for i in neutral:
        neutral_words.extend(i)
    # print(neutral_words)
    # print("neutral\n")






    list_of_all_words = []
    for row in positive,negative,neutral:
        for i in row:
            list_of_all_words.extend(i)

    # print("\nVocabulary------------",list_of_all_words)




    positive_distinct_word = {}
    neutral_distinct_word = {}
    negative_distinct_word = {}

#calculate tf
    tfPositive = {}
    tfNegative = {}
    tfNeutral  = {}
        
    for i in positive_words:
            if(i not in tfPositive.keys()):
                tfPositive[i] = 1 + math.log10(sum(1 for p in positive_words if p == i))   # Log-frequency weighting, can use other (accuracy needs to be checked)
   
    for i in negative_words:
            if(i not in tfNegative.keys()):
                tfNegative[i] = 1 + math.log10(sum(1 for p in negative_words if p == i))
    for i in neutral_words:
            if(i not in tfNeutral.keys()):
                tfNeutral[i] = 1 + math.log10(sum(1 for p in neutral_words if p == i))


    
    # print("\nCount of unique tfpositive words  ",tfPositive)
    # print("\nCount of unique tfnegative words  ",tfNegative)
    # print("\nCount of unique tfneutral words  ",tfNeutral)



   #calculation of IDF weights
    Idf = {}
    for i in list_of_all_words:
        if i not in dict_distinct_words:
            dict_distinct_words[i] = 1
        else:
            dict_distinct_words[i] += 1


    for i in dict_distinct_words:
        if i in positive_words:
            word_belongs_to_class = 1
        if i in negative_words:
            word_belongs_to_class += 1
        if i in neutral_words:
            word_belongs_to_class += 1
    


        Idf[i] = math.log10(1+(3 / word_belongs_to_class))
     # print(dict_distinct_words[i])

    # print("\nCount of idf of unique word",Idf)

#claculate product wt and predict
# for i in test_data:

    # print("\nSabai distinct words=====",dict_distinct_words)
# print("Total no of distinct words------",result)
# return result


    tf_idf_positive ={}
    tf_idf_negative ={}
    tf_idf_neutral ={}

    tf_idf_po =0
    tf_idf_ne =0
    tf_idf_nu =0

# a =[]
# count = 0
# for row in test_news:

#     for i in tfPositive:
#         for y in Idf:
#             for x in row:
#                 print("---\n")
#                 if (x == y)and (x==i):
#                     # a.append(x)
#                     tf_idf_po +=tfPositive[x]*Idf[x]

#             tf_idf_positive[count] = tf_idf_po

#             for x in tfNegative:
#                 print("---\n")
#                 if (x == y)and (x==i):
#                     tf_idf_ne +=tfNegative[x]*Idf[x]
#             tf_idf_negative[count] =tf_idf_ne

#             for x in tfNeutral:
#                 print("---\n")
#                 if (x == y)and (x==i):
#                     # a.append(x)
#                     tf_idf_nu +=tfNeutral[x]*Idf[x]
#             tf_idf_neutral[count] =  tf_idf_nu
#     count +=1
    def calculate_tfidf(test_news,tfSentiment,Idf):
        count = 0
        tf_idf =0
        tf_idf_sentiment = {}

        for word in test_news:
            # for word in row:
            if(word in tfSentiment.keys()):
                    tf_idf +=tfSentiment[word]*Idf[word]
        tf_idf_sentiment[count] = tf_idf
        count +=1
        return tf_idf_sentiment

    tf_idf_positive = calculate_tfidf(test_news,tfPositive,Idf)
    tf_idf_negative =  calculate_tfidf(test_news,tfNegative,Idf)
    tf_idf_neutral = calculate_tfidf(test_news,tfNeutral,Idf)

        # if(word in .keys()):
        #     weight[''] = weight[''] + [word] * Idf[word]
        # if(word in tfNegative.keys()):
        #     weight['Negative'] = weight['Negative'] + tfNegative[word] * Idf[word]
        # if(word in tfNeutral.keys()):
        #     weight['Neutral'] = weight['Neutral'] + tfNeutral[word] * Idf[word]
    

# tf_idf_positive[row] = tf_idf_po
# tf_idf_negative[row] =tf_idf_ne
# tf_idf_neutral[row] =  tf_idf_nu
    # print("tf-idf -po==================",tf_idf_po)

    # print("\n Positive tf-idf   ===",tf_idf_positive)
    # print("\n Negative tf-idf   ===",tf_idf_negative)
    # print("\n Neutral tf-idf   ===",tf_idf_neutral)

    # for i in test_news:
    #     print(i)

    # p = []
    # for i in test_title:
    #     p.append(i.pk)

    # t= []
    # for i in test_title:
    #     t.append(i.title)

    # des= []
    # for i in test_title:
    #     des.append(i.description)


    # a = []
    # for i in test_title:
    #     a.append(i.article)

    # u = []
    # for i in test_title:
    #     u.append(i.url)

    # iu = []
    # for i in test_title:
    #     iu.append(i.image_url)

    # pd = []
    # for i in test_title:
    #     pd.append(i.pubDate)

    # variable1 = len(tfidfPositiveClassified.objects.all())
    # variable2 = len(tfidfNegativeClassified.objects.all())
    # variable3 = len(tfidfNeutralClassified.objects.all())


    # print("oh rice killer\n")
    # for i in range(len(test_news)):
    #     if (variable1 > 0 ) and (variable2 > 0 ) and (variable3 > 0):
    #         break
    #     else:
    if (tf_idf_positive[0] > tf_idf_negative[0]) and (tf_idf_positive[0] > tf_idf_neutral[0]):
        positive_news.append("Positive")
        positive_news.append(tf_idf_positive[0])
        positive_news.append(tf_idf_negative[0])
        positive_news.append(tf_idf_neutral[0])
        print("ka seta")
        print(positive_news)
        return positive_news
        
                # r = tfidfPositiveClassified(s_no = p[i],title =  t[i],description =des[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                # r.save()
               

    elif (tf_idf_negative[0] > tf_idf_neutral[0]) and (tf_idf_negative[0] > tf_idf_positive[0]):
        negative_news.append("Negative")
        negative_news.append(tf_idf_positive[0])
        negative_news.append(tf_idf_negative[0])
        negative_news.append(tf_idf_neutral[0])
        
        print("ka seta")
        print(negative_news)
        
        return negative_news                # r = tfidfNegativeClassified(s_no = p[i],title =  t[i],description =des[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                # r.save()
               

    elif (tf_idf_neutral[0] > tf_idf_negative[0]) and (tf_idf_neutral[0] > tf_idf_positive[0]):
        neutral_news.append("Neutral")
        neutral_news.append(tf_idf_positive[0])
        neutral_news.append(tf_idf_negative[0])
        neutral_news.append(tf_idf_neutral[0])
        print("ka seta")
        print(neutral_news)
        
        return neutral_news
                # r = tfidfNeutralClassified(s_no = p[i],title =  t[i],description =des[i],article = a[i],url = u[i],image_url  = iu[i],pubDate = pd[i])
                # r.save()
               

    else:
        error_data.append("error:cannot ne classify")
        return error_data
                # print("Error: Cannot be classified  ")
    # print("List of positive news:")
    # for i in positive_news:
    #     print(i)
    # print("No. of positive news = ", len(positive_news))
    # print("\n")

    # print("List of negative news:")
    # for i in negative_news:
    #     print(i)
    # print("No. of negative news = ", len(negative_news))
        
    # print("\n")
    # print("List of neutral news:") 
    # for i in neutral_news:
    #     print(i)
    # print("No. of neutral news = ", len(neutral_news))
        
    # print("\n")
    # print("List of error news:")
    # for i in error_data:
    #     print(i)

# print("\nCount of unique tfpositive words  ",tfPositive)
# print("\nCount of unique tfnegative words  ",tfNegative)
# print("\nCount of unique tfneutral words  ",tfNeutral)
          
# print("\nCount of idf of unique word",Idf)