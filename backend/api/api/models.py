from django.db import models

class Item(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField()