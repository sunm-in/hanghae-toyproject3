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
@app.route('/register')
def register():
    return render_template('register.html')


# 위시리스트
@app.route('/favorite')
def favorite():
    return render_template('wishlist.html')


# 장바구니
@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)