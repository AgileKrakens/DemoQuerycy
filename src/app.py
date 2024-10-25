from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route(f'/perfil/<int:id_perfil>')
def perfil_JSON(id_perfil):
   try:
       with open(f'../src/data/json_files/{id_perfil + 1}.json', 'r', encoding='utf-8') as f:
           dados = json.load(f)
       return render_template('perfil.html', perfil=dados)
   except FileNotFoundError:
       return "Perfil não encontrado", 404
   
@app.route('/')
def index():
   return render_template('home.html')

@app.route('/pagina-politicos')
def politicos():
   folder_path = 'data\json_files'
   dados = []
   try:
       # Carregar todos os arquivos JSON
       for filename in sorted(os.listdir(folder_path)):
           if filename.endswith('.json'):
               print(filename)
               with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                   dados.append(json.load(f))
   except FileNotFoundError as e:
       raise e
    #    return "Diretório não encontrado", 404
   except UnicodeDecodeError as e:
       return f"Erro ao ler arquivo: {str(e)}", 500 
   print(dados)
   return render_template('politicos.html', politicos=sorted(dados,key=lambda x:x['nome'][5:]))
 
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)