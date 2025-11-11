from flask import Flask, request, jsonify

app = Flask(__name__)

models = {
    '1': {
        'id': '1',
        'name': 'Sentiment Classifier',
        'type': 'classification',
        'accuracy': 0.94
    },
    '2': {
        'id': '2',
        'name': 'Text Generator',
        'type': 'generation',
        'accuracy': 0.89
    }
}

# CREATE - Add a new model
@app.route('/models', methods=['POST'])
def create_model():
    data = request.get_json()
    
    # Validate input
    required_fields = ['name', 'type', 'accuracy']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Generate new ID
    new_id = str(len(models) + 1)
    data['id'] = new_id
    models[new_id] = data
    
    return jsonify(data), 201

# READ - Get all models
@app.route('/models', methods=['GET'])
def get_models():
    return jsonify(list(models.values()))

# READ - Get a specific model
@app.route('/models/<model_id>', methods=['GET'])
def get_model(model_id):
    if model_id not in models:
        return jsonify({'error': 'Model not found'}), 404
    
    return jsonify(models[model_id])

# UPDATE - Update a model
@app.route('/models/<model_id>', methods=['PUT'])
def update_model(model_id):
    if model_id not in models:
        return jsonify({'error': 'Model not found'}), 404
    
    data = request.get_json()
    models[model_id].update(data)
    models[model_id]['id'] = model_id  # Ensure ID doesn't change
    
    return jsonify(models[model_id])

# DELETE - Delete a model
@app.route('/models/<model_id>', methods=['DELETE'])
def delete_model(model_id):
    if model_id not in models:
        return jsonify({'error': 'Model not found'}), 404
    
    deleted_model = models.pop(model_id)
    return jsonify({'message': 'Model deleted', 'model': deleted_model})

if __name__ == '__main__':
    app.run(debug=True, port=5000)