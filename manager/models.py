from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_creator")
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"
    

class Assignments(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignment_creator")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="assignment_category")
    added = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    missed = models.BooleanField(default=False)
    time_str = models.CharField(max_length=15, blank=True, null=True)
    date_str = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        ordering = ["due_time"]

    def __str__(self):
        return f"{self.category}"

