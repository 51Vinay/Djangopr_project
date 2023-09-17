# email_app/models.py

from django.db import models

class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name
