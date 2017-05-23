from django.conf.urls import url

from plugins.annotators import views

urlpatterns = [
    url(r'^$', views.index, name='annotators_index'),
]