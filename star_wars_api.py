import requests

from entity.person import Person
from entity.planet import Planet
from entity.starship import Starship


class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev'

    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}/api/{entity}/{entity_id}/"
        respoune = requests.get(url)

        if respoune.status_code == 200:
            return respoune.json()
        else:
            raise ValueError(f"Неможливо отримати дані для сутності {entity} з індетефікатором {entity_id}")

    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)
    def get_planet(self, planet_id):
        planet_dict = self.get_entity('planets', planet_id)
        return Planet(planet_dict)
    def get_starship(self, starship_id):
        starship_dict = self.get_entity('starships', starship_id)
        return Starship(starship_dict)