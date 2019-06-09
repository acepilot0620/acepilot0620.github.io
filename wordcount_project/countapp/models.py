from django.db import models

class InputText(models.Model):
    content = models.TextField
    def __str__(self):
        return self.content 
    