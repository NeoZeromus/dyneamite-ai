from django.db import models

# Create your models here.

class Message(models.Model):
    message = models.TextField()
    tokens = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    
class API(models.Model):
    api = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.api
    
    
