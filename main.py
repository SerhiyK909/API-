from star_wars_api import StarWarsApi

api_client = StarWarsApi()

person = api_client.get_person(1)
print(f"Person name: {person.name}")
print(f"Person skin color: {person.skin_color}")


planet = api_client.get_planet(2)
print(f"Planet name: {planet.name}")
print(f"Planet rotation_period: {planet.rotation_period}")

starship = api_client.get_starship(3)
print(f"starship name: {starship.name}")
print(f"starship model: {starship.model}")