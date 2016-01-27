from django.conf.urls import url, handler404
from blog.views import *

urlpatterns = [
    url(r'^test$', test_form, name='test_form'),
    url(r'^articles$', show_articles, name='show_articles'),
]

