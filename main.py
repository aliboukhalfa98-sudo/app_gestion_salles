from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
try:
    conn = dao.get_connection()
    print("Connexion MySQL réussie")
    conn.close()
except Exception as e:
    print("Erreur connexion :", e)

# Test ajout
s1 = Salle("S100", "Salle Test", "Classe", 25)
dao.insert_salle(s1)
print("Salle ajoutée")

# Test recherche
salle = dao.get_salle("S100")
if salle:
    print("Salle trouvée :")
    salle.afficher_infos()

# Test modification
s1.libelle = "Salle modifiée"
s1.type = "Laboratoire"
s1.capacite = 30
dao.update_salle(s1)
print("Salle modifiée")

# Test affichage toutes les salles
print("Liste des salles :")
liste = dao.get_salles()
for s in liste:
    s.afficher_infos()
    print("------")

# Test suppression
dao.delete_salle("S100")
print("Salle supprimée")