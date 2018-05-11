from application import db
from application.danceclass import models


class UserDanceclass(db.Model):

    __tablename__ = "userdanceclass"
  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    danceclass_id = db.Column('danceclass_id', db.Integer, db.ForeignKey('danceclass.id'))
    account_id = db.Column('account_id', db.Integer, db.ForeignKey('account.id'))
    
    danceclass = db.relationship('Danceclass', foreign_keys=danceclass_id, backref="danceclass_id")
    account = db.relationship('User', foreign_keys=account_id, backref="account_id")

    def __init__(self, danceclass_id):
        self.danceclass_id = danceclass_id
       