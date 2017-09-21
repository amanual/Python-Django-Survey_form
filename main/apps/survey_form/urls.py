from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^surveys/process$', views.index),
    url(r'^result$', views.result),
    # url(r'^reset', views.reset)     --this rest route could be used to reset the counter
]