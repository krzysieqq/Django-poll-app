from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # Adding ClassBasedViews
    # # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/result/
    # url(r'^(?P<question_id>[0-9]+)/results/', views.results, name='results'),
    # # ex: /polls/5/vote
    # url(r'^(?P<question_id>[0-9]+)/vote/', views.vote, name='vote'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/', views.vote, name='vote')
]

