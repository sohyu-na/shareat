from flask import Flask, render_template
import sys
app = Flask(__name__)


@app.route("/")
def main_home():
    return render_template("index.html")


# @app.route("/registration")
# def register_restaurant():
#     return render_template("index.html")


# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
