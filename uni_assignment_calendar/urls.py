from django.urls import path

from . import views

app_name = 'calendar'
urlpatterns = [
    # ex: /calendar/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /calendar/1/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:events_id>/', views.detail, name='detail'),
    # ex: /calendar/create
    path('create/', views.create_assignment, name='create'),
    # ex: /calendar/1/results/
    path('<int:events_id>/results/', views.results, name='results'),
    # ex: /calendar/1/vote/
    path('<int:events_id>/vote/', views.vote, name='vote'),
]