"""Models for local bands database."""
from app import db

from sqlalchemy.dialects.postgresql import JSONB


class Band(db.Model):
    """Band model."""

    __tablename__ = 'bands'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(120), nullable=False)
    # albums = db.Column(db.Text, nullable=True)
    # location = db.Column(db.String(120), nullable=True)
    # styles = db.Column(db.Text, nullable=True)
    # websites = db.Column(db.Text, nullable=True)
    # bio = db.Column(db.Text, nullable=True)
    name = db.Column(JSONB, nullable=False)
    albums = db.Column(JSONB)
    location = db.Column(JSONB)
    styles = db.Column(JSONB)
    websites = db.Column(JSONB)
    bio = db.Column(JSONB)

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
