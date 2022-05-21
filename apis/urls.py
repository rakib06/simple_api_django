from django.urls import path

from .views import ListTodo, DetailTodo
from .views import ListHadith, DetailHadith, getHadithTitle

urlpatterns = [
    path('todo/', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('hadith/', ListHadith.as_view()),
    path('hadith/<int:pk>/', DetailHadith.as_view()),
    path('hadith/t', getHadithTitle.as_view()),
    



]
