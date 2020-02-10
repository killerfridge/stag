from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class QuestionListView(LoginRequiredMixin, ListView):
    template_name = 'poll/poll_list.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voted = Question.objects.filter(answer__voted_by=self.request.user.id)
        context['voted'] = voted
        return context
    

class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'poll/poll_detail.html'


