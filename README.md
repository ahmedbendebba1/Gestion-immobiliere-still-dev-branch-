
*******************

# Gestion-immobiliere
Projet de gestion immobilière avec API Rest 

# Installer les libraries 
1-Créer un environnement python pour installer les libraries <br>

```
python -m venv env<br>

```

2-Activer l'environnement<br> 

```
source env/bin/activate<br>

```
3-Installer les libraries<br>

```
pip install -r requirments.txt

```

# Créer une base de donnée Mysql :immo_db
1-créer une base de donnée immo_db dans le bash Mysql:<br>
2-Changer username et password dans config.py<br>

```
SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@localhost/immo_db"    exemple: "mysql://root:@localhost/immo_db")

```

 # Migrer les données
 
```
  python migrate.py db init
  python migrate.py db migrate 
  python migrate.py db upgrade
```

 # Executer 
 
```
 python run.py

```
*****
 
1-Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc… )<br>

```
http://127.0.0.1:5000/api/bienimmobiliers/{id_immobilière} 

```
```
Body :  {
            "nom" : "string",
            "description" : "string",
            "pieces" : int,
            "caracteristiques" : "string",
            "type_immo" : "string",
            "ville" :"string",
            "id_utilisateur" : "string"
        }
        
```
*****
        
2-Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)<br>

```
http://127.0.0.1:5000/api/utilisateurs

```

```
http://127.0.0.1:5000/api/utilisateurs/{id_utilisateurs} 

```
```
Body:    {
            "date_de_naissance": "1994-09-12T00:00:00",
            "id_utilisateur": "string",
            "nom": "string",
            "prenom": "string"
        }

```
*****
        
3-Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière : <br>

```
http://127.0.0.1:5000/api/bienimmobiliers/findByVille/{ville}

```
