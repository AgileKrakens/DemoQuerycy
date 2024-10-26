from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/perfil/<nome>')
def json_perfil(nome):
    try:
        with open(f'../src/data/json_files/{nome}.json', encoding='utf-8') as f:
            dados = json.load(f)
            total_presença = 0
            porcentagem_presença = 0
            total_ausencia = 0
            porcentagem_ausencia = 0

            for k in range(1,len(dados['presencas']),2):
                total_presença += int(dados['presencas'][k])
            
            for k in range(1,len(dados['ausencias']),2):
                total_ausencia += int(dados['ausencias'][k])

            porcentagem_presença = round(total_presença * 100 / (total_presença + total_ausencia),2)

            porcentagem_ausencia = round(total_ausencia * 100 / (total_ausencia + total_presença),2)

        return render_template('perfil.html', perfil=dados, porcentagem_presença=porcentagem_presença, porcentagem_ausencia=porcentagem_ausencia)
    except FileNotFoundError:
        return "perfil não encontrado :/", 404

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/pagina-politicos')
def politicos():
   folder_path = 'data/json_files'
   dados = []
   try:

       for filename in sorted(os.listdir(folder_path)):
           if filename.endswith('.json'):
               print(filename)
               with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                   dados.append(json.load(f))
   except FileNotFoundError as e:
       raise e
    
   except UnicodeDecodeError as e:
       return f"Erro ao ler arquivo: {str(e)}", 500 
   return render_template('politicos.html', politicos=sorted(dados,key=lambda x:x['nome'][5:]))
 
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
