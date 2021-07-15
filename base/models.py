from django.db import models
from django.contrib.auth.models import User # inbuilt django user info table dealing all of username, email, password...
# Create your models here.

class Task(models.Model): # task is database table and below attributes
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # one to many relationship(foreign key) with User table
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['complete'] # orderig will be done task is complete or not