#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        """
        Getter method for cities attribute.
        """
        city_list = []
        for city in list(storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
