from django.db import models


class HelpRequest(models.Model):

    description = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_on = models.DateTimeField(null=True)
    complete_by = models.DateTimeField(null=True)
    requested_by = models.CharField(max_length=80, null=True)
    completed_by = models.CharField(max_length=80, null=True)

    @property
    def completed(self):
        return bool(self.completed_on)
