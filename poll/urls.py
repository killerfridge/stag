from django.urls import path
from .views import QuestionListView, QuestionDetailView


app_name = 'poll'

urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('<int:pk>', QuestionDetailView.as_view(), name='detail')
]