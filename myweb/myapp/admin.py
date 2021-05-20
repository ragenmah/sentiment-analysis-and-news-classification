# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Feed)
admin.site.register(MyModel)
admin.site.register(Search)
admin.site.register(ClassifiedText)



admin.site.register(PositiveTraining)
admin.site.register(NegativeTraining)
admin.site.register(NeutralTraining)

admin.site.register(stemmedVerbPositiveTraining)
admin.site.register(stemmedVerbNegativeTraining)
admin.site.register(stemmedVerbNeutralTraining)
# admin.site.register(tokenisation)

admin.site.register(stemmedVerbTestNews)
admin.site.register(testNews)

admin.site.register(naivePositiveClassified)
admin.site.register(naiveNegativeClassified)
admin.site.register(naiveNeutralClassified)

# admin.site.register(Delivery)
admin.site.register(tfidfPositiveClassified)
admin.site.register(tfidfNegativeClassified)
admin.site.register(tfidfNeutralClassified)


admin.site.register(NaiveCount)
admin.site.register(TfidfCount)
