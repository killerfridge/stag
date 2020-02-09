from django.contrib import admin
from .models import Question, Answer
# Register your models here.


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ['question', 'votes', 'voted_by']
    readonly_fields = ['votes']


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['choice', 'votes', 'voted_by']
    readonly_fields = ['votes', 'voted_by']
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
