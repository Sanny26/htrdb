from django.urls import path, re_path

from . import views


# use re_path for using it along with regular expressions
urlpatterns = [
	path('', views.main, name='home'),
	path('progess', views.progess, name='progress'),
	path('faq', views.faq, name='faq'),
	path('people', views.people, name='people'),
	path('contact', views.contact, name='contact')
	]