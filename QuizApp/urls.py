from django.urls import path
from .views import Quiz, Questions

app_name = 'QuizApp'

urlpatterns = [
    path('', Quiz.as_view()),
    path('q/<int:pk>/', Questions.as_view()),
]
