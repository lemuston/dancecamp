from application import db
from application.models import Base


class Danceclass(Base):

    __tablename__ = "danceclass"

    teacher_id = db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'))
    location_id = db.Column('location_id', db.Integer, db.ForeignKey('location.id'))
    length = db.Column(db.Integer)
    descr = db.Column(db.String)

    teacher = db.relationship('Teacher', foreign_keys=teacher_id, backref="teacher")
    location = db.relationship('Location', foreign_keys=location_id, backref="location")

   # sqlite_autoincrement=True

    def __init__(self, name, length, descr, teacher_id, location_id):
        self.name = name
        self.length = length
        self.descr = descr
        self.teacher_id = teacher_id
        self.location_id = location_id
        