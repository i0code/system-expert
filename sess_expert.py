import tkinter as tk
from tkinter import messagebox
from systeme_expert import SystemeExpert  # Import de la classe SystemeExpert depuis le fichier systeme_expert.py

class SessionExpert(tk.Tk):
    def __init__(self, fichier_symptomes, fichier_regles):  # Modification pour accepter deux arguments
        super().__init__()
        self.title("Session de l'Expert")
        self.systeme_expert = SystemeExpert("base_connaissances.txt", "regles.txt")  # Passage des deux arguments
        self.create_widgets()

    def create_widgets(self):
        self.label_titre = tk.Label(self, text="Gestion des symptômes")
        self.label_titre.grid(row=0, column=0, columnspan=3)

        self.label_symptome = tk.Label(self, text="Symptôme :")
        self.label_symptome.grid(row=1, column=0, sticky=tk.E)

        self.symptome_entry = tk.Entry(self)
        self.symptome_entry.grid(row=1, column=1, padx=5, pady=5)

        self.ajouter_button = tk.Button(self, text="Ajouter", command=self.ajouter_symptome)
        self.ajouter_button.grid(row=1, column=2, padx=5, pady=5)

        self.listbox_symptomes = tk.Listbox(self)
        for index, symptome in self.systeme_expert.symptomes.items():
            self.listbox_symptomes.insert(tk.END, f"{index}: {symptome}")
        self.listbox_symptomes.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.label_selection = tk.Label(self, text="Sélectionnez un symptôme :")
        self.label_selection.grid(row=3, column=0, columnspan=3)

        self.selection_var = tk.StringVar(self)
        self.selection_var.set("Aucun")

        self.options_menu = tk.OptionMenu(self, self.selection_var, *["Aucun"] + [str(index) for index in self.systeme_expert.symptomes.keys()])
        self.options_menu.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.label_nouveau_symptome = tk.Label(self, text="Nouveau symptôme :")
        self.label_nouveau_symptome.grid(row=5, column=0, sticky=tk.E)

        self.nouveau_symptome_entry = tk.Entry(self)
        self.nouveau_symptome_entry.grid(row=5, column=1, padx=5, pady=5)

        self.modifier_button = tk.Button(self, text="Modifier", command=self.modifier_symptome)
        self.modifier_button.grid(row=5, column=2, padx=5, pady=5)

        self.supprimer_button = tk.Button(self, text="Supprimer", command=self.supprimer_symptome)
        self.supprimer_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

    def ajouter_symptome(self):
        symptome = self.symptome_entry.get().strip()
        if symptome:
            self.systeme_expert.ajouter_symptome(symptome)
            self.listbox_symptomes.insert(tk.END, f"{len(self.systeme_expert.symptomes)}: {symptome}")
            self.symptome_entry.delete(0, tk.END)

    def modifier_symptome(self):
        index = self.selection_var.get()
        nouveau_symptome = self.nouveau_symptome_entry.get().strip()
        if index != "Aucun" and nouveau_symptome:
            index = int(index)
            self.systeme_expert.modifier_symptome(index, nouveau_symptome)
            self.listbox_symptomes.delete(index - 1)
            self.listbox_symptomes.insert(index - 1, f"{index}: {nouveau_symptome}")
            self.nouveau_symptome_entry.delete(0, tk.END)

    def supprimer_symptome(self):
        index = self.selection_var.get()
        if index != "Aucun":
            index = int(index)
            self.systeme_expert.supprimer_symptome(index)
            self.listbox_symptomes.delete(index - 1)
            for i in range(index, len(self.systeme_expert.symptomes) + 1):
                self.listbox_symptomes.insert(i - 1, f"{i}: {self.systeme_expert.symptomes[i]}")
                self.listbox_symptomes.delete(i)

    def quitter(self):
        self.systeme_expert.sauvegarder_symptomes("base_connaissances.txt")
        self.destroy()

if __name__ == "__main__":
    app = SessionExpert("base_connaissances.txt", "fichier_regles.txt")  # Passage des deux arguments
    app.mainloop()
