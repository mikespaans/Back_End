from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


# laat vragen formulier zien
@app.route('/', methods=['GET'])
def index():
    return render_template(template_name_or_list='formulier_paniek.html')



# verwerk antwoorden paniek
@app.route("/resultaat_paniek", methods=["POST"])
def paniek():
    huisdier = request.form.get("huisdier", "")
    persoon = request.form.get("persoon", "")
    land = request.form.get("land", "")
    vervelen = request.form.get("vervelen", "")
    speelgoed = request.form.get("speelgoed", "")
    docent = request.form.get("docent", "")
    geld = request.form.get("geld", "")
    bezigheid = request.form.get("bezigheid", "")

    return render_template(template_name_or_list='resultaat_paniek.html', huisdier=huisdier, persoon=persoon, land=land, vervelen=vervelen, speelgoed=speelgoed, docent=docent, geld=geld, bezigheid=bezigheid)


# verwerk antwoorden onkunde

@app.route("/resultaat_onkunde", methods=["POST"])
def onkunde():
    willen_kunnen = request.form.get("willen_kunnen", "")
    persoon_opschieten = request.form.get("persoon_opschieten", "")
    favoriete_getal = request.form.get("favoriete_getal", "")
    vakantie_gaan = request.form.get("vakantie_gaan", "")
    beste_eigenschap = request.form.get("beste_eigenschap", "")
    slechtste_eigenschap = request.form.get("slechtste_eigenschap", "")
    ergste_overkomen = request.form.get("ergste_overkomen", "")
    return render_template(template_name_or_list='resultaat_onkunde.html', willen_kunnen=willen_kunnen, persoon_opschieten=persoon_opschieten, favoriete_getal=favoriete_getal, vakantie_gaan=vakantie_gaan, beste_eigenschap=beste_eigenschap, slechtste_eigenschap=slechtste_eigenschap, ergste_overkomen=ergste_overkomen)


#start onkunde
@app.route('/onkunde', methods=['GET'])
def start_onkunde():
    return render_template(template_name_or_list='formulier_onkunde.html')