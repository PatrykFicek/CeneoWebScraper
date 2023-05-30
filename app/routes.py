from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/extract')
def extract():
    return render_template("extract.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/author')
def author():
    return render_template("author.html")

@app.route('/product1')
def product1():
    return render_template("product1.html")

@app.route('/product2')
def product2():
    return render_template("product2.html")