"""Database migration settings."""
import os

from app import create_app, db
from app import models

from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager


app = create_app(config_name=os.getenv('APP_SETTINGS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# def populate_db():
#         """Populate db with band data."""
#         with open('./band_data.json') as d:
#             the_data = json.load(d)
#             for band in the_data:
#                 entry = Band(band,
#                              the_data[band]['albums'],
#                              the_data[band]['location'],
#                              the_data[band]['styles'],
#                              the_data[band]['websites'],
#                              the_data[band]['bio'])
#                 db.session.add(entry)
#                 db.session.commit()


# populate_db()

if __name__ == '__main__':
    manager.run()
