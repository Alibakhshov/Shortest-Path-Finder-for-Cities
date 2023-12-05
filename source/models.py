from database import Base
from sqlalchemy import Column, Integer, String, Float


class City(Base):

    __tablename__ = 'City'
    properties = ('name', 'population', 'longitude', 'latitude', 'rank', 'state')

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    longitude = Column(Float)
    latitude = Column(Float)
    population = Column(Integer)
    rank = Column(Integer)
    state = Column(String)

    def __init__(self, **data):
        self.name = data['city']
        self.longitude = data['longitude']
        self.latitude = data['latitude']
        self.population = data.get('population', 0)
        self.rank = data('rank', 0)
        self.state = data('state', '')
        

    def __repr__(self):
        return self.name + ', ' + self.population
