from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhanghae3


# 메인
@app.route('/')
def home():
    return render_template('index.html')


# 로그인
@app.route('/login')
def login():
    return render_template('login.html')


# 회원가입
app.config["SECRET_KEY"] = "team2"


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        birthday = request.form['birthday']
        phone = request.form['phone']
        gender = request.form['gender']
        addres = request.form['addres']
        shop = request.form['shop']
        email = request.form['email']
        pw = request.form['pw']

        doc = {'lastname': lastname, 'firstname': firstname, 'birthday': birthday, 'phone': phone,
               'gender': gender, 'addres': addres, 'shop': shop, 'email': email, 'pw': pw}

        db.ikea.insert_one(doc)

        return jsonify({'msg': '회원가입이 완료되었습니다. 로그인을 진행해주세요.'})


# 위시리스트
@app.route('/favorite')
def favorite():
    return render_template('wishlist.html')


# 장바구니
@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
