from django.db import models

class ApiResponse(models.Model):
    text = models.TextField()

class ChatHistory(models.Model):
    username = models.CharField(max_length=100)
    text_field = models.TextField()