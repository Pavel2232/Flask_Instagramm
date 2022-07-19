from flask import Blueprint, render_template

from app.constance import post_dao

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def page_index():
    """ Лента постов """
    post = post_dao.load_data()
    return render_template('index.html', posts=post)


@main_blueprint.route("/users/<username>")
def user_feed_page(username):
    """Страница пользователя с его постами"""
    post = post_dao.get_posts_all(username)
    return render_template('user-feed.html', userpost=post)
