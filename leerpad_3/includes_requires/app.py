import variables
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    Name = variables.Name
    return flask.render_template(template_name_or_list='index.html', Name=Name)