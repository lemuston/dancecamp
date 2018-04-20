from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
   # __table_args__ = {'extend_existing': True} 
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    phone = db.Column(db.String(144))
    email = db.Column(db.String(100))
    

    #danceclass = db.relationship("Danceclass", backref='account', lazy=True)
  
    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]