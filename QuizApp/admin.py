from django.contrib import admin
from .models import Category, Answer, Quizes, Question


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Quizes)
class QuizesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_right', ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz', 'difficulty', 'tecqnique']

    list_display = ['title', 'quiz', 'date_updated', 'difficulty']

    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']
    


# from django.contrib import admin
# from .models import Category, Quiz, Question, Answer, Choice


# admin.site.register(Choice)


# class QuizInline(admin.StackedInline):
#     model = Quiz
#     extra = 0


# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 0


# class AnswerInline(admin.StackedInline):
#     model = Answer
#     extra = 0


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",


#     )
#     list_filter = ("name",)
#     search_fields = ("name__startswith",)
#     inlines = [QuizInline, QuestionInline, AnswerInline]


# @admin.register(Quiz)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = (
#         "category",
#         "title",
#         "date_created",
#     )

#     inlines = [QuestionInline]
