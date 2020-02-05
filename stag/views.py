from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question
# Create your views here.


class QuestionListView(ListView):
    model = Question
