from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

app.config.update(
    ENV='development',
    DEBUG=True
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/order-details")
def orderDetails():
    return render_template('order-details.html')

@app.route("/section-divider")
def sectionDividerWidget():
    return render_template('section-divider.html')

server = Server(app.wsgi_app)
# server.watch
server.watch('templates')
server.watch('static')
server.serve(port=5000, host='localhost')
