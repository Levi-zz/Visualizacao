from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/wordcloud")
def chart1():
    return render_template('wordcloud.html')

@app.route("/graph_force")
def chart2():
    return render_template('graph_force.html')

@app.route("/paralelas")
def chart3():
    return render_template('paralelas.html')

@app.route("/topics")
def chart4():
    return render_template('Topics.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
