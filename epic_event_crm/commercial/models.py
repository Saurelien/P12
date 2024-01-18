from django.db import models
from epic_event_crm.collaborator.models import Collaborator


class Commercial(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name="commercial_collaborator")
