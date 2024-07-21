from django.shortcuts import render,get_object_or_404
from .models import quiz,question

# Create your views here.
def home(request):
    First_name = 'Arya'
    quizs = quiz.objects.all()
    return render(request, 'home.html',{'name':First_name, 'quizs':quizs})

def quiz_details(request, test_id):
    Quiz = get_object_or_404(quiz,pk=test_id)
    return render(request, 'test_details.html', {'Quiz':Quiz})

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