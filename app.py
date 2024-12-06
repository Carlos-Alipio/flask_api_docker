from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/amor', methods=['GET'])
def ping():
    return jsonify({'Amor_do_Alipio': 'Cristiane Freire de Sá'}), 200

if __name__ == '__main__':
    # Executa a aplicação no host 0.0.0.0 e porta 5000 (útil para o Docker)
    app.run(host='0.0.0.0', port=5000)
