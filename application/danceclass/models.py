from application import db
from application.models import Base

class Danceclass(Base):

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    sqlite_autoincrement=True

    def __init__(self, name):
        self.name = name
       # self.done = False
        