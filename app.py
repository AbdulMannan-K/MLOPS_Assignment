from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained recommendation model
model = joblib.load('model.pkl')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    data = request.get_json()

    # Check if 'user_id' is present in the request
    if 'user_id' not in data:
        return jsonify({'error': 'User ID is missing'}), 400

    user_id = data['user_id']

    # Perform recommendation based on the user ID
    # Here, you need to replace this with your actual recommendation logic
    recommendations = []  # Placeholder for recommendations

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
