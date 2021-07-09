from django.db import models
from django.contrib.auth.models import User

USER_CHOICES = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
)
class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    user_type = models.CharField(max_length=20, choices=USER_CHOICES)

    def __str__(self):
        return str(self.user)
