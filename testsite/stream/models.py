from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import signals

from items.models import PhotoItem, TweetItem


class NotDeletedStreamManager(models.Manager):
    def get_queryset(self):
        return super(NotDeletedStreamManager, self).get_queryset().filter(deleted=False)


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    objects = models.Manager()
    active = NotDeletedStreamManager()

    def __unicode__(self):
        return '{} {}: {}'.format(self.__class__.__name__,
                                  self.content_type.model,
                                  self.created_at)


def update_stream(sender, instance, created, **kwargs):
    if created:
        Stream.objects.create(
            user=instance.user,
            created_at=instance.created_at,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.id)

for item_type in (TweetItem, PhotoItem):
    signals.post_save.connect(update_stream, sender=item_type)