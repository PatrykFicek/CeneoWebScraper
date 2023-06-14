from app import app
from flask import render_template, request, redirect, url_for
from app.utils import get_element, selectors
from bs4 import BeautifulSoup
import requests
import json
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST','GET'])
def extract():
    if request.method == 'POST':
        product_code = request.form['product_id']
        return redirect(url_for('product', product_code=product_code))
    
        while(url):
                
            response = req.get(url)
            page = BeautifulSoup(response.text, 'html.parser')
            opinions = page.select("div.js_product-review")

            for opinion in opinions:
                single_opinion = {}
                for key, value in selectors.items():
                    single_opinion[key] = get_element(opinion, *value)
                all_opinions.append(single_opinion)
                
            try:    
                url = "https://www.ceneo.pl/"+get_element(page, "a.pagination__next", "href") 
            except TypeError:
                url = None

        try:    
            os.mkdir("./opinions")
        except FileExistsError:
            pass
            
        with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:    
            json.dump(all_opinions, jf ,indent = 4, ensure_ascii = False)
    
    return render_template('extract.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/author')
def author():
    return render_template('author.html')

@app.route('/product/<product_code>')
def product(product_code):
    return render_template('product.html', product_code=product_code)