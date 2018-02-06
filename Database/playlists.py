from . import db


class Playlists(db.Model):
    PlaylistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), unique=True, nullable=False)

    def __str__(self):
        return '{}-{}'.format(self.PlaylistId, self.Name)
