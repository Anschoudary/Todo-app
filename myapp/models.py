from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=255)
    OPTION_ONE = 'High'
    OPTION_TWO = 'medium'
    OPTION_THREE = 'low'
    OPTIONS = [
        (OPTION_ONE, 'High'),
        (OPTION_TWO, 'Medium'),
        (OPTION_THREE, 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=OPTIONS, default=OPTION_TWO)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title