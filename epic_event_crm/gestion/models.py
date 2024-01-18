from django.db import models
from epic_event_crm.collaborator.models import Collaborator


class Gestion(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name="gestion_collaborator")
