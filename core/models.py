from django.db import models
import uuid

class Post(models.Model):

    EXERCISES = [
        ("Strength Training", "Strength Training"), ("Running", "Running"),
        ("Swimming", "Swimming"), ("Tennis", "Tennis"), ("Cycling", "Cycling"),
        ("Volleyball", "Volleyball")
    ]

    FEELINGS = [
        ("Excited", "Excited"), ("Determined", "Determined"), ("Drained", "Drained"),
        ("Motivated", "Motivated"), ("Accomplished", "Accomplished"),
        ("Down", "Down"), ("Tired", "Tired")
    ]

    workout = models.CharField(max_length=200,choices=EXERCISES)
    workout_duration = models.IntegerField(null=True, blank=True)
    feeling = models.CharField(max_length=200, null=True, blank=True, choices=FEELINGS)
    body = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.workout

class Comment(models.Model):
    body = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.body
