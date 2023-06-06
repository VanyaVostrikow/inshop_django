from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TelegrammUser(models.Model):

    chat_id = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'TelegrammUser {}'.format(self.id)