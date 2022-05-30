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

@app.route("/button")
def button():
    return render_template('button.html')

@app.route("/order-number-and-date")
def orderNumberAndDate():
    return render_template('order-number-and-date.html')

@app.route("/returns-or-damages")
def returnOrDamages():
    return render_template('returns-or-damages.html')

@app.route("/items-displayer")
def itemsDisplayer():
    return render_template('items-displayer.html')

@app.route("/order-details")
def orderDetails():
    return render_template('order-details.html')

@app.route("/section-divider")
def sectionDivider():
    return render_template('section-divider.html')

@app.route("/green-delivery")
def greenDelivery():
    return render_template('green-delivery.html')

@app.route("/footer")
def footer():
    return render_template('footer.html')

server = Server(app.wsgi_app)
# server.watch
server.watch('templates')
server.watch('static')
server.serve(port=5000, host='localhost')
