from django.shortcuts import render,get_object_or_404,redirect
from .models import quiz,question
from .forms import QuizForm,UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
    First_name = 'Arya'
    quizs = quiz.objects.all()
    return render(request, 'home.html',{'name':First_name, 'quizs':quizs})

def quiz_details(request, test_id):
    Quiz = get_object_or_404(quiz,pk=test_id)
    return render(request, 'test_details.html', {'Quiz':Quiz})

@login_required
def quiz_start(request, test_id):
    Quiz = get_object_or_404(quiz,pk = test_id)
    questions = Quiz.questions.all()
    
    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            
            if user_answer and user_answer.lower() == question.answer.lower():
                score+=1
        return render(request, 'quiz_submit.html',{'score':score, 'questions':total_questions})
    
    else:
        return render(request, 'quiz_start.html' , {'Quiz':Quiz, 'questions':questions})
    
@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz_temp = form.save(commit = False)
            quiz_temp.User = request.user
            quiz_temp.save()
            return redirect('home')
    
    else:
        form = QuizForm
        return render(request, 'create_quiz.html', {'form':form})
    


#fix bugs-------------------------------------------------
@login_required
def edit_quiz(request, test_id):
    quiz_instance = get_object_or_404(quiz, pk=test_id, User=request.user)

    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz_instance)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
    else:
        form = QuizForm(instance=quiz_instance)
        return render(request, 'edit_quiz.html', {'form': form})
    
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
        return render(request , 'registration/register.html', {'form':form})

