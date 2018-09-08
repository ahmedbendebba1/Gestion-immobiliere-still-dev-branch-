from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Utilisateur(db.Model):
    _tablename_ = 'utilisateur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)
    prenom = db.Column(db.String(50), unique=True, nullable=False)
    date_de_naissance = db.Column(db.TIMESTAMP, nullable=False)
    
    def __init__(self, nom, prenom, date_de_naissance):
        self.nom = nom
        self.prenom =  prenom
        self.date_de_naissance = date_de_naissance


class UtilisateurSchema(ma.Schema):
    id = fields.Integer()
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    date_de_naissance = fields.DateTime()