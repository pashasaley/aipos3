from flask import request

from app.models import User, Conference, Room, PresentationTime, Paper, Tag
from app import db, app
import json


@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    response = []
    presentations = []
    for user in users:
        for item in user.presentation:
            presentations.append({
                'presentation_id': item.id,
                'presentation_start': str(item.start),
                'presentation_end': str(item.end)
            })
        response.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'presentations': presentations
        })
    return json.dumps(response)


@app.route('/user/<id_user>', methods=['GET'])
def get_user(id_user):
    user = User.query.get(id_user)
    presentations = []
    for item in user.presentation:
        presentations.append({
            'presentation_id': item.id,
            'presentation_start': str(item.start),
            'presentation_end': str(item.end)
        })
    response = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'presentations': presentations
    }
    return json.dumps(response)


@app.route('/user/<id_user>', methods=['DELETE'])
def delete_user(id_user):
    user = User.query.get(id_user)
    db.session.delete(user)
    db.session.commit()
    return


@app.route('/user/<id_user>', methods=['POST'])
def update_user(id_user):
    data = request.get_json()
    user = User.query.get(id_user)
    username = data['username']
    email = data['email']
    if username != '':
        user.username = username
    if email != '':
        user.email = email
    db.session.commit()
    return


@app.route('/user/add', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    email = data['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return


@app.route('/conference', methods=['GET'])
def get_all_conferences():
    conferences = Conference.query.all()
    response = []
    papers = []
    for conference in conferences:
        for item in conference.paper:
            papers.append({
                'paper_id': str(item.id),
                'paper_name': str(item.name),
                'paper_description': item.description
            })
        response.append({
            'id': conference.id,
            'name': conference.name,
            'start': str(conference.start),
            'end': str(conference.end),
            'papers': papers
        })
    return json.dumps(response)


@app.route('/conference/<id_conference>', methods=['GET'])
def get_conference(id_conference):
    conference = Conference.query.get(id_conference)
    papers = []
    for item in conference.paper:
        papers.append({
            'paper_id': item.id,
            'paper_name': item.name,
            'paper_description': item.description
        })
    response = {
        'id': conference.id,
        'name': conference.name,
        'start': str(conference.start),
        'end': str(conference.end),
        'papers': papers
    }
    return json.dumps(response)


@app.route('/conference/<id_conference>', methods=['DELETE'])
def delete_conference(id_conference):
    conference = Conference.query.get(id_conference)
    db.session.delete(conference)
    db.session.commit()
    return


@app.route('/conference/<id_conference>', methods=['GET', 'POST'])
def update_conference(id_conference):
    data = request.get_json()
    conference = Conference.query.get(id_conference)
    name = data['name']
    start = data['start']
    end = data['end']
    if name != '':
        conference.name = name
    if start != '':
        conference.start = start
    if end != '':
        conference.end = end
    db.session.commit()
    return


@app.route('/conference/add', methods=['POST'])
def add_conference():
    data = request.get_json()
    name = data['name']
    start = data['start']
    end = data['end']
    conference = Conference(name=name, start=start, end=end)
    db.session.add(conference)
    db.session.commit()
    return


@app.route('/room', methods=['GET'])
def get_all_rooms():
    rooms = Room.query.all()
    response = []
    presentations = []
    for room in rooms:
        for item in room.presentation:
            presentations.append({
                'presentation_id': item.id,
                'presentation_start': str(item.start),
                'presentation_end': str(item.end)
            })
        response.append({
            'id': room.id,
            'name': room.name,
            'location': room.location,
            'presentations': presentations
        })
    return json.dumps(response)


@app.route('/room/<id_room>', methods=['GET'])
def get_room(id_room):
    room = Room.query.get(id_room)
    presentations = []
    for item in room.presentation:
        presentations.append({
            'presentation_id': item.id,
            'presentation_start': str(item.start),
            'presentation_end': str(item.end)
        })
    response = {
        'id': room.id,
        'name': room.name,
        'location': room.location,
        'presentations': presentations
    }
    return json.dumps(response)


@app.route('/room/<id_room>', methods=['DELETE'])
def delete_room(id_room):
    room = Room.query.get(id_room)
    db.session.delete(room)
    db.session.commit()
    return


@app.route('/room/<id_room>', methods=['POST'])
def update_room(id_room):
    data = request.get_json()
    room = Room.query.get(id_room)
    name = data['name']
    location = data['location']
    if name != '':
        room.name = name
    if location != '':
        room.location = location
    db.session.commit()
    return


@app.route('/room/add', methods=['POST'])
def add_room():
    data = request.get_json()
    name = data['name']
    location = data['location']
    room = Room(name=name, location=location)
    db.session.add(room)
    db.session.commit()
    return


@app.route('/tag', methods=['GET'])
def get_all_tags():
    tags = Tag.query.all()
    response = []
    for tag in tags:
        paper = Paper.query.get(tag.paper_id)
        response.append({
            'id': tag.id,
            'name': tag.name,
            'paper_id': paper.id,
            'paper_name': paper.name,
            'paper_description': paper.description
        })
    return json.dumps(response)


@app.route('/tag/<id_tag>', methods=['GET'])
def get_tag(id_tag):
    tag = Tag.query.get(id_tag)
    paper = Paper.query.get(tag.paper_id)
    response = {
        'id': tag.id,
        'name': tag.name,
        'paper_id': paper.id,
        'paper_name': paper.name,
        'paper_description': paper.description
    }
    return json.dumps(response)


@app.route('/tag/<id_tag>', methods=['DELETE'])
def delete_tag(id_tag):
    tag = Tag.query.get(id_tag)
    db.session.delete(tag)
    db.session.commit()
    return


@app.route('/tag/<id_tag>', methods=['POST'])
def update_tag(id_tag):
    data = request.get_json()
    tag = Tag.query.get(id_tag)
    name = data['name']
    paper_name = data['paper_name']
    if name != '':
        tag.name = name
    if paper_name != '':
        tag.paper_id = Paper.query.filter_by(name=paper_name).first().id
    db.session.commit()
    return


@app.route('/tag/add', methods=['POST'])
def add_tag():
    data = request.get_json()
    name = data['name']
    paper_name = data['paper_name']
    tag = Tag(name=name, paper_id=Paper.query.filter_by(name=paper_name).first().id)
    db.session.add(tag)
    db.session.commit()
    return


@app.route('/paper', methods=['GET'])
def get_all_papers():
    papers = Paper.query.all()
    response = []
    for paper in papers:
        conf = Conference.query.get(paper.conference_id)
        response.append({
            'id': paper.id,
            'name': paper.name,
            'description': paper.description,
            'conf_id': conf.id,
            'conf_name': conf.name,
            'conf_start': str(conf.start),
            'conf_end': str(conf.end),
        })
    return json.dumps(response)


@app.route('/paper/<id_paper>', methods=['GET'])
def get_paper(id_paper):
    paper = Paper.query.get(id_paper)
    conf = Conference.query.get(paper.conference_id)
    response = {
        'id': paper.id,
        'name': paper.name,
        'description': paper.description,
        'conf_id': conf.id,
        'conf_name': conf.name,
        'conf_start': str(conf.start),
        'conf_end': str(conf.end),
    }
    return json.dumps(response)


@app.route('/paper/<id_paper>', methods=['DELETE'])
def delete_paper(id_paper):
    paper = Paper.query.get(id_paper)
    db.session.delete(paper)
    db.session.commit()
    return


@app.route('/paper/<id_paper>', methods=['PUT'])
def update_paper(id_paper):
    data = request.get_json()
    paper = Paper.query.get(id_paper)
    name = data['name']
    description = data['description']
    conference_name = data['conference_name']
    if name != '':
        paper.name = name
    if description != '':
        paper.description = description
    if conference_name != '':
        paper.conference_id = Conference.query.filter_by(name=conference_name).first().id
    db.session.commit()
    return


@app.route('/paper/add', methods=['POST'])
def add_paper():
    data = request.get_json()
    name = data['name']
    description = data['description']
    conference_name = data['conference_name']
    paper = Paper(name=name, description=description,
                  conference_id=Conference.query.filter_by(name=conference_name).first().id)
    db.session.add(paper)
    db.session.commit()
    return


@app.route('/presentation', methods=['GET'])
def get_all_pr_times():
    pr_times = PresentationTime.query.all()
    response = []
    for pr_time in pr_times:
        paper = Paper.query.get(pr_time.paper_id)
        speaker = User.query.get(pr_time.speaker)
        room = Room.query.get(pr_time.room_id)
        response.append({
            'id': pr_time.id,
            'start': str(pr_time.start),
            'end': str(pr_time.end),
            'paper_id': paper.id,
            'paper_name': paper.name,
            'paper_description': paper.description,
            'room_id': room.id,
            'room_name': room.name,
            'room_location': room.location,
            'speaker_id': speaker.id,
            'speaker_username': speaker.username,
            'speaker_email': speaker.email
        })
    return json.dumps(response)


@app.route('/presentation/<id_pr_time>', methods=['GET'])
def get_pr_time(id_pr_time):
    pr_time = PresentationTime.query.get(id_pr_time)
    paper = Paper.query.get(pr_time.paper_id)
    speaker = User.query.get(pr_time.speaker)
    room = Room.query.get(pr_time.room_id)
    response = {
        'id': pr_time.id,
        'start': str(pr_time.start),
        'end': str(pr_time.end),
        'paper_id': paper.id,
        'paper_name': paper.name,
        'paper_description': paper.description,
        'room_id': room.id,
        'room_name': room.name,
        'room_location': room.location,
        'speaker_id': speaker.id,
        'speaker_username': speaker.username,
        'speaker_email': speaker.email
    }
    return json.dumps(response)


@app.route('/presentation/<id_pr_time>', methods=['DELETE'])
def delete_pr_time(id_pr_time):
    pr_time = PresentationTime.query.get(id_pr_time)
    db.session.delete(pr_time)
    db.session.commit()
    return


@app.route('/presentation/<id_pr_time>', methods=['PUT'])
def update_pr_time(id_pr_time):
    data = request.get_json()
    pr_time = PresentationTime.query.get(id_pr_time)
    start = data['start']
    end = data['end']
    room_name = data['room_name']
    speaker_name = data['speaker_name']
    paper_name = data['paper_name']
    if start != '':
        pr_time.start = start
    if end != '':
        pr_time.end = end
    if room_name != '':
        pr_time.room_id = Room.query.filter_by(name=room_name).first().id
    if speaker_name != '':
        pr_time.speaker = User.query.filter_by(username=speaker_name).first().id
    if paper_name != '':
        pr_time.paper_id = Paper.query.filter_by(name=paper_name).first().id
    db.session.commit()
    return


@app.route('/presentation/add', methods=['POST'])
def add_pr_time():
    data = request.get_json()
    start = data['start']
    end = data['end']
    room_name = data['room_name']
    speaker_name = data['speaker_name']
    paper_name = data['paper_name']
    pr_time = PresentationTime(start=start, end=end,
                               speaker=User.query.filter_by(username=speaker_name).first().id,
                               room_id=Room.query.filter_by(name=room_name).first().id,
                               paper_id=Paper.query.filter_by(name=paper_name).first().id)
    db.session.add(pr_time)
    db.session.commit()
    return


if __name__ == '__main__':
    app.run(debug=True, port='5001')
