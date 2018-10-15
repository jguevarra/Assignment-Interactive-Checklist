from django.urls import path

from . import views

app_name = 'assignment_calendar'

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    # ex: /home/1/
    path('<int:post_id>/', views.detail, name='detail'),
]