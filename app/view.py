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


@app.route('/user/add', methods=['GET', 'POST'])
def add_users():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        data = {
            'username': name,
            'email': email
        }
        add_user(data)
        return redirect(url_for('all_users'))
    return render_template('add_user.html')


@app.route('/room', methods=['GET'])
def all_rooms():
    rooms = get_all_rooms()
    return render_template('all_rooms.html', rooms=rooms)


@app.route('/room', methods=['POST'])
def delete_rooms():
    id_room = request.form['id_room']
    delete_room(id_room)
    return redirect(url_for('all_rooms'))


@app.route('/room/add', methods=['GET', 'POST'])
def add_rooms():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        data = {
            'name': name,
            'location': location
        }
        add_room(data)
        return redirect(url_for('all_rooms'))
    return render_template('add_room.html')


@app.route('/paper', methods=['GET'])
def all_papers():
    papers = get_all_papers()
    return render_template('all_papers.html', papers=papers)


@app.route('/paper', methods=['POST'])
def delete_papers():
    id_paper = request.form['id_paper']
    delete_paper(id_paper)
    return redirect(url_for('all_papers'))


@app.route('/paper/add', methods=['GET', 'POST'])
def add_papers():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        conference_name = request.form['conf_name']
        data = {
            'name': name,
            'description': description,
            'conference_name': conference_name
        }
        add_paper(data)
        return redirect(url_for('all_papers'))
    confs = get_all_conferences()
    return render_template('add_paper.html', confs=confs)


@app.route('/conference', methods=['GET'])
def all_conferences():
    conferences = get_all_conferences()
    return render_template('all_conf.html', confs=conferences)


@app.route('/conference/add', methods=['GET', 'POST'])
def add_conferences():
    if request.method == 'POST':
        name = request.form['name']
        start = request.form['start']
        end = request.form['end']
        data = {
            'name': name,
            'start': start,
            'end': end
        }
        add_conference(data)
        return redirect(url_for('all_conferences'))
    return render_template('add_conf.html')


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


@app.route('/presentation/add', methods=['GET', 'POST'])
def add_presentations():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        speaker_name = request.form['speaker_name']
        paper_name = request.form['paper_name']
        room_name = request.form['room_name']
        data = {
            'start': start,
            'end': end,
            'speaker_name': speaker_name,
            'paper_name': paper_name,
            'room_name': room_name
        }
        add_pr_time(data)
        return redirect(url_for('all_presentations'))
    papers = get_all_papers()
    speakers = get_all_users()
    rooms = get_all_rooms()
    return render_template('add_pres.html', papers=papers, speakers=speakers, rooms=rooms)


@app.route('/tag', methods=['GET'])
def all_tags():
    tags = get_all_tags()
    return render_template('all_tags.html', tags=tags)


@app.route('/tag', methods=['POST'])
def delete_tags():
    id_tag = request.form['id_tag']
    delete_tag(id_tag)
    return redirect(url_for('all_tags'))


@app.route('/tag/add', methods=['GET', 'POST'])
def add_tags():
    if request.method == 'POST':
        name = request.form['name']
        paper_name = request.form['paper_name']
        data = {
            'name': name,
            'paper_name': paper_name
        }
        add_tag(data)
        return redirect(url_for('all_tags'))
    papers = get_all_papers()
    return render_template('add_tag.html', papers=papers)


if __name__ == '__main__':
    app.run()
