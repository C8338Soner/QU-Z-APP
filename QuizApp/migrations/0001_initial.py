# Generated by Django 3.2.9 on 2021-11-26 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Quiz', max_length=200, verbose_name='Quiz Title')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='quiz_category', to='QuizApp.category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('tecqnique', models.IntegerField(choices=[(0, 'Multiple Choice')], default=0, verbose_name='Type of Qustion')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('difficulty', models.IntegerField(choices=[(0, 'fundamental'), (1, 'easy'), (2, 'intermediate'), (3, 'hard'), (4, 'extremely hard')], default=0, verbose_name='Difficulty')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='QuizApp.quizes')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='QuizApp.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]
