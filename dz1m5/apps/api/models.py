from tabnanny import verbose
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"