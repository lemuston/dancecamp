from application import db
from application.models import Base


class Danceclass(Base):

    #__tablename__ = "danceclass"

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    length = db.Column(db.Integer)
    descr = db.Column(db.String)

    sqlite_autoincrement=True

    def __init__(self, name, length, descr):
        self.name = name
        self.length = length
        self.descr = descr
        