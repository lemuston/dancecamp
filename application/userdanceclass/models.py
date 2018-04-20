from application import db


class UserDanceclass(db.Model):

    __tablename__ = "userdanceclass"
  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    danceclass_id = db.Column(db.Integer, db.ForeignKey('danceclass.id'), nullable=False)