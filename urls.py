from django.urls import path

from . import views

app_name = 'multipl'

urlpatterns = [
    path('',views.index, name='index'),
    # ex: /multipl/
    path('', views.index, name='index'),
    # ex: /multipl/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /multipl/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /multipl/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

 
