from flask import Flask, render_template
import json
import os
from itertools import cycle

app = Flask(__name__)

# Seta o caminho para os JSON dos políticos
JSON_DIR = 'data/json_files'


# Função para carregar dados de todos os políticos
def carregar_politicos():
    dados = []
    # Itera sobre cada arquivo JSON no diretório passado
    for filename in sorted(os.listdir(JSON_DIR)):
        if filename.endswith('.json'):
            # Cada arquivo na iteração é aberto, e seu conteúdo é gravado como um elemento objeto (dicionário) da lista 'dados'
            with open(os.path.join(JSON_DIR, filename), 'r', encoding='utf-8') as f:
                dados.append(json.load(f))
    # A função, no fim, retorna uma lista com um objeto para cada político com os dados dos JSON, que é ordenado alfabeticamente
    return sorted(dados, key=lambda x: x['nome'][5:])


@app.route('/')
def index():
    # Carrega os dados dos políticos para a página
    politicos = carregar_politicos()
    num_cards_per_slide = 4
    num_slides = -(-len(politicos) // num_cards_per_slide)  # Calcula o número de slides restantes

    # Repete políticos para preencher o último slide completamente
    politicos_filled = list(zip(range(num_slides * num_cards_per_slide), cycle(politicos)))

    return render_template('home.html', politicos=[p for _, p in politicos_filled])


@app.route('/pagina-politicos')
def pagina_politicos():
    # Carrega os dados dos políticos para a página
    politicos = carregar_politicos()
    return render_template('politicos.html', politicos=politicos)


@app.route('/perfil/<nome>')
def json_perfil(nome):
    try:
        with open(f'{JSON_DIR}/{nome}.json', encoding='utf-8') as f:
            dados = json.load(f)
            total_presença = sum(int(dados['presencas'][i]) for i in range(1, len(dados['presencas']), 2))
            total_ausencia = sum(int(dados['ausencias'][i]) for i in range(1, len(dados['ausencias']), 2))

            porcentagem_presença = round(total_presença * 100 / (total_presença + total_ausencia), 2)
            porcentagem_ausencia = round(total_ausencia * 100 / (total_presença + total_ausencia), 2)

        return render_template(
            'perfil.html',
            perfil=dados,
            porcentagem_presença=porcentagem_presença,
            porcentagem_ausencia=porcentagem_ausencia,
        )
    except FileNotFoundError:
        return "Perfil não encontrado :/", 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
