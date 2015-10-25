from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    approved = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.user.username
