from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import sys
import bokeh

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/abc")
def abc():
    return render_template("abc_overview.html")


@app.route("/abc/<int:abc_id>")
def abc_id(abc_id):
    return render_template("abc_detail.html", abc_id=abc_id)


@app.route("/abc/<int:abc_id>/model/<int:model_id>")
def abc_model(abc_id, model_id):
    return render_template("model.html", abc_id=abc_id, model_id=model_id)


if __name__ == '__main__':
    db = sys.argv[1]
    app.run()