from pokemon_battle.models import db

def clear_session():
    db.session.remove()
    db.drop_all()
    db.create_all()