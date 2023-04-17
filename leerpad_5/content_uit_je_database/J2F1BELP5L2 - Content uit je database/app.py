from flask import Flask, render_template
import datetime
from peewee import MySQLDatabase, Model, CharField, IntegerField


app = Flask(__name__)

db = MySQLDatabase(
    'databank',
    user='root',
    password='',
    host='localhost',
    port=3306
)

class Onderwerpen(Model):
    name = CharField()
    description = CharField()
    image = CharField()

    class Meta:
        database = db


# @app.route('/')
# def footer():
#     date = datetime.datetime.now()
#     date = date.strftime("%d/%m/%Y")
#     return render_template('footer.html', date=date)


@app.route('/')
def Days_gone():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    game = Onderwerpen.select().where(Onderwerpen.name == "Days gone")
    Game_Description = game[0].description
    Image = game[0].image
    print (Image)
    return render_template('footer.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", date=date, Game_Description=Game_Description, image=Image)

@app.route('/Red_dead_redemption_2')
def Red_dead_redemption_2():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    game = Onderwerpen.select().where(Onderwerpen.name == "red dead redemption")
    Game_Description = game[0].description
    Image = game[0].image
    print (Image)
    return render_template('footer.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", date=date, Game_Description=Game_Description, image=Image)

@app.route('/Subnautica')
def Subnautica():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    game = Onderwerpen.select().where(Onderwerpen.name == "subnautica")
    Game_Description = game[0].description
    Image = game[0].image
    print (Image)
    return render_template('footer.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", date=date, Game_Description=Game_Description, image=Image)

@app.route('/the_sons_of_the_forest')
def the_sons_of_the_forest():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    game = Onderwerpen.select().where(Onderwerpen.name == "the sons of the forest")
    Game_Description = game[0].description
    Image = game[0].image
    print (Image)
    return render_template('footer.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", date=date, Game_Description=Game_Description, image=Image)

db.close()
