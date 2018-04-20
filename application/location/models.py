from application import db
from application.models import Base

class Location(Base):

    __tablename__ = "location"
    
    address = db.Column(db.String(144))
    city = db.Column(db.String(144))

   
    
    def __init__(self, name):
        self.name = name