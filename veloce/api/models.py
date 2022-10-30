from django.db import models


class RinCommands(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cog = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
