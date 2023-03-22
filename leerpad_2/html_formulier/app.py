from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


# url_for('static', filename='style.css')


@app.route('/')
def index():
    # username = request.args.get('username')
    return render_template(template_name_or_list='welcome.html')

    # return render_template(template_name_or_list='welcome.html')
@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form.get("username", "")
    email = request.form.get("email", "")
    print (type(name))
    return render_template(template_name_or_list='response.html', name=name, email=email)
