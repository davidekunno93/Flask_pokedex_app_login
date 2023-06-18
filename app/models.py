# functions that you wish to incorporate in the route files

import requests
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

#creating the database
class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    team = db.relationship('Team', backref='author', lazy=True)

    def __init__(self, name, u_name, email, pw):
        self.name = name
        self.username = u_name
        self.email = email
        self.password = pw

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, pokemon):
        self.pokemon = pokemon
    
    def catch_pokemon(self):
        db.session.add(self)
        db.session.commit()


class Pokemon():
    def __init__(self, name):
        self.name = name.title()
        # url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # response = requests.get(url)
        # if response.ok:
        #     data = response.json()
    
    def test_data(self):
        url = (f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}/")
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return data
        else:
            print("The name specified is not in the Pokemon database")

# capture sprite URL
# sprite = data["sprites"]["front_shiny"]
    def sprite(self):
        self.test_data()
        data = self.test_data()
        sprite = data["sprites"]["front_shiny"]
        return sprite

# capture pokemon's name
# pokemon_name = data["name"].title()
    def pokemon_name(self):
        self.test_data()
        data = self.test_data()
        pokemon_name = data["name"].title()
        return f"*This Pokemon's name is: {pokemon_name}*"

# capture pokemon's XP
# pokemon_xp = data["base_experience"]
    def exp(self):
        self.test_data()
        data = self.test_data()
        pokemon_xp = data["base_experience"]
        return f"This Pokemon's XP is: {pokemon_xp}"

    def abilities(self):
        self.test_data()
        data = self.test_data()
        abilities = {}
        ability_list = data["abilities"]
        # abilities key is a list of indices > indices dict first key ability > ability dict {name: "", url: ""}
        for k in range(2):
            ability_name = data["abilities"][int(k)]["ability"]["name"].title()
            # response2 = url link to ability's details
            response2 = requests.get(data["abilities"][int(k)]["ability"]["url"])
            if response2.ok:
                data2 = response2.json()
                effect = data2["effect_entries"][1]["effect"]
                abilities[ability_name] = effect
        return abilities
    
    def moves(self):
        self.test_data()
        data = self.test_data()
        moves = {}
        move_list = data["moves"]
        for k in range(4):
            move_name = move_list[int(k)]["move"]["name"].title()
            response2 = requests.get(move_list[int(k)]["move"]["url"])
            if response2.ok:
                data2 = response2.json()
                move_power = data2["power"]
                moves[move_name] = move_power
        return moves
    
    def stats(self):
        self.test_data()
        data = self.test_data()
        stats = {}
        stats_list = data["stats"]
        stats["hp"] = stats_list[0]["base_stat"]
        stats["attack"] = stats_list[1]["base_stat"]
        stats["defense"] = stats_list[2]["base_stat"]
        return stats

    def pokedex(self):
        all_dict = {}
        print(self.pokemon_name())
        all_dict["name"] = self.name
        all_dict["sprite"] = self.sprite()
        all_dict["abilities"] = self.abilities()
        all_dict["moves"] = self.moves()
        all_dict["stats"] = self.stats()
        return all_dict