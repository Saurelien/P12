from django.db import models
"""from epic_event_crm.client.models import Client"""
from epic_event_crm.collaborator.models import Collaborator


"""
Un contrat est lié a un client qui est lié
au gestionnaire si le contrat est signé, le commercial met a jour le profil
du client souhaitant organisé un évènement
EDIT: decimal_places rend possible un float de deux chiffre après la virgule ( du bonus sans importance )
EDIT 2 DecimalField est une trouvaille qui permet d'indiquer a django que la base de donnée du contrat
va stocker une valeur précise, dans mon cas ce sera la variable total_cost & remaining_amount
"""


class Contrat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # rajouter le client car sans cela pas de lien faisable
    commercial_contact = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut_contrat = models.BooleanField(default=False)  # True si le contrat est signé, False sinon

    def save(self, *args, **kwargs):
        if self.commercial_contact.role != 'commercial':
            raise ValueError("Le contact commercial doit avoir le rôle du département commercial.")
        super().save(Contrat, *args, **kwargs)
