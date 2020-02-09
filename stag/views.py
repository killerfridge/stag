from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Question
# Create your views here.


class QuestionListView(ListView):
    model = Question
    template_name = 'stag/question_list.html'


class HomeView(TemplateView):
    template_name = 'stag/home.html'
