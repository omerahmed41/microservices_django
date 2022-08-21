from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone, dateformat
# Create your models here.


class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='todo_item', null=True, on_delete=models.CASCADE)
    content = models.TextField()
    priority = models.TextField()
    flag = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expireDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super().save(*args, **kwargs)
