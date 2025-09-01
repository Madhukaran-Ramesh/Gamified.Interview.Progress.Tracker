from models.db import get_session
from models.models import Mission

def get_missions(stage, level):
    session = get_session()
    return session.query(Mission).filter_by(stage=stage, level=level).all()

def add_mission(name, description, stage, level, skill_type, is_timed=False, time_limit=0, hurdle=''):
    session = get_session()
    mission = Mission(
        name=name,
        description=description,
        stage=stage,
        level=level,
        skill_type=skill_type,
        is_timed=is_timed,
        time_limit=time_limit,
        hurdle=hurdle
    )
    session.add(mission)
    session.commit()
    return mission
