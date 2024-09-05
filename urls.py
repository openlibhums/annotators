from django.urls import re_path

from plugins.annotators import views

urlpatterns = [
    re_path(r'^$', views.index, name='annotators_index'),
]