from flask import Blueprint, redirect, flash, render_template, request,current_app
from .models import User
from app import db

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('/user/login.html')
    user_name = request.form.get('name')
    user_password = request.form.get('password')
    user_exit = db.session.query(User).filter(User.name == user_name).all()
    if user_exit:
        for i in user_exit:
            if i.password == user_password:
                return render_template('/user/success.html')

        return render_template('/user/login.html')
    return "查询不到该用户"

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =='GET':
        return render_template('/user/register.html')
    user_name = request.form.get('name')
    user_password = request.form.get('password')
    user_phone = request.form.get('phone')

    #查找该手机是否已注册
    user_phones = db.session.query(User).filter(User.phone==user_phone).all()
    if user_phones:
        return "该手机号已被注册"

    user = User()
    user.name = user_name
    user.password = user_password
    user.phone = user_phone
    db.session.add(user)
    db.session.commit()
    return render_template('/user/success.html')

@user.route('/register')
def impression():
    kind = request.args.get('kind')
    print(kind)