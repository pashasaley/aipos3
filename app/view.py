from app import app
from flask import render_template, request, redirect, url_for

from app.rest import *


@app.route('/')
def hello_world():
    return render_template('home_page.html')


@app.route('/user', methods=['GET'])
def all_users():
    users = get_all_users()
    return render_template('all_users.html', users=users)


@app.route('/user', methods=['POST'])
def delete_users():
    id_user = request.form['id_user']
    delete_user(id_user)
    return redirect(url_for('all_users'))


@app.route('/room', methods=['GET'])
def all_rooms():
    rooms = get_all_rooms()
    return render_template('all_rooms.html', rooms=rooms)


@app.route('/room', methods=['POST'])
def delete_rooms():
    id_room = request.form['id_room']
    delete_room(id_room)
    return redirect(url_for('all_rooms'))


@app.route('/paper', methods=['GET'])
def all_papers():
    papers = get_all_papers()
    return render_template('all_papers.html', papers=papers)


@app.route('/paper', methods=['POST'])
def delete_papers():
    id_paper = request.form['id_paper']
    delete_paper(id_paper)
    return redirect(url_for('all_papers'))


@app.route('/conference', methods=['GET'])
def all_conferences():
    conferences = get_all_conferences()
    return render_template('all_conf.html', confs=conferences)


@app.route('/conference', methods=['POST'])
def delete_conferences():
    id_conference = request.form['id_conference']
    delete_conference(id_conference)
    return redirect(url_for('all_conferences'))


@app.route('/presentation', methods=['GET'])
def all_presentations():
    presentations = get_all_pr_times()
    return render_template('all_presentations.html', presentations=presentations)


@app.route('/presentation', methods=['POST'])
def delete_presentations():
    id_pr_time = request.form['id_pr_time']
    delete_pr_time(id_pr_time)
    return redirect(url_for('all_presentations'))


@app.route('/tag', methods=['GET'])
def all_tags():
    tags = get_all_tags()
    return render_template('all_tags.html', tags=tags)


@app.route('/tag', methods=['POST'])
def delete_tags():
    id_tag = request.form['id_tag']
    delete_tag(id_tag)
    return redirect(url_for('all_tags'))


if __name__ == '__main__':
    app.run()
