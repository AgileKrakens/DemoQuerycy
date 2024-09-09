from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    alterar = "test"
    return render_template('index.html', alterar=alterar)

if __name__ == '__main__':
    app.run(debug=True)
