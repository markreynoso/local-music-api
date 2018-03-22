"""Initialize app."""
import json
from flask import abort, jsonify, request

from flask_api import FlaskAPI

# from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

from instance.config import app_config


# db = SQLAlchemy()
mongo = PyMongo()


def create_app(config_name):
    """Configuration settings."""
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    mongo.init_app(app)

    # from .models import Band

    @app.route('/api/bands/', methods=['GET', 'POST'])
    def get_all_bands():
        if request.method == 'POST':
            name = request.data.get('name')
            albums = request.data.get('albums')
            location = request.data.get('location')
            styles = request.data.get('styles')
            websites = request.data.get('websites')
            bio = request.data.get('bio')
            if name:
                band = mongo.db.bands
                band.insert({'name': name,
                             'albums': albums,
                             'location': location,
                             'styles': styles,
                             'websites': websites,
                             'bio': bio
                             })
                response = jsonify({'name': band.name,
                                    'albums': band.albums,
                                    'location': band.location,
                                    'styles': band.styles,
                                    'websites': band.websites,
                                    'bio': band.bio,
                                    })
                response.status_code = 201
                return response
        else:
            bands = mongo.db.bands
            output = []
            for band in bands.find():
                output.append({'name': band['name'],
                               'albums': band['albums'],
                               'location': band['location'],
                               'styles': band['styles'],
                               'websites': band['websites'],
                               'bio': band['bio']
                               })
            response = jsonify(output)
            response.status_code = 201
            return response

    @app.route('/api/bands/search/', methods=['GET', 'PUT', 'DELETE'])
    def bands_name():
        band_name = request.args.get('name')

        bands = mongo.db.bands
        band_search = bands.find_one({'name': band_name})
        if not band_search:
            abort(404)

        if request.method == 'DELETE':
            band_search.delete()
            return {"message":
                    "{} deleted successfully".format(band_search.id)}, 200

        elif request.method == 'PUT':
            band_search['name'] = request.data.get('name')
            band_search['albums'] = request.data.get('albums')
            band_search['location'] = request.data.get('location')
            band_search['styles'] = request.data.get('styles')
            band_search['websites'] = request.data.get('websites')
            band_search['bio'] = request.data.get('bio')
            response = jsonify({
                'name': band_search['name'],
                'albums': band_search['albums'],
                'location': band_search['location'],
                'styles': band_search['styles'],
                'websites': band_search['websites'],
                'bio': band_search['bio'],
            })
            response.status_code = 200
            return response
        else:
            response = jsonify({
                'name': band_search['name'],
                'albums': band_search['albums'],
                'location': band_search['location'],
                'styles': band_search['styles'],
                'websites': band_search['websites'],
                'bio': band_search['bio'],
            })
            response.status_code = 200
            return response

    @app.route('/api/bands/match/', methods=['GET'])
    def bands_styles():
        styles = request.args.get('styles').split('_')
        bands = mongo.db.bands
        if len(styles) <= 1:
            band_search = bands.find({'styles': styles[0]})
            if not band_search:
                abort(404)
            results = []
            for band in band_search:
                results.append({'name': band['name'],
                                'albums': band['albums'],
                                'location': band['albums'],
                                'styles': band['styles'],
                                'websites': band['websites'],
                                'bio': band['bio'],
                                })
            response = jsonify(results)
            response.status_code = 200
            return response
        else:
            results = []
            output = bands.find({'styles': {'$all': styles}})
            for band in output:
                results.append({'name': band['name'],
                                'albums': band['albums'],
                                'location': band['albums'],
                                'styles': band['styles'],
                                'websites': band['websites'],
                                'bio': band['bio'],
                                })
            response = jsonify(results)
            response.status_code = 200
            return response


    # @app.route('/api/bands/load/', methods=['GET'])
    # def bands_load():
    #     with open('band_data.json') as d:
    #         the_data = json.load(d)
    #         for band in the_data:
    #             entry = Band(band,
    #                          the_data[band]['albums'],
    #                          the_data[band]['location'],
    #                          the_data[band]['styles'],
    #                          the_data[band]['websites'],
    #                          the_data[band]['bio'])
    #             db.session.add(entry)
    #             db.session.commit()
    #     return 'thanks'

    # @app.route('/api/bands/', methods=['GET', 'POST'])
    # def bands():
    #     if request.method == 'POST':
    #         name = request.data.get('name')
    #         albums = request.data.get('albums')
    #         location = request.data.get('location')
    #         styles = request.data.get('styles')
    #         websites = request.data.get('websites')
    #         bio = request.data.get('bio')
    #         if name:
    #             band = Band(name=name,
    #                         albums=albums,
    #                         location=location,
    #                         styles=styles,
    #                         webites=websites,
    #                         bio=bio
    #                         )
    #             band.save()
    #             response = jsonify({
    #                 'id': band.id,
    #                 'name': band.name,
    #                 'location': band.location,
    #                 'styles': band.styles,
    #                 'websites': band.websites,
    #                 'bio': band.bio,
    #             })
    #             response.status_code = 201
    #             return response
    #     else:
    #         bands = Band.get_all()
    #         results = []

    #         for band in bands:
    #             obj = {
    #                 'id': band.id,
    #                 'name': band.name,
    #                 'albums': band.albums,
    #                 'location': band.location,
    #                 'styles': band.styles,
    #                 'websites': band.websites,
    #                 'bio': band.bio
    #             }
    #             results.append(obj)
    #         response = jsonify(results)
    #         response.status_code = 200
    #         return response

    # @app.route('/api/bands/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    # def bands_manipulation(id, **kwargs):
    #     band_search = Band.query.filter_by(id=id).first()
    #     if not band_search:
    #         abort(404)

    #     if request.method == 'DELETE':
    #         band_search.delete()
    #         return {"message":
    #                 "{} deleted successfully".format(band_search.id)}, 200

    #     elif request.method == 'PUT':
    #         band_search.name = request.data.get('name')
    #         band_search.albums = request.data.get('albums')
    #         band_search.location = request.data.get('location')
    #         band_search.styles = request.data.get('styles')
    #         band_search.websites = request.data.get('websites')
    #         band_search.bio = request.data.get('bio')
    #         band_search.save()
    #         response = jsonify({
    #             'id': band_search.id,
    #             'name': band_search.name,
    #             'location': band_search.location,
    #             'styles': band_search.styles,
    #             'websites': band_search.websites,
    #             'bio': band_search.bio,
    #         })
    #         response.status_code = 200
    #         return response
    #     else:
    #         response = jsonify({
    #             'id': band_search.id,
    #             'name': band_search.name,
    #             'location': band_search.location,
    #             'styles': band_search.styles,
    #             'websites': band_search.websites,
    #             'bio': band_search.bio,
    #         })
    #         response.status_code = 200
    #         return response

    # @app.route('/api/bands/search/', methods=['GET', 'PUT', 'DELETE'])
    # def bands_search():
    #     band_name = request.args.get('name')
    #     # band_location = request.args.get('location')
    #     # band_styles = request.args.get('styles')

    #     import pdb; pdb.set_trace()
    #     band_search = Band.query.filter_by(bands.data['name'].astext == band_name).first()
    #     if not band_search:
    #         abort(404)

    #     if request.method == 'DELETE':
    #         band_search.delete()
    #         return {"message":
    #                 "{} deleted successfully".format(band_search.id)}, 200

    #     elif request.method == 'PUT':
    #         band_search.name = request.data.get('name')
    #         band_search.albums = request.data.get('albums')
    #         band_search.location = request.data.get('location')
    #         band_search.styles = request.data.get('styles')
    #         band_search.websites = request.data.get('websites')
    #         band_search.bio = request.data.get('bio')
    #         band_search.save()
    #         response = jsonify({
    #             'id': band_search.id,
    #             'name': band_search.name,
    #             'location': band_search.location,
    #             'styles': band_search.styles,
    #             'websites': band_search.websites,
    #             'bio': band_search.bio,
    #         })
    #         response.status_code = 200
    #         return response
    #     else:
    #         response = jsonify({
    #             'id': band_search.id,
    #             'name': band_search.name,
    #             'location': band_search.location,
    #             'styles': band_search.styles,
    #             'websites': band_search.websites,
    #             'bio': band_search.bio,
    #         })
    #         response.status_code = 200
    #         return response

    # @app.route('/api/bands/load/', methods=['GET'])
    # def bands_load():
    #     with open('band_data.json') as d:
    #         the_data = json.load(d)
    #         for band in the_data:
    #             entry = Band(band,
    #                          the_data[band]['albums'],
    #                          the_data[band]['location'],
    #                          the_data[band]['styles'],
    #                          the_data[band]['websites'],
    #                          the_data[band]['bio'])
    #             db.session.add(entry)
    #             db.session.commit()
    #     return 'thanks'

    # <----------- use only to load db ------------>
    # @app.route('/api/bands/load/', methods=['GET'])
    # def load_db_bands():
    #     band = mongo.db.bands
    #     with open('band_data.json') as d:
    #         the_data = json.load(d)
    #         for entry in the_data:
    #             band.insert({
    #                 'name': entry.lower(),
    #                 'albums': the_data[entry]['albums'],
    #                 'location': the_data[entry]['location'].lower(),
    #                 'styles': the_data[entry]['styles'],
    #                 'websites': the_data[entry]['websites'],
    #                 'bio': the_data[entry]['bio']
    #             })
    #     return 'Thanks!'

    return app
