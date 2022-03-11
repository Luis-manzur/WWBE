"""Django models utilities"""

#Django
from django.db import models

class WWBModel(models.Model):
    """Comparte Ride base model.

    WWB acts as an abstract base class from wich every oder model in the project will inherit. This class provides every table with the following attributes:
        + created (DateTime): store the datime the object was created
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateField(
        "created at",
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateField(
        "modified at",
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta options"""

        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
