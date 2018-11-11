from django.urls import path

from . import views

app_name = 'calendar'

urlpatterns = [
    # ex: /calendar/
    path('', views.user_login, name='login'),
    path('home/', views.IndexView.as_view(), name='index'),
    # ex: /calendar/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /calendar/create
    path('create/', views.create_assignment, name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

# urlpatterns = [
#     # ex: /calendar/
#     path('', views.IndexView.as_view(), name='index'),
#     # ex: /calendar/1/
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # ex: /calendar/create
#     path('create/', views.create_assignment, name='create'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]