"""Models for local bands database."""
from app import db

from sqlalchemy.dialects.postgresql import JSON


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

    @staticmethod
    def get_all():
        """Return entire db."""
        return Band.query.all()

    def delete(self):
        """Delete db entry."""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Object representation for query."""
        return '<name {}>'.format(self.name)
