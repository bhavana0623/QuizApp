# Generated by Django 5.0.6 on 2024-07-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_option1_question_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_option',
        ),
    ]