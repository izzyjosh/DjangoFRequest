from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid

class Frequest(models.Model):
    id = models.UUIDField(
            primary_key=True,
            unique=True,
            default=uuid.uuid4,
            editable=False,)
    sender = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="sender")
    receiver = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="receiver")
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"form {self.sender.username} to {self.receiver.username}"


class Image(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    images = models.ImageField(upload_to="user_image")

    def __str__(self):
        return self.user.username


class Notification(models.Model):
    id = models.UUIDField(
            primary_key=True,
            editable=False,
            default=uuid.uuid4,)
    message = models.CharField(max_length=500)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
