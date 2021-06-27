from django.db import models


class HelpRequest(models.Model):

    description = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
    requested_by = models.CharField(max_length=80)
    completed_by = models.CharField(max_length=80)
