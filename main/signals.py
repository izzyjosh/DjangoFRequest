from django.dispatch import receiver
from .models import Frequest,Notification
from django.db.models.signals import post_save


@receiver(post_save,sender=Frequest)
def friend_request_notification(sender,instance,created,**kwargs):
    send_to = instance.receiver
    message = f"you were added by {send_to.username}"

    Notification.objects.create(
            message=message,
            owner=send_to)


