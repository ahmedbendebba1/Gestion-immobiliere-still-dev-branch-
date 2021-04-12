from flask import request
from flask_restful import Resource
from Model import db, Utilisateur, UtilisateurSchema

utilisateur_schema= UtilisateurSchema()
utilisateurs_schema = UtilisateurSchema(many=True)

class UtilisateurResource(Resource):
    def get(self):
        utilisateurs = Utilisateur.query.all()
        utilisateurs = utilisateurs_schema.dump(utilisateurs).data
        return {'status': 'success', 'data': utilisateurs}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = utilisateur_schema.load(json_data)
        if errors:
            return errors, 422
        utilisateur = Utilisateur.query.filter_by(id_utilisateur=data['id_utilisateur']).first()
        if utilisateur:
            return {'message': 'Utilisateur already exists'}, 400
        utilisateur = Utilisateur(
            id_utilisateur = json_data['id_utilisateur'],
            nom = json_data['nom'],
            prenom = json_data['prenom'],
            date_de_naissance = json_data['date_de_naissance']
            )
        db.session.add(utilisateur)
        db.session.commit()
        result = utilisateur_schema.dump(utilisateur).data
        return { "status": 'success', 'data': result }, 201    


class UtilisateurResourceParam(Resource):
        def get(self, id_utilisateur):
            print (id_utilisateur)
            utilisateur = Utilisateur.query.filter_by(id_utilisateur=id_utilisateur)
            utilisateur = utilisateurs_schema.dump(utilisateur).data
            return {'status': 'success', 'data': utilisateur}, 200

        def put(self, id_utilisateur):
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400
            # Validate and deserialize input
            data, errors = utilisateur_schema.load(json_data)
            if errors:
                return errors, 422
            utilisateur = Utilisateur.query.filter_by(id_utilisateur=id_utilisateur).first()
            if not utilisateur:
                return {'message': 'Utilisateur does not exist'}, 400
            utilisateur.nom = data['nom']
            utilisateur.prenom = data['prenom']
            utilisateur.date_de_naissance = data['date_de_naissance']        
            db.session.commit()

            result = utilisateur_schema.dump(utilisateur).data

            return { "status": 'success', 'data': result }, 204

        def delete(self, id_utilisateur):
            utilisateur = Utilisateur.query.filter_by(id_utilisateur=id_utilisateur).delete()
            db.session.commit()
            result = utilisateur_schema.dump(utilisateur).data
            return { "status": 'success', 'data': result}, 204



            
