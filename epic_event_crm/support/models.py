from django.db import models
from epic_event_crm.collaborator.models import Collaborator


class Support(models.Model):
    collaborateur = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name='supports')
