from django.urls import path
from .views import QuestionListView


app_name = 'poll'

urlpatterns = [
    path('', QuestionListView.as_view(), name='list')
]