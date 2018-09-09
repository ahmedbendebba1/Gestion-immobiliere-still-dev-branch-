*** Export HTML ***
*******************

# Gestion-immobiliere
Projet de gestion immobiliere avec API Rest 

# Installer les libraries 
1-Créer un environnement python pour installer les libraries <br>
python -m venv env<br>
2-Activer l'environnement<br> 
source env/bin/activate<br>
3-Installer les libraries<br>
pip install -r requirments.txt<br>


# Créer une base de donnée Mysql :immo_db
1-créer une base de donnée imm_db dans le bash Mysql:<br>
2-Changer username et password dans config.py<br>
 (SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@localhost/immo_db"    exemple: "mysql://root:@localhost/immo_db")<br>

 # Migrer les données
 1- python migrate.py db init<br>
 2- python migrate.py db migrate<br> 
 3- python migrate.py db upgrade<br> 

 # Executer 
 python run.py<br>
1-Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc… )<br>
URL: http://127.0.0.1:5000/api/bienimmobiliers/{id_immobilière} : Requete Put<br>
Body :  {
            "nom" : "Immobilière1",
            "description" : "Large appartement",
            "pieces" : 3,
            "caracteristiques" : "pieces larges lumineuses",
            "type_immo" : "Appartement",
            "ville" :"Paris",
            "id_utilisateur" : "Arnaud"
        }<br>
2-Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)<br>
URL: http://127.0.0.1:5000/api/utilisateurs : Requete Get<br>
******************************
URL : http://127.0.0.1:5000/api/utilisateurs/{id_utilisateurs} : Requete put<br>
Body:    {
            "date_de_naissance": "1994-09-12T00:00:00",
            "id_utilisateur": "string",
            "nom": "string",
            "prenom": "string"
        }
Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière : <br>
URL : http://127.0.0.1:5000/api/bienimmobiliers/findByVille/{ville}<br>

