from django.db import models

class ApiResponse(models.Model):
    text = models.TextField()