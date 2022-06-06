""" Импорт библиотек """
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

""" Создание объекта """
app = Flask(__name__)





""" Создание путей """
@app.route('/')
@app.route('/home')
def index():
	return render_template("index.html")


@app.route('/Americano')
def americano():
	return render_template("Americano.html")


@app.route('/Anime')
def anime():
	return render_template("anime.html")


@app.route('/Bicherin')
def bicherin():
	return render_template("Bicherin.html")


@app.route('/Breve')
def breve():
	return render_template("Breve.html")


@app.route('/Cappuccino')
def cappuccino():
	return render_template("Cappuccino.html")


@app.route('/Coffee')
def coffee():
	return render_template("coffee.html")


@app.route('/Con_panna')
def con_panna():
	return render_template("Con_panna.html")


@app.route('/Corretto')
def corretto():
	return render_template("Corretto.html")


@app.route('/Cosplay')
def cosplay():
	return render_template("cosplay.html")


@app.route('/Doppio')
def doppio():
	return render_template("Doppio.html")


@app.route('/Espresso')
def espresso():
	return render_template("Espresso.html")


@app.route('/Flat_White')
def flat_White():
	return render_template("Flat_White.html")


@app.route('/Fredo')
def fredo():
	return render_template("Fredo.html")


@app.route('/Glasse')
def glasse():
	return render_template("Glasse.html")


@app.route('/Honey_Raf')
def honey_Raf():
	return render_template("Honey_Raf.html")


@app.route('/Irish')
def irish():
	return render_template("Irish.html")


@app.route('/Japan_coffee')
def japan_coffee():
	return render_template("japan_coffee.html")


@app.route('/Japan_tea')
def japan_tea():
	return render_template("japan_tea.html")


@app.route('/Latte')
def latte():
	return render_template("Latte.html")


@app.route('/Latte_Macchiato')
def latte_Macchiato():
	return render_template("Latte_Macchiato.html")


@app.route('/Macchiato')
def macchiato():
	return render_template("Macchiato.html")


@app.route('/Marochino')
def marochino():
	return render_template("Marochino.html")


@app.route('/Moccachino')
def moccachino():
	return render_template("Moccachino.html")


@app.route('/Raf_coffee')
def raf_coffee():
	return render_template("Raf_coffee.html")


@app.route('/Restaurant')
def restaurant():
	return render_template("restaurant.html")


@app.route('/Ristretto')
def ristretto():
	return render_template("Ristretto.html")


@app.route('/Romano')
def romano():
	return render_template("Romano.html")


@app.route('/Tea')
def tea():
	return render_template("tea.html")


@app.route('/Triplo')
def triplo():
	return render_template("Triplo.html")


@app.route('/Viennese_coffee')
def viennese_coffee():
	return render_template("Viennese_coffee.html")



""" Запуск сервера """
if __name__ == "__main__":
	app.run(debug=True)