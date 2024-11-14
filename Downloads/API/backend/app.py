import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Carrega o arquivo CSV
        data_df = pd.read_csv('data.csv', delimiter=',')
        
        print("DataFrame carregado:")
        print(data_df)
        
        print("Colunas antes da limpeza:", data_df.columns)
        
        # Limpa os nomes das colunas
        data_df.columns = data_df.columns.str.replace('"', '')
        
        print("Colunas após a limpeza:", data_df.columns)
        
        # Verifica se a coluna 'Peso' existe
        if 'Peso' not in data_df.columns:
            raise ValueError("A coluna 'Peso' não foi encontrada no arquivo CSV.")
        
        # Filtra os dados pela data
        filter_date = pd.to_datetime('2024-11-07')
        filtered_data = data_df[data_df["Data"].dt.date == filter_date.date()]
        
        # Verifica se a data filtrada tem dados
        if filtered_data.empty:
            return jsonify({"message": "Nenhum dado encontrado para essa data"}), 404
        
        # Retorna os dados filtrados como JSON
        return jsonify(filtered_data.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"message": f"Erro ao processar a data: {e}"}), 400

if __name__ == "__main__":
    app.run(debug=True)