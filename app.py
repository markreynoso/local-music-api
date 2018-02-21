"""Flask server to serve local band data."""
import json
import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# from models import Band

from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
db = SQLAlchemy(app)


@app.route("/api/all")
def all_bands():
    """Base api rounte, return all bands."""
    return "Welcome!"


class Band(db.Model):
    """Band model."""

    __tablename__ = "bands"
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(120), nullable=False)
    # albums = db.Column(db.Text, nullable=True)
    # location = db.Column(db.String(120), nullable=False)
    # styles = db.Column(db.Text, nullable=False)
    # websites = db.Column(db.Text, nullable=True)
    # bio = db.Column(db.Text, nullable=True)
    name = db.Column(JSON)
    albums = db.Column(JSON)
    location = db.Column(JSON)
    styles = db.Column(JSON)
    websites = db.Column(JSON)
    bio = db.Column(JSON)

    def __init__(self, name, albums, location, styles, websites, bio):
        """Initialize model data."""
        self.name = name
        self.albums = albums
        self.location = location
        self.styles = styles
        self.websites = websites
        self.bio = bio

    def __repr__(self):
        """Object representation for query."""
        return '<name {}>'.format(self.name)


def populate_db():
    """Populate db with band data."""
    with open('./band_data.json') as d:
        the_data = json.load(d)
        for band in the_data:
            entry = Band(band,
                         the_data[band]['albums'],
                         the_data[band]['location'],
                         the_data[band]['styles'],
                         the_data[band]['websites'],
                         the_data[band]['bio'])
            db.session.add(entry)
            db.session.commit()


populate_db()


if __name__ == "__main__":
    app.run()
