from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('schedule/<str:login>/', views.schedule, name="schedule"),
    path('', views.check_student, name='check_student'),
    path('teachers_search/', views.teachers_search, name="teachers_search"),
    path('view_teachers/<str:last_name>/', views.view_teachers, name="view_teachers"),
]