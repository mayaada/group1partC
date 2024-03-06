from flask import render_template, redirect, url_for
from flask import Blueprint

# about blueprint definition
order_page = Blueprint(
    'order_page',
    __name__,
    static_folder='static',
    static_url_path='/order_page',
    template_folder='templates'
)


# Routes
@order_page.route('/order_page')
def index():
    return render_template('order_page.html')
