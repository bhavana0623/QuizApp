from django.db import models

# Create your models here.

class quiz(models.Model):
    
    QUESTION_TYPES = [
        ('mcq', 'MULTIPLE CHOICE'),
        ('des', 'DESCRIPTIVE TYPE'),
    ]
    
    name = models.CharField(max_length=100)
    
    description = models.TextField(default='')
    
    max_questions = models.IntegerField(default=0)
    max_marks = models.IntegerField()
    question_type = models.CharField(max_length=3,choices=QUESTION_TYPES)
    total_time = models.IntegerField(default=0)
    questions = models.ManyToManyField('question', related_name='questions')


    def __str__(self):
        return self.name


class question(models.Model):
    
    quest = models.TextField()
    answer = models.CharField(max_length=255)
    
    
    
    #many to many relation
   
    
    def __str__(self):
        return f'{self.pk} - {self.quest[:10]}'
    