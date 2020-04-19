from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    presentation = db.relationship('PresentationTime', backref='speaker_presentation',
                                   cascade="all,delete", lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    paper = db.relationship('Paper', backref='conference', cascade="all,delete", lazy='dynamic')

    def __repr__(self):
        return '<Conference {}>'.format(self.name)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.Text)
    presentation = db.relationship('PresentationTime', backref='rooms_presentation',
                                   cascade="all,delete", lazy='dynamic')

    def __repr__(self):
        return '<Room {}>'.format(self.name)


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text)
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    tag = db.relationship('Tag', backref='paper_tag', cascade="all,delete", lazy='dynamic')
    presentation = db.relationship('PresentationTime', backref='paper_presentation',
                                   cascade="all,delete", lazy='dynamic')

    def __repr__(self):
        return '<Paper {}>'.format(self.name)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'))

    def __repr__(self):
        return '<Tag {}>'.format(self.name)


class PresentationTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    speaker = db.Column(db.Integer, db.ForeignKey('user.id'))
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    def __repr__(self):
        return '<Presentation Time {}>'.format(self.id)
