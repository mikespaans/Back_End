from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

# url_for('static', filename='style.css')


@app.route('/')
def index():
    # username = request.args.get('username')
    print ("test")
    return render_template(template_name_or_list='welcome.html')

    # return render_template(template_name_or_list='welcome.html')
@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form.get("username", "")
    email = request.form.get("email", "")
    return f'<h1>De ingevulde gegevens zijn</h1> <p> Naam : {name} <br> email : {email}</p>'
