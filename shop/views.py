from flask import render_template, session, request, redirect
from shop import app
from shop.models import Computers, Menu

SHOPPING_CART = 'cart_session_info'

@app.route('/')
@app.route('/shop/')
def main_page():
    try:
        print(session[SHOPPING_CART])
    except KeyError:
        print('no cart session')
    computers = Computers.query.all()
    return render_template('main_page.html', computers=computers)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    computer = Computers.query.get(product_id)
    menu = Menu.query.all()
    return render_template('product_page.html', product_id=product_id, computer=computer, menu=menu)


@app.route('/cart/')
def cart_page():
    return render_template('cart.html')


@app.route('/cart/clear/')
def clear_cart():
    session.clear()
    return redirect('/shop/')


@app.route('/cart/add/<int:comp_id>/')
def add_comp_to_cart(comp_id):
    if SHOPPING_CART not in session:
        session[SHOPPING_CART] = [{'id': comp_id, 'count': 1}]
    elif session[SHOPPING_CART]:
        if any(filter(lambda cart_item: cart_item['id'] == comp_id, session[SHOPPING_CART])):
            for cart_item in session[SHOPPING_CART]:
                if cart_item['id'] == comp_id:
                    cart_item['count'] += 1
        else:
            session[SHOPPING_CART].append({'id': comp_id, 'count': 1})
        session.modified = True
    return redirect('/shop/')


@app.route('/cart/decrease/<int:comp_id>/')
def decrease_comp_in_cart(comp_id):
    try:
        if session[SHOPPING_CART]:
            for cart_item in session[SHOPPING_CART]:
                if cart_item['id'] == comp_id:
                    if cart_item['count'] <= 1:
                        session[SHOPPING_CART].pop(session[SHOPPING_CART].index(cart_item))
                        #Check for delete last item in cart, if true clear session
                        if not session[SHOPPING_CART]:
                            return redirect('/cart/clear/')
                    else:
                        cart_item['count'] -= 1
            session.modified = True
        return redirect('/shop/')
    except KeyError as e:
        print(e)
