from django.urls import path

from . import views

app_name = 'calendar'
urlpatterns = [
    # ex: /calendar/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /calendar/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('home/', views.calendar,{'year': 2018, 'month':10}),
    path('create/', views.create_assignment, name='create'),
]