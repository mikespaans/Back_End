import content
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    Name = content.Name
    Picture = content.Picture
    Llorem_ipsum = content.Llorem_ipsum
    return flask.render_template(template_name_or_list='index.html', Name=Name, Picture=Picture, Llorem_ipsum=Llorem_ipsum)