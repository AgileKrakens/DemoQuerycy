import matplotlib.pyplot as plt
import io
import base64
from db import get_db_connection

def gerar_grafico(nome_autor=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = """
    SELECT tema, COUNT(*) as total
    FROM law_records
    WHERE autor = %s
    GROUP BY tema
    ORDER BY total DESC
    LIMIT 8
    """
    cursor.execute(query, (nome_autor,))
    
    temas = cursor.fetchall()
    cursor.close()

    # Coletar os dados
    temas_nomes = [tema[0] for tema in temas]
    temas_totais = [tema[1] for tema in temas]

    cursor = connection.cursor()
    query_restantes = """
    SELECT COUNT(*)
    FROM law_records
    WHERE autor = %s AND tema NOT IN (
        SELECT tema FROM (
            SELECT tema
            FROM law_records
            WHERE autor = %s
            GROUP BY tema
            ORDER BY COUNT(*) DESC
            LIMIT 8
        ) AS subquery
    )
    """

    cursor.execute(query_restantes, (nome_autor, nome_autor))
    restantes = cursor.fetchone()[0]
    cursor.close()
    
    temas_nomes.append("Restantes")
    temas_totais.append(restantes)
    total_aprovados = sum(temas_totais)

    # Criar o gráfico
    plt.figure(figsize=(12, 6))  # Ajustar o tamanho para mais espaço
    indices = list(range(1, len(temas_nomes) + 1))
    plt.bar(indices, temas_totais, color='black', alpha=0.7)
    plt.title('Temas de Leis Aprovadas')
    plt.xlabel('Índice')
    plt.ylabel('Número de Leis Aprovadas')

    # Adicionar porcentagens e totais no gráfico
    for i, v in enumerate(temas_totais):
        plt.text(indices[i], v + 0.5, f"{v} ({(v / total_aprovados) * 100:.1f}%)", ha='center')

    # Ajustar os ticks do eixo X para usar os índices
    plt.xticks(indices)

    # Criar legenda associando os números aos temas
    legenda = "\n".join([f"{i} - {tema}" for i, tema in zip(indices, temas_nomes)])

    # Adicionar a legenda ao lado do gráfico
    plt.legend(
        [legenda], loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize=10, frameon=False, handlelength=0, handletextpad=0
    )

    # Ajustar o layout para evitar cortes
    plt.tight_layout()

    # Salvar o gráfico em um objeto BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')  # Salvar com bounding box ajustado
    img.seek(0)
    plt.close()


    # Codificar a imagem em base64
    return base64.b64encode(img.getvalue()).decode('utf-8')
