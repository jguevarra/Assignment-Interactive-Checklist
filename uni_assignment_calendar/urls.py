from django.urls import path

from . import views

app_name = ''

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.index, name='index'), # this good
    path('<int:events_id>/', views.detail, name='detail'),
    path('course/<int:class_id>/', views.course_detail, name='course_detail'),
    path('create/', views.create_assignment, name='create'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/ScheduleResults/',views.ScheduleResults,name='ScheduleResults'),
    path('AboutUs/', views.AboutView, name='AboutUs'),
    path('goals/', views.GoalsView, name='goals'),
    path('schedule/hideAssgn/',views.hideAssgn,name='hideAssgn'),
    path('schedule/toggle/',views.toggle,name='toggle')
]
