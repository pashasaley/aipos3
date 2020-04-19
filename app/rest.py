from app.models import User, Conference, Room, PresentationTime, Paper, Tag
from app import db


def get_all_users():
    users = User.query.all()
    response = []
    presentations = []
    for user in users:
        for item in user.presentation:
            presentations.append({
                'presentation_id': item.id,
                'presentation_start': item.start,
                'presentation_end': item.end
            })
        response.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'presentations': presentations
        })
    return response


def get_user(id_user):
    user = User.query.get(id_user)
    response = []
    presentations = []
    for item in user.presentation:
        presentations.append({
            'presentation_id': item.id,
            'presentation_start': item.start,
            'presentation_end': item.end
        })
    response.append({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'presentations': presentations
    })
    return response


def delete_user(id_user):
    user = User.query.get(id_user)
    db.session.delete(user)
    db.session.commit()


def update_user(id_user, data):
    user = User.query.get(id_user)
    username = data['username']
    email = data['email']
    if username != '':
        user.username = username
    if email != '':
        user.email = email
    db.session.commit()


def add_user(data):
    username = data['username']
    email = data['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()


def get_all_conferences():
    conferences = Conference.query.all()
    response = []
    papers = []
    for conference in conferences:
        for item in conference.paper:
            papers.append({
                'paper_id': item.id,
                'paper_name': item.name,
                'paper_description': item.description
            })
        response.append({
            'id': conference.id,
            'name': conference.name,
            'start': conference.start,
            'end': conference.end,
            'papers': papers
        })
    return response


def get_conference(id_conference):
    conference = Conference.query.get(id_conference)
    response = []
    papers = []
    for item in conference.paper:
        papers.append({
            'paper_id': item.id,
            'paper_name': item.name,
            'paper_description': item.description
        })
    response.append({
        'id': conference.id,
        'name': conference.name,
        'start': conference.start,
        'end': conference.end,
        'papers': papers
    })
    return response


def delete_conference(id_conference):
    conference = Conference.query.get(id_conference)
    db.session.delete(conference)
    db.session.commit()


def update_conference(id_conference, data):
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


def add_conference(data):
    name = data['name']
    start = data['start']
    end = data['end']
    conference = Conference(name=name, start=start, end=end)
    db.session.add(conference)
    db.session.commit()


def get_all_rooms():
    rooms = Room.query.all()
    response = []
    presentations = []
    for room in rooms:
        for item in room.presentation:
            presentations.append({
                'presentation_id': item.id,
                'presentation_start': item.start,
                'presentation_end': item.end
            })
        response.append({
            'id': room.id,
            'name': room.name,
            'location': room.location,
            'presentations': presentations
        })
    return response


def get_room(id_room):
    room = Room.query.get(id_room)
    response = []
    presentations = []
    for item in room.presentation:
        presentations.append({
            'presentation_id': item.id,
            'presentation_start': item.start,
            'presentation_end': item.end
        })
    response.append({
        'id': room.id,
        'name': room.name,
        'location': room.location,
        'presentations': presentations
    })
    return response


def delete_room(id_room):
    room = Room.query.get(id_room)
    db.session.delete(room)
    db.session.commit()


def update_room(id_room, data):
    room = Room.query.get(id_room)
    name = data['name']
    location = data['location']
    if name != '':
        room.name = name
    if location != '':
        room.location = location
    db.session.commit()


def add_room(data):
    name = data['name']
    location = data['location']
    room = Room(name=name, location=location)
    db.session.add(room)
    db.session.commit()


def get_all_tags():
    tags = Tag.query.all()
    response = []
    for tag in tags:
        paper = Paper.qeury.get(tag.paper_id)
        response.append({
            'id': tag.id,
            'username': tag.name,
            'paper_id': paper.id,
            'paper_name': paper.name,
            'paper_description': paper.description
        })
    return response


def get_tag(id_tag):
    tag = Tag.query.get(id_tag)
    response = []
    paper = Paper.qeury.get(tag.paper_id)
    response.append({
        'id': tag.id,
        'username': tag.name,
        'paper_id': paper.id,
        'paper_name': paper.name,
        'paper_description': paper.description
    })
    return response


def delete_tag(id_tag):
    tag = Tag.query.get(id_tag)
    db.session.delete(tag)
    db.session.commit()


def update_tag(id_tag, data):
    tag = Tag.query.get(id_tag)
    name = data['name']
    paper_id = int(data['paper_id'])
    if name != '':
        tag.name = name
    if paper_id != '':
        tag.paper_id = paper_id
    db.session.commit()


def add_tag(data):
    name = data['name']
    paper_id = int(data['paper_id'])
    tag = Tag(name=name, paper_id=paper_id)
    db.session.add(tag)
    db.session.commit()


def get_all_papers():
    papers = Paper.query.all()
    response = []
    for paper in papers:
        conf = Conference.qeury.get(paper.conference_id)
        response.append({
            'id': paper.id,
            'username': paper.name,
            'description': paper.description,
            'conf_id': conf.id,
            'conf_name': conf.name,
            'conf_start': conf.start,
            'conf_end': conf.end,
        })
    return response


def get_paper(id_paper):
    paper = Paper.query.get(id_paper)
    response = []
    conf = Conference.qeury.get(paper.conference_id)
    response.append({
        'id': paper.id,
        'username': paper.name,
        'description': paper.description,
        'conf_id': conf.id,
        'conf_name': conf.name,
        'conf_start': conf.start,
        'conf_end': conf.end,
    })
    return response


def delete_paper(id_paper):
    paper = Tag.query.get(id_paper)
    db.session.delete(paper)
    db.session.commit()


def update_paper(id_paper, data):
    paper = Tag.query.get(id_paper)
    name = data['name']
    description = data['description']
    conference_id = int(data['conference_id'])
    if name != '':
        paper.name = name
    if description != '':
        paper.description = description
    if conference_id != '':
        paper.conference_id = conference_id
    db.session.commit()


def add_paper(data):
    name = data['name']
    description = data['description']
    conference_id = int(data['conference_id'])
    paper = Paper(name=name, description=description, conference_id=conference_id)
    db.session.add(paper)
    db.session.commit()


def get_all_pr_times():
    pr_times = PresentationTime.query.all()
    response = []
    for pr_time in pr_times:
        paper = Conference.qeury.get(pr_time.paper_id)
        speaker = User.qeury.get(pr_time.speaker_id)
        room = Room.qeury.get(pr_time.room_id)
        response.append({
            'id': pr_time.id,
            'start': pr_time.start,
            'end': pr_time.end,
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
    return response


def get_pr_time(id_pr_time):
    pr_time = Paper.query.get(id_pr_time)
    response = []
    paper = Conference.qeury.get(pr_time.paper_id)
    speaker = User.qeury.get(pr_time.speaker_id)
    room = Room.qeury.get(pr_time.room_id)
    response.append({
        'id': pr_time.id,
        'start': pr_time.start,
        'end': pr_time.end,
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
    return response


def delete_pr_time(id_pr_time):
    pr_time = Tag.query.get(id_pr_time)
    db.session.delete(pr_time)
    db.session.commit()


def update_pr_time(id_pr_time, data):
    pr_time = Tag.query.get(id_pr_time)
    start = data['start']
    end = data['end']
    room_id = int(data['room_id'])
    speaker_id = int(data['speaker_id'])
    paper_id = int(data['paper_id'])
    if start != '':
        pr_time.start = start
    if end != '':
        pr_time.end = end
    if room_id != '':
        pr_time.room_id = room_id
    if speaker_id != '':
        pr_time.speaker = speaker_id
    if paper_id != '':
        pr_time.paper_id = paper_id
    db.session.commit()


def add_pr_time(data):
    start = data['start']
    end = data['end']
    room_id = int(data['room_id'])
    speaker_id = int(data['speaker_id'])
    paper_id = int(data['paper_id'])
    pr_time = PresentationTime(start=start, end=end, speaker=speaker_id,
                               room_id=room_id, paper_id=paper_id)
    db.session.add(pr_time)
    db.session.commit()
