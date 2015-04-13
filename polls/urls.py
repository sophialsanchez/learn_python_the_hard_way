from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'), #^$, matches start of str, matches end of str
	# ex: polls/nob-hill
	url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/nob-hill/get_response/
	url(r'^(?P<slug>[-\w]+)/get_response/$', views.Response, name='get_response'),
)



#	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), #\d+ matches a #
#	url(r'^(?P<slug>.+)/$', views.DetailView.as_view(), name='detail'),
#	url(r'/get_response/$', views.ResponseFormView.as_view(), name='get_response'),
