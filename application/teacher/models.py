from application import db
from application.models import Base

class Teacher(Base):

    __tablename__ = "teacher"
    
    descr = db.Column(db.String(144), nullable=False)

   # danceclass = db.relationship("Danceclass", backref='teacher', lazy=True)

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        
    
    def get_id(self):
        return self.id