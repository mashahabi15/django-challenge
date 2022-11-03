from django.db import models
from django.utils import timezone

from selling_platform.model_manager.base_manager import BaseManager


class Base(models.Model):
    # Soft Deletion
    is_deleted = models.BooleanField(default=False)
    deletion_time = models.DateTimeField(blank=True, null=True, default=None)

    # override these fields accordingly
    objects = BaseManager()
    all_objects = BaseManager(alive_only=False)

    # we want to have these fields in each model to log creation time and last update time of an object
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # Abstract Base class inheriting
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        It is called on each object's delete method (objects which are inherited from this class)
        """
        self.is_deleted = True
        self.deletion_time = timezone.now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        """
        Watch Out! Call this method only when you want to really delete an object!
        """
        super(Base, self).delete(using=using, keep_parents=keep_parents)

    def restore(self):
        """
        Call this method when you want to restore a deleted object.
        """
        self.is_deleted = False
        self.deletion_time = None
        self.save()
