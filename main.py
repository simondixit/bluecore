from flask import Flask, render_template, abort
from livereload import Server

app = Flask(__name__)

app.config.update(
    ENV='development',
    DEBUG=True
)

@app.route("/")
def default():
    return render_template('index.html')

@app.route("/<string:path>")
def index(path):
    if path != "":
        return render_template(path + '.html')
    else:
        abort(404)

server = Server(app.wsgi_app)
# server.watch
server.watch('templates')
server.watch('static')
server.serve(port=5000, host='localhost')
