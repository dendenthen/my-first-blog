#imports
from django.conf.urls import url
from . import views

# url patterns
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
