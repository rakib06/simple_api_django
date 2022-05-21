from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from todos.models import Todo
from hadith.models import Hadith
from .serializers import TodoSerializer, HadithSerializer, HadithTitleSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListHadith(generics.ListCreateAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer


class DetailHadith(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithSerializer

class getHadithTitle(generics.ListCreateAPIView):
    queryset = Hadith.objects.all()
    serializer_class = HadithTitleSerializer