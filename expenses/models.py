from django.db import models
from users.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    category = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title