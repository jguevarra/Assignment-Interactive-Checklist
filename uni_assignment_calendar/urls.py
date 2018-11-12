from django.urls import path

from . import views

app_name = ''

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('course/<int:class_id>/', views.course_detail, name='course_detail'),
    path('create/', views.create_assignment, name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('schedule/', views.schedule, name='schedule'),
    path(r'schedule/ScheduleResults/$',views.ScheduleResults,name='ScheduleResults')
]
