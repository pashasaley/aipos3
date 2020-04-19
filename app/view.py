from app import app
from flask import render_template

from app.rest import *


@app.route('/')
def hello_world():
    return render_template('home_page.html')


@app.route('/user', methods=['GET'])
def all_users():
    users = get_all_users()
    return render_template('all_users.html', users=users)


@app.route('/room', methods=['GET'])
def all_rooms():
    rooms = get_all_rooms()
    return render_template('all_rooms.html', rooms=rooms)


@app.route('/paper', methods=['GET'])
def all_papers():
    papers = get_all_papers()
    return render_template('all_papers.html', papers=papers)


@app.route('/conference', methods=['GET'])
def all_conferences():
    conferences = get_all_conferences()
    return render_template('all_conf.html', confs=conferences)


@app.route('/presentation', methods=['GET'])
def all_presentations():
    presentations = get_all_pr_times()
    return render_template('all_presentations.html', presentations=presentations)


@app.route('/tag', methods=['GET'])
def all_tags():
    tags = get_all_tags()
    return render_template('all_tags.html', tags=tags)


if __name__ == '__main__':
    app.run()
