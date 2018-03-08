"""Initialize app."""
from flask import abort, jsonify, request

from flask_api import FlaskAPI

from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config


db = SQLAlchemy()


def create_app(config_name):
    """Configuration settings."""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import Band

    @app.route('/api/bands/', methods=['GET', 'POST'])
    def bands():
        if request.method == 'POST':
            name = request.data.get('name')
            albums = request.data.get('albums')
            location = request.data.get('location')
            styles = request.data.get('stylesa')
            websites = request.data.get('websites')
            bio = request.data.get('bio')
            if name:
                band = Band(name=name,
                            albums=albums,
                            location=location,
                            styles=styles,
                            webites=websites,
                            bio=bio
                            )
                band.save()
                response = jsonify({
                    'id': band.id,
                    'name': band.name,
                    'location': band.location,
                    'styles': band.styles,
                    'websites': band.websites,
                    'bio': band.bio,
                })
                response.status_code = 201
                return response
        else:
            bands = Band.get_all()
            results = []

            for band in bands:
                obj = {
                    'id': band.id,
                    'name': band.name,
                    'albums': band.albums,
                    'location': band.location,
                    'styles': band.styles,
                    'websites': band.websites,
                    'bio': band.bio
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/api/bands/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def bands_manipulation(id, **kwargs):
        band_search = Band.query.filter_by(id=id).first()
        if not band_search:
            abort(404)

        if request.method == 'DELETE':
            band_search.delete()
            return {"message":
                    "{} deleted successfully".format(band_search.id)}, 200

        elif request.method == 'PUT':
            band_search.name = request.data.get('name')
            band_search.albums = request.data.get('albums')
            band_search.location = request.data.get('location')
            band_search.styles = request.data.get('styles')
            band_search.websites = request.data.get('websites')
            band_search.bio = request.data.get('bio')
            band_search.save()
            response = jsonify({
                'id': band_search.id,
                'name': band_search.name,
                'location': band_search.location,
                'styles': band_search.styles,
                'websites': band_search.websites,
                'bio': band_search.bio,
            })
            response.status_code = 200
            return response
        else:
            response = jsonify({
                'id': band_search.id,
                'name': band_search.name,
                'location': band_search.location,
                'styles': band_search.styles,
                'websites': band_search.websites,
                'bio': band_search.bio,
            })
            response.status_code = 200
            return response

    @app.route('/api/bands/search/', methods=['GET', 'PUT', 'DELETE'])
    def bands_search():
        band_name = request.args.get('name')
        # band_location = request.args.get('location')
        # band_styles = request.args.get('styles')

        import pdb; pdb.set_trace()
        band_search = Band.query.filter_by(name=band_name).first()
        if not band_search:
            abort(404)

        if request.method == 'DELETE':
            band_search.delete()
            return {"message":
                    "{} deleted successfully".format(band_search.id)}, 200

        elif request.method == 'PUT':
            band_search.name = request.data.get('name')
            band_search.albums = request.data.get('albums')
            band_search.location = request.data.get('location')
            band_search.styles = request.data.get('styles')
            band_search.websites = request.data.get('websites')
            band_search.bio = request.data.get('bio')
            band_search.save()
            response = jsonify({
                'id': band_search.id,
                'name': band_search.name,
                'location': band_search.location,
                'styles': band_search.styles,
                'websites': band_search.websites,
                'bio': band_search.bio,
            })
            response.status_code = 200
            return response
        else:
            response = jsonify({
                'id': band_search.id,
                'name': band_search.name,
                'location': band_search.location,
                'styles': band_search.styles,
                'websites': band_search.websites,
                'bio': band_search.bio,
            })
            response.status_code = 200
            return response

    return app
