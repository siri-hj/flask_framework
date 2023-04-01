from app import db

class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    phone = db.Column(db.String(64))

class Imperssion(db.Model):
    #定义表名
    __tablename__ = 'impressions'
    #定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scenery = db.Column(db.Integer)
    animal = db.Column(db.Integer)
    impression_num = db.Column(db.Integer)
    user_id = db.Column(db.Integer, primary_key=True)