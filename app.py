from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

from resources.Utilisateur import UtilisateurResource, UtilisateurResourceParam
from resources.BienImmobilier import BienImmobilierResource, BienImmobilierResourceParam,BienImmobilierResourceSearch

#from resources.Utilis import UtilisateurResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(UtilisateurResource, '/utilisateurs')
api.add_resource(UtilisateurResourceParam, '/utilisateurs/<string:id_utilisateur>')
api.add_resource(BienImmobilierResource, '/bienimmobiliers')
api.add_resource(BienImmobilierResourceParam, '/bienimmobiliers/<int:id>')
api.add_resource(BienImmobilierResourceSearch, '/bienimmobiliers/findByVille/<string:ville>')


#api.add_resource(UtilisateurResource, '/bienimmob')

