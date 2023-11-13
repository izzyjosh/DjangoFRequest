from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class MyUser(AbstractUser):
    
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    contact = models.IntegerField(blank=True,null=True)
    friends = models.ManyToManyField('self',symmetrical=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username



