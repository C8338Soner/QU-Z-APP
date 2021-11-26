from rest_framework import serializers
from .models import Quizes, Question


class QuizSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Quizes
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
 
 class Meta: 
  model = Question
  fields = '__all__'
