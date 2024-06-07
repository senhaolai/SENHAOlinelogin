from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.display_name
