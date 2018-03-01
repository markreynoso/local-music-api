"""Flask server to serve local band data."""
import json
import os

from app import create_app


config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()


# from flask import Flask


# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# db = SQLAlchemy(app)


# @app.route("/api/all")
# def all_bands():
#     """Base api rounte, return all bands."""
#     return "Welcome!"


# def populate_db():
#     """Populate db with band data."""
#     with open('./band_data.json') as d:
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


# populate_db()


# if __name__ == "__main__":
#     app.run()
