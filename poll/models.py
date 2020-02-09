from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        """On save, update the timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(blank=True)
    voted_by = models.ManyToManyField(User, blank=True)
    choice = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        """On save, update the timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Answer, self).save(*args, **kwargs)

    def _votes(self):
        return self.voted_by.count()

    def __str__(self):
        return self.choice

    votes = property(_votes)

    # TODO create a query within the model to return the number of votes
