from flask import Blueprint
from flask import render_template
from flask import request
from api.blockr import api

home_view = Blueprint('home_view', __name__)

@home_view.route('/')
@home_view.route('/index')
def home_controller():
    return render_template('home.html')


@home_view.route('/coin/', methods=['POST'])
def get_info():
    coin = request.values.get('coin')
    trans = request.values.get('trans')

    if request.method == 'POST':
        coin = api.Api(coin)
        return coin.block_info(trans)
    else:
        return 'Method not allowed'