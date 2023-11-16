from django.dispatch import receiver
from .models import Frequest,Notification
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User = get_user_model()


@receiver(post_save,sender=Frequest)
def friend_request_notification(sender,instance,created,**kwargs):
    send_to = instance.receiver
    message = f"you were added by {instance.sender.username}"

    if sender:
        Notification.objects.create(
            message=message,
            owner=send_to)

"""@receiver(m2m_change,sender=User.friends.through)
def accepted_request_notification(sender,instance,action,**kwargs):
    message = f"{request.user.username} accepted your friend request"

    Notification.objects.create(
            message=message,
            owner=send_to)"""
