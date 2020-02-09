from django.urls import path, include
from .views import QuestionListView, HomeView

app_name = 'stag'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('questions/', QuestionListView.as_view(), name='questions')
]