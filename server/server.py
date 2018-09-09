from flask import Flask

#app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"


if __name__ == "__main__":
    app.run()