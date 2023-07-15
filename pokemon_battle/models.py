from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    types = Column(String)  
    stats = Column(String)  
    abilities = Column(String)  
    moves = Column(String)

    def __repr__(self):
        return f"Pokemon(id={self.id}, name='{self.name}', types='{self.types}', stats='{self.stats}', abilities='{self.abilities}', moves='{self.moves}')"