from flask import Flask, render_template

from models import computers, menu

app = Flask(__name__)


@app.route('/')
@app.route('/shop/')
def main_page():
    return render_template('main_page.html', computers=computers)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    return render_template('product_page.html', product_id=product_id, computers=computers, menu=menu)
