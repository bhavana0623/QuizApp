from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('<int:test_id>/',views.quiz_details, name='quiz_details'),
    path('<int:test_id>/start_quiz/' , views.quiz_start , name='start'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('<int:test_id>/edit_quiz/', views.edit_quiz, name='edit_quiz'),
    path('register/', views.register , name='register')
    
    
    
    
]
