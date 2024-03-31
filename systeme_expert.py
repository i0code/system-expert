import tkinter as tk
from tkinter import messagebox

class SystemeExpert:
    def __init__(self, fichier_symptomes, fichier_regles):
        # Initialisation du système expert
        self.fichier_symptomes = fichier_symptomes
        self.fichier_regles = fichier_regles
        self.charger_symptomes()
        self.charger_regles()

    def charger_symptomes(self):
        # Charger les symptômes depuis le fichier
        self.symptomes = {}
        with open(self.fichier_symptomes, 'r') as file:
            for index, line in enumerate(file, start=1):
                symptome = line.strip()
                self.symptomes[index] = symptome

    def charger_regles(self):
        # Charger les règles depuis le fichier
        self.regles = {}
        with open(self.fichier_regles, 'r') as file:
            for line in file:
                symptomes, panne = line.strip().split(':')
                symptomes_liste = list(map(int, symptomes.split(',')))
                self.regles[panne] = symptomes_liste

    def sauvegarder_regles(self):
        # Sauvegarder les règles dans le fichier
        with open(self.fichier_regles, 'w') as file:
            for panne, symptomes in self.regles.items():
                symptomes_str = ','.join(map(str, symptomes))
                file.write(f"{symptomes_str}:{panne}\n")

    def sauvegarder_symptomes(self):
        # Sauvegarder les symptômes dans le fichier
        with open(self.fichier_symptomes, 'w') as file:
            for index, symptome in self.symptomes.items():
                file.write(f"{symptome}\n")
        
        # Mettre à jour les règles dans le fichier des règles
        self.sauvegarder_regles()

    def ajouter_symptome(self, symptome):
        # Méthode pour ajouter un symptôme
        index = len(self.symptomes) + 1
        self.symptomes[index] = symptome
        self.sauvegarder_symptomes()

    def modifier_symptome(self, index, nouveau_symptome):
        # Méthode pour modifier un symptôme
        if index in self.symptomes:
            self.symptomes[index] = nouveau_symptome
            self.sauvegarder_symptomes()

    def supprimer_symptome(self, index):
        # Méthode pour supprimer un symptôme
        if index in self.symptomes:
            del self.symptomes[index]
            self.sauvegarder_symptomes()

    def diagnostiquer_panne(self, symptomes_entres):
        # Méthode pour diagnostiquer la panne en fonction des symptômes
        pannes_detectees = []
        for panne, symptomes in self.regles.items():
            if any(symptome in symptomes_entres for symptome in symptomes):
                pannes_detectees.append(panne)
        return pannes_detectees

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Système Expert de Diagnostic de Pannes")
        # Utilisation des noms de fichiers corrects
        self.systeme_expert = SystemeExpert("base_connaissances.txt", "regles.txt")  
        self.create_widgets()

    def create_widgets(self):
        self.label_symptomes = tk.Label(self, text="Symptômes observés :")
        self.label_symptomes.pack()

        self.checkboxes_symptomes = {}
        for num, symptome in self.systeme_expert.symptomes.items():
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self, text=symptome, variable=var)
            checkbox.pack(anchor=tk.W)
            self.checkboxes_symptomes[num] = var

        self.diagnostiquer_button = tk.Button(self, text="Diagnostiquer", command=self.diagnostiquer)
        self.diagnostiquer_button.pack()

    def diagnostiquer(self):
        symptomes_entres = [num for num, var in self.checkboxes_symptomes.items() if var.get() == 1]
        pannes_detectees = self.systeme_expert.diagnostiquer_panne(symptomes_entres)
        if pannes_detectees:
            messagebox.showinfo("Résultat du diagnostic", f"Pannes détectées : {', '.join(pannes_detectees)}")
        else:
            messagebox.showinfo("Résultat du diagnostic", "Aucune panne détectée.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
