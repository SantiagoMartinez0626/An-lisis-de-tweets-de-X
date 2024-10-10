from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('archive/covid19_tweets.csv')

df = df[['id', 'text', 'created_at', 'user']]

tweets = df.to_dict(orient='records')

@app.route('/tweets', methods=['GET'])
def get_tweets():
    return jsonify(tweets)

@app.route('/tweets/<int:tweet_id>', methods=['GET'])
def get_tweet(tweet_id):
    tweet = next((tweet for tweet in tweets if tweet['id'] == tweet_id), None)
    if tweet:
        return jsonify(tweet)
    else:
        return jsonify({'error': 'Tweet no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
