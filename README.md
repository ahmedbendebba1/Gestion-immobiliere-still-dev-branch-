# Gestion-immobiliere
Projet de gestion immobiliere avec API Rest

# Installer les libraries 
1-Créer un environnement python pour installer les libraries
python -m venv env
2-Activer l'environnement 
source env/bin/activate
3-Installer les libraries
pip install -r requirments.txt


# Créer une base de donnée Mysql :immo_db
1-créer une base de donnée imm_db dans le bash Mysql:
2-Changer username et password dans config.py
 (SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@localhost/immo_db"    exemple: "mysql://root:@localhost/immo_db")

 # Migrer les données
 1- python migrate.py db init
 2- python migrate.py db migrate 
 3- python migrate.py db upgrade 
