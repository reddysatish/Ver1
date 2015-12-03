from django.conf.urls import url,patterns
from . import views
from django.conf import settings
urlpatterns=[
    url(r'^art$',views.list,name='index'),
    url(r'^art/(?P<id>\d+)$',views.desc,name='index'),
]