from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^personal_information', views.personal_information),
    re_path(r'^$', views.bible_list, name='bible_list'),
    re_path(r'^shortcut/$', views.shortcut, name='shortcut'),
    re_path(r'(?P<pk>\d+)/$', views.bible_detail, name='bible_detail'),
    re_path(r'^introduction/$', views.introduction, name='introduction'),
    re_path(r'^shape/$', views.shape, name='shape')
]
