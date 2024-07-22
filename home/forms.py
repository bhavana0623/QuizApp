from django import forms
from .models import quiz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuizForm(forms.ModelForm):
    class Meta:
        model = quiz
        fields = ['name','description','max_questions','max_marks','question_type','total_time','questions']
        
#fix questions


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2') 