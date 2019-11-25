from flask import render_template
from shop import app
from shop.models import Computers, Menu


@app.route('/')
@app.route('/shop/')
def main_page():
    computers = Computers.query.all()
    return render_template('main_page.html', computers=computers)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    computer = Computers.query.get(product_id)
    menu = Menu.query.all()
    return render_template('product_page.html', product_id=product_id, computer=computer, menu=menu)
