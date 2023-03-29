import flask
import datetime

app = flask.Flask(__name__)


@app.route('/')
def the_sons_of_the_forest():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    return flask.render_template('the_sons_of_the_forest.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", Picture="the_sons_of_the_forest.jpg", date=date)

@app.route('/Days_gone')
def Days_gone():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    return flask.render_template('Days_gone.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", Picture="days_gone.jpg", date=date)

@app.route('/Red_dead_redemption_2')
def Red_dead_redemption_2():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    return flask.render_template('Red_dead_redemption_2.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", Picture="red_dead_redemption.jpg", date=date)

@app.route('/Subnautica')
def Subnautica():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    return flask.render_template('Subnautica.html', Days_gone="Days_gone.html", Red_dead_redemption_2="Red_dead_redemption_2.html", Subnautica="Subnautica.html", the_sons_of_the_forest="the_sons_of_the_forest.html", Picture="Subnautica.jpg", date=date)

