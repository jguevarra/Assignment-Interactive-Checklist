from django.urls import path

from . import views

app_name = 'calendar'
urlpatterns = [
    # ex: /calendar/
    path('', views.index, name='index'),
    # ex: /calendar/1/
    path('<int:events_id>/', views.detail, name='detail'),
    path('home/', views.calendar,{'year': 2018, 'month':10}),
]