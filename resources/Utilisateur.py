from flask import request
from flask_restful import Resource
from Model import db, Utilisateur, UtilisateurSchema


utilisateurs_schema = UtilisateurSchema()

class UtilisateurResource(Resource):
    def get(self):
        utilisateurs = Utilisateur.query.all()
        utilisateurs = utilisateurs_schema.dump(utilisateurs).data
        return {'status': 'success', 'data': utilisateurs}, 200