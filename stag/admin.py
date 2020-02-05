from django.contrib import admin
from .models import Question, Category, Comment
# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
