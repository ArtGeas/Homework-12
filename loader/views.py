from flask import Blueprint, render_template, request, current_app
from loader.utils import save_uploaded_picture
from main.utils import PostHandler
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO, encoding='utf-8')

@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template('post_form.html')

@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "Ошибка загрузки"
    picture_path = save_uploaded_picture(picture)

    if not picture_path:
        logging.info(f'Файл {picture.filename} - не картинка')
        return 'Файл не является изображением'

    post_handler = PostHandler(current_app.config['POST_PATH'])
    new_post = {'pic': picture_path, 'content': content}
    error = post_handler.add_post(new_post)
    if result:
        logging.error(f'Ошибка загрузки поста: {error}')
        return 'Ошибка загрузки'

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
