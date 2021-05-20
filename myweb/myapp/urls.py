from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^article/$', views.article_list, name='article_list'),
	url(r'test/$',views.test_list, name='test_list'),
	url(r'^training/$',views.training_news, name='training_news'),
    url(r'^tarticle_negative/(?P<pk>\d+)/$',views.tnegative_detail, name='tnegative_detail'),
    url(r'^tarticle_positive/(?P<pk>\d+)/$',views.tpositive_detail, name='tpositive_detail'),
    url(r'^tarticle_neutral/(?P<pk>\d+)/$',views.tneutral_detail, name='tneutral_detail'),

    url(r'^article_negative/(?P<pk>\d+)/$',views.negative_detail, name='negative_detail'),
    url(r'^article_positive/(?P<pk>\d+)/$',views.positive_detail, name='positive_detail'),
    url(r'^sentiment/$', views.sentiment, name='sentiment'),
    url(r'^article_neutral/(?P<pk>\d+)/$',views.neutral_detail, name='neutral_detail'),
    url(r'^$',views.index, name='index'),
    url(r'^article_detail/$',views.positive_detail, name='article_detail'),
    url(r'^result/(?P<pk>\d+)/$', views.result, name='result'),
    url(r'^classified/(?P<pk>\d+)/$', views.classified_text, name='classified_text'),
    url (r'^visualization/$', views.visualization, name='visualization'),
    
    # url(r'^$',views.category_list, name='category_list'),
    # url(r'^checkout/$', views.checkout, name='checkout'),
    # url(r'^search/$', views.search_product, name='search_product'),
    # url(r'^categories/(?P<slug>[\w\-]+)$', views.category_list, name='category_list'),
    # url(r'^product_detail/(?P<slug>[\w\-]+)$',views.product_detail, name='product_detail'),
    # url(r'^register/$',views.register, name='register'),
    # url(r'^accounts/login/$',views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^profile/dashboard/$',views.dashboard, name='dashboard'),

	
]