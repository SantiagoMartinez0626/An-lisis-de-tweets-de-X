from flask import Flask, jsonify, render_template, request, url_for
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv('archive/covid19_tweets.csv')

# Imprimir las columnas disponibles
print("Columnas disponibles:", df.columns.tolist())

# Asegúrate de usar las columnas correctas que existen en tu CSV
df = df[['text']]  # Por ahora solo usamos 'text' que sabemos existe

tweets = df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweets', methods=['GET'])
def get_tweets():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    return jsonify(tweets[offset:offset + limit])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
