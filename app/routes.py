# importing app to route different web directories
from app import app
from flask import render_template, request, redirect, url_for
from .auth.forms import PokeForm
from .models import Pokemon
from flask_login import current_user, login_user, logout_user, login_required

# if url = localhost:5000/ call this function and return this
@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    form = PokeForm()
    if request.method == "POST":
        if form.validate():
            name = form.pokemon.data
            pokemon = Pokemon(name)
            pokedex = pokemon.pokedex()
            return render_template("pokedex.html", pokemon=pokedex)
    return render_template("index.html", form=form)

@app.route('/pokedex')
@login_required
def pokedex():
    return render_template("pokedex.html")

