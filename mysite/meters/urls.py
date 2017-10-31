from django.conf.urls import url

from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^data/$', views.jason, name='jason'),
url(r'^more/$', views.hostel, name='hostel'),
	]
