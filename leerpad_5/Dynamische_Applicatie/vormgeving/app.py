from flask import Flask, render_template
# import datetime
from peewee import MySQLDatabase, Model, CharField, IntegerField

app = Flask(__name__)

db = MySQLDatabase(
    'databank',
    user='root',
    password='',
    host='localhost',
    port=3306
)

class characters(Model):
    name = CharField()
    avatar = CharField()
    health = IntegerField()
    bio = CharField()
    color = CharField()
    attack = IntegerField()
    defense = IntegerField()
    weapon = CharField()
    armor = CharField()

    class Meta:
        database = db

# <img class="avatar" src="resources/images/bowser.">
 
@app.route('/')
def index():
    all = characters.select()
    number_characters = len(all)
    return render_template('index.html', image='images/bowser.jpg', character="character.html", characters=all, number_characters=number_characters)

@app.route('/<name>')
def character(name):
    character = characters.get(characters.name == name)
    return render_template('character.html', character=character)



db.close()