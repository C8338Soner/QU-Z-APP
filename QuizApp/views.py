from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Quizes, Question
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import APIView

# Create your views here.

class Quiz(generics.ListAPIView):
 queryset = Quizes.objects.all()
 serializer_class = QuizSerializer
 
 
 
 
class Questions(APIView):
 def get(self, request, pk):
     qs = Question.objects.filter(pk=pk)
     serializer = QuestionSerializer(qs)
     return Response(serializer.data)
    
    
    
    
  # def get(self, request, id, format=None):
  #     snippet = Question.objects.filter(id)
  #     serializer = QuestionSerializer(snippet)
  #     return Response(serializer.data)
 
 
 
 
 
 # def get_object(self, pk):
 #    return get_object_or_404(Question, pk=pk)
   
   
   
 # def get(self, pk ):
 #  question = Question.get_object(pk)
 #  serializer = QuestionSerializer(question, many=True)
 #  return Response(serializer.data)
  
 
