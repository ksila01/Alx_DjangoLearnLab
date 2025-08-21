from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(recipient, actor, verb, target=None):
    ct = None
    obj_id = None
    if target is not None:
        ct = ContentType.objects.get_for_model(type(target))
        obj_id = target.pk
    if recipient != actor:
        Notification.objects.create(
            recipient=recipient,
            actor=actor,
            verb=verb,
            content_type=ct,
            object_id=obj_id,
        )
