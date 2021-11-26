from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quizes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']
    category = models.ForeignKey(
        Category, related_name='quiz_category', default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, default = _('New Quiz'), verbose_name = _('Quiz Title'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_('Last Updated'))
    class Meta:
        abstract = True
    

class Question(Updated):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']
    difficulty_list = (
        (0, _("fundamental")),
        (1, _("easy")),
        (2, _("intermediate")),
        (3, _("hard")),
        (4, _("extremely hard")),
    )
    type = (
        (0, _("Multiple Choice")),
        (0, _("Single Choice")),
    )
    quiz = models.ForeignKey(
        Quizes, related_name='question', on_delete=models.DO_NOTHING)
    tecqnique = models.IntegerField(choices=type, default=0, verbose_name=_('Type of Qustion'))
    title = models.CharField(max_length=300, verbose_name=_('Title'))
    difficulty = models.IntegerField(choices=difficulty_list, default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status')) 

    def __str__(self):
        return self.title


class Answer(Updated):
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']
        
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)    
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer_text

