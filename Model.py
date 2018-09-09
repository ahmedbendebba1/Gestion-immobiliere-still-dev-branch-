from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Utilisateur(db.Model):
    _tablename_ = 'utilisateur'
    
    
    id_utilisateur = db.Column(db.String(50),primary_key=True, index= True, unique=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_de_naissance = db.Column(db.TIMESTAMP, nullable=False)
    #utilisateur = db.relationship('Utilisateur',backref='bienimmobilier')
    
    #db.ForeignKeyConstraint(['id_utilisateur'],['bienimmobilier.id_utilisateur'])
    #utilisateur = db.relationship('Utilisateur', backref='bienimmobilier')
    def __init__(self, id_utilisateur,nom, prenom, date_de_naissance):
        self.id_utilisateur= id_utilisateur
        self.nom = nom
        self.prenom =  prenom
        self.date_de_naissance = date_de_naissance


class UtilisateurSchema(ma.Schema):
    id_utilisateur = fields.String()
    nom = fields.String(required=True)
    prenom = fields.String(required=True)
    date_de_naissance = fields.DateTime()



class BienImmobilier(db.Model):
    _tablename_ = 'bienimmobilier'
    
    __table_args__ = (
        db.ForeignKeyConstraint(['id_utilisateur'],['utilisateur.id_utilisateur']),
    )
    
    id = db.Column(db.Integer,primary_key=True)
    
    nom = db.Column(db.String(100), nullable=False, )
    description = db.Column(db.String(500), nullable=False)
    pieces = db.Column(db.Integer(), nullable=False)
    caracteristiques = db.Column(db.String(200), nullable=False)
    type_immo = db.Column(db.String(50), nullable=False)
    ville = db.Column(db.String(50), nullable=False,)
    id_utilisateur = db.Column(db.String(50) ,index=True, nullable=False  )
    #id_utilisateur = db.Column(db.String(50) , unique=True , nullable=False ,db.ForeignKey('utilisateur.id_utilisateur',ondelete='CASCADE') )
    
    #id_utilisateur = db.Column(db.String(50), nullable=False, index=True, unique= True)
    ##utilisateur = db.relationship('utilisateur',primaryjoin="and_(User.id==Address.user_id, ""Address.city=='Boston')", backref='bienimmobilier')
    utilisateur = db.relationship('Utilisateur', backref=db.backref('bienimmobilier'))


    
    def __init__(self, nom, description, pieces,caracteristiques, type_immo, ville, id_utilisateur):
        self.nom = nom
        self.description = description
        self.pieces = pieces
        self.caracteristiques = caracteristiques
        self.type_immo = type_immo
        self.ville =ville
        self.id_utilisateur = id_utilisateur

class BienImmobilierSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nom = fields.String(required=True)
    description = fields.String(required=True)
    pieces = fields.Integer(required=True)
    caracteristiques = fields.String(required=True)
    type_immo = fields.String(required=True)
    ville = fields.String(required=True)
    id_utilisateur = fields.String(required=True)