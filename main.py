from flask import Flask, render_template, abort
from livereload import Server
import os

# VARIABLES
app = Flask(__name__)
server = Server(app.wsgi_app)
templates_dir = os.getcwd() + '/templates/'

app.config.update(
    ENV='development',
    DEBUG=True
)

# CONTROLLERS
@app.route("/")
def default():
    return render_template('index.html')

@app.route("/<string:request>")
def index(request):
    template = request + '.html'
    if os.path.isfile(templates_dir + template):
        return render_template(template)
    else:
        abort(404)

# WATCHERS
server.watch('templates')
server.watch('static')

server.serve(port=5000, host='localhost')