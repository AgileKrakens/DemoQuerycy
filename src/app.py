from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route(f'/perfil/<int:id_perfil>')
def perfil_JSON(id_perfil):
        with open(f'../src/data/json_files/{id_perfil}.json', 'r') as f:
            dados = json.load(f)
        return render_template('perfil.html', perfil=dados)
        
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/pagina-politicos')
def politicos():
    return render_template('politicos.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
