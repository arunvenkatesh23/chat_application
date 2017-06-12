from django.conf.urls import url
from . import views

app_name = 'chatroom'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.send, name='send'),
]
