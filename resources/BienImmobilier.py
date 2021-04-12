from flask import request
from flask_restful import Resource
from Model import db, BienImmobilier, BienImmobilierSchema

bienimmobilier_schema= BienImmobilierSchema()
bienimmobiliers_schema = BienImmobilierSchema(many=True)

class BienImmobilierResource(Resource):
    def get(self):
        bienimmobiliers = BienImmobilier.query.all()
        bienimmobiliers = bienimmobiliers_schema.dump(bienimmobiliers).data
        return {"satatus":"success", "data": bienimmobiliers}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = bienimmobilier_schema.load(json_data)
        if errors:
            return errors, 422
        bienimmobilier = BienImmobilier(
            nom = json_data['nom'],
            description = json_data['description'],
            pieces = json_data['pieces'],
            caracteristiques = json_data['caracteristiques'],
            type_immo = json_data['type_immo'],
            ville =json_data['ville'],
            id_utilisateur = json_data['id_utilisateur']
            )
        db.session.add(bienimmobilier)
        db.session.commit()
        result = bienimmobilier_schema.dump(bienimmobilier).data
        return { "status": 'success', 'data': result }, 201


class BienImmobilierResourceParam(Resource):
        def get(self,id):
            bienimmobiliers = BienImmobilier.query.filter_by(id=id)
            bienimmobiliers = bienimmobiliers_schema.dump(bienimmobiliers).data
            return {"satatus":"success", "data": bienimmobiliers}, 200

        def put(self, id):
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400
            # Validate and deserialize input
            data, errors = bienimmobilier_schema.load(json_data)
            if errors:
                return errors, 422
            bienimmobilier = BienImmobilier.query.filter_by(id=id).first()
            if not bienimmobilier:
                return {'message': 'Bien Immobilier does not exist'}, 400
            bienimmobilier.nom = data['nom']
            bienimmobilier.description = data['description']
            bienimmobilier.pieces = data['pieces']
            bienimmobilier.caracteristiques = data['caracteristiques']
            bienimmobilier.type_immo = data['type_immo']
            bienimmobilier.ville = data['ville']
            bienimmobilier.id_utilisateur = data['id_utilisateur']       
            db.session.commit()
            result = bienimmobilier_schema.dump(bienimmobilier).data
            return { "status": 'success', 'data': result }, 204


class BienImmobilierResourceSearch(Resource):
        def get(self,ville):
            bienimmobiliers = BienImmobilier.query.filter_by(ville=ville)
            bienimmobiliers = bienimmobiliers_schema.dump(bienimmobiliers).data
            return {"satatus":"success", "data": bienimmobiliers}, 200



