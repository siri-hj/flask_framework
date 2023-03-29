from flask import Blueprint, render_template, jsonify, request,current_app
from .common import random_num
from .redis_con import redis_store
from .models import User

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')

@admin.route('/valid_code')
def valid_vode():
    # 获取数据
    phone = request.args.get('phone')
    print(phone)

    try:
        # 生成四位随机数字字母作为验证码
        code = random_num()
        # 将验证码保存到redis中，第一个参数是key，第二个参数是value，第三个参数表示60秒后过期
        redis_store.set('{}'.format(phone), '{}'.format(code), 60)
        # 这里用输出验证码来代替短信发送验证码
        print(code)
        return jsonify(status="成功", msg="验证码发送成功")
    except Exception as e:
        return jsonify(status='失败', msg="验证码发送失败")

@admin.route('/user_check')
def admin_check():
    if request.method == 'GET':
        users = User.query.all()
        return render_template('user_check.html', users=users)