from django.urls import path

from . import views

urlpatterns = [
    # ex: /calendar/
    path('', views.index, name='index'),
    # ex: /calendar/1/
    path('<int:post_id>/', views.detail, name='detail'),
    path('home/', views.calendar,{'year': 2018, 'month':10}),
]