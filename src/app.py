from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/perfil/1')
def perfil_JSON():
        with open(f'../src/data/json_files/1.json', 'r') as f:
            dados = json.load(f)
        return render_template('perfil.html', perfil=dados)
        
@app.route('/')
def index():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
