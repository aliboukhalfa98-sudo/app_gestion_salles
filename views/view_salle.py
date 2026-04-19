import customtkinter as ctk
from tkinter import messagebox
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=10)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=10)

        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type")
        self.label_type.grid(row=2, column=0, padx=10, pady=10)
        self.entry_type = ctk.CTkEntry(self.cadreInfo)
        self.entry_type.grid(row=2, column=1, padx=10, pady=10)

        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)

 # Cadre Actions
        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )
            ok, msg = self.service_salle.ajouter_salle(salle)

            if ok:
                messagebox.showinfo("Succès", msg)
            else:
                messagebox.showerror("Erreur", msg)

        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )

            ok, msg = self.service_salle.modifier_salle(salle)

            if ok:
                messagebox.showinfo("Succès", msg)
            else:
                messagebox.showerror("Erreur", msg)

        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier")

    def supprimer_salle(self):
        code = self.entry_code.get()

        if not code:
            messagebox.showerror("Erreur", "Veuillez saisir le code de la salle")
            return

        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Succès", "Salle supprimée avec succès")

    def rechercher_salle(self):
        code = self.entry_code.get()

        if not code:
            messagebox.showerror("Erreur", "Veuillez saisir le code de la salle")
            return

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, str(salle.capacite))

        else:
            messagebox.showerror("Erreur", "Salle introuvable")


