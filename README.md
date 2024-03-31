# système-expert
### Description
Le projet consiste en un système expert de diagnostic de pannes informatiques. Il comprend deux parties principales :
#### 1-Interface Utilisateur ('systeme_expert.py') : 
Cette interface permet à l'utilisateur de sélectionner les symptômes observés sur un ordinateur et de diagnostiquer les pannes potentielles.
#### 2-Interface de l'Expert ('sess_expert.py') : 
Cette interface est destinée à l'expert en informatique pour gérer les symptômes et les règles utilisés par le système expert.
#### Les fichiers de données nécessaires sont :
'base_connaissances.txt' : Contient une liste de symptômes observés sur un ordinateur.
'regles.txt' : Contient les règles qui déterminent les pannes possibles en fonction des symptômes observés.
### Utilisation
#### 1-Interface Utilisateur ('systeme_expert.py')
Exécutez le fichier 'systeme_expert.py'.
Sélectionnez les symptômes observés en cochant les cases correspondantes.
Cliquez sur le bouton "Diagnostiquer" pour obtenir le résultat du diagnostic.
#### 2-Interface de l'Expert ('sess_expert.py')
Exécutez le fichier 'sess_expert.py'.
Utilisez l'interface pour ajouter, modifier ou supprimer des symptômes.
Les règles sont automatiquement mises à jour dans le fichier 'regles.txt'.
