import logging

from flask import Blueprint, render_template, request, current_app
from main.utils import PostHandler

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
  s = request.args.get('s')
  logging.info(f'Поиск: {s}')
  post_handler = PostHandler(current_app.config['POST_PATH'])
  posts = post_handler.search_posts(s)

  return render_template('post_list.html', posts=posts, substr=s)
