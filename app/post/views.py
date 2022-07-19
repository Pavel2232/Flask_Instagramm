import logging

from flask import Blueprint, render_template, request, jsonify, abort
from app.config import loger_api
from app.constance import post_dao, comment_dao

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

logger = loger_api


@post_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    """Страница одного поста подробно"""
    post = post_dao.get_post_by_pk(post_id)
    if not post:
        abort(404)
    result_comment = comment_dao.get_comments_by_post_id(post_id)
    return render_template('post.html', result_comment=result_comment, post=post)


@post_blueprint.route("/search")
def post_find():
    """Страница с поиском"""
    s = request.args.get('s')
    if s == request.args.get(" "):
        return render_template('search.html')
    posts = post_dao.search_for_posts(s)
    return render_template('search.html', posts=posts)


@post_blueprint.route("/api/posts")
def api_posts_page():
    """API полный список постов в виде JSON-списка"""
    logging.info("Запрос всех поста")
    return jsonify(post_dao.get_data())


@post_blueprint.route("/api/posts/<int:post_id>")
def api_posts_id_page(post_id):
    """API возвращает один пост в виде JSON-словаря."""
    logging.info("Запрос 1 поста")
    for post in post_dao.get_data():
        if post["pk"] == post_id:
            return jsonify(post)
    return None
