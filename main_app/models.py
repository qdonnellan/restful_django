from django.db import models

class Thing(models.Model):
    """
    a dummy model called "Thing"
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,default='')
    body = models.TextField()
