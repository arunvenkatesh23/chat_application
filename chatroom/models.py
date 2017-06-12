from django.db import models
from django.conf import settings
from accounts.models import User


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    receiver = models.EmailField(max_length=40, null=False)
    room = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return '%s' % self.user.username
