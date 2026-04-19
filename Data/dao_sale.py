import json
import mysql.connector

from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connection

    def insert_salle(self, salle):
        connection = self.get_connection()
        curseur = connection.cursor()

        requete = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)

        curseur.execute(requete, valeurs)
        connection.commit()

        curseur.close()
        connection.close()

    def update_salle(self, salle):
        connection = self.get_connection()
        curseur = connection.cursor()

        requete = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)

        curseur.execute(requete, valeurs)
        connection.commit()

        curseur.close()
        connection.close()

    def delete_salle(self, code):
        connection = self.get_connection()
        curseur = connection.cursor()

        requete = "DELETE FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))

        connection.commit()

        curseur.close()
        connection.close()

    def get_salle(self, code):
        connection = self.get_connection()
        curseur = connection.cursor()

        requete = "SELECT code, libelle, type, capacite FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))

        resultat = curseur.fetchone()

        curseur.close()
        connection.close()

        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
        return None