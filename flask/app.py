from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html");

@app.route('/file')
def game_over():
    return send_file('static/file.png')


if __name__ == "__main__":
    app.run(debug=True);
