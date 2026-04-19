from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

print("Liste des salles :")
for s in service.recuperer_salles():
    s.afficher_infos()
    print("------")

salle1 = Salle("S101", "Salle A", "Classe", 20)
ok, msg = service.ajouter_salle(salle1)
print(msg)

salle1.libelle = "Salle A modifiee"
salle1.type = "Bureau"
salle1.capacite = 15
ok, msg = service.modifier_salle(salle1)
print(msg)

s = service.rechercher_salle("S101")
if s:
    print("Salle trouvée :")
    s.afficher_infos()

service.supprimer_salle("S101")
print("Salle supprimée")