from models.db import get_session
from models.models import User, Progress, Mission, Leaderboard
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError

def register_user(username, password, email):
    session = get_session()
    password_hash = pbkdf2_sha256.hash(password)
    user = User(username=username, password_hash=password_hash, email=email)
    session.add(user)
    try:
        session.commit()
        # Create initial progress
        progress = Progress(user_id=user.id)
        session.add(progress)
        session.commit()
        return True, "Registration successful."
    except IntegrityError:
        session.rollback()
        return False, "Username or email already exists."

def authenticate_user(username, password):
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password_hash):
        return user
    return None

def get_user_progress(user_id):
    session = get_session()
    return session.query(Progress).filter_by(user_id=user_id).first()

def update_progress(user_id, stage=None, level=None, completed_missions=None, achievements=None, score=None, badges=None):
    session = get_session()
    progress = session.query(Progress).filter_by(user_id=user_id).first()
    if stage:
        progress.stage = stage
    if level:
        progress.level = level
    if completed_missions:
        progress.completed_missions = completed_missions
    if achievements:
        progress.achievements = achievements
    session.commit()
    if score or badges:
        user = session.query(User).filter_by(id=user_id).first()
        if score:
            user.score = score
        if badges:
            user.badges = badges
        session.commit()

def get_leaderboard(top_n=10):
    session = get_session()
    return session.query(User).order_by(User.score.desc()).limit(top_n).all()
