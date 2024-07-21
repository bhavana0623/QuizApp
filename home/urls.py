from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('<int:test_id>/',views.quiz_details, name='quiz_details'),
    path('<int:test_id>/start_quiz/' , views.quiz_start , name='start')
    
    
]
