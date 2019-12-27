from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/34/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/34/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/34/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]