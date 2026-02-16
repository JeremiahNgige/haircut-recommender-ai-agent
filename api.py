from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Placeholder: Logic to generate haircut recommendations
    recommendations = ['Buzz Cut', 'Fade', 'Pompadour']  # Example recommendations
    return jsonify(recommendations)

@app.route('/add-recommendation', methods=['POST'])
def add_recommendation():
    data = request.json
    new_recommendation = data.get('recommendation')
    # Placeholder: Logic to add a new recommendation
    return jsonify({'message': f'Successfully added {new_recommendation}'}), 201

if __name__ == '__main__':
    app.run(debug=True)