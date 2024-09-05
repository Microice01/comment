from django.db import models

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  # Return the first 50 characters
