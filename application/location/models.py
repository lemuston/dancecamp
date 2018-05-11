from application import db
from application.models import Base

class Location(Base):

    __tablename__ = "location"
    
    address = db.Column(db.String(144))
    city = db.Column(db.String(144))

   
    
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city