from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Custom error handler decorator
def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            return jsonify({'error': 'Invalid input', 'message': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Internal server error', 'message': str(e)}), 500
    return decorated_function

@app.route('/predict', methods=['POST'])
@handle_errors
def predict():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if 'text' not in data:
        raise ValueError('Text field is required')
    
    if len(data['text']) > 1000:
        raise ValueError('Text too long. Maximum 1000 characters')
    
    # Your prediction code here
    result = {'prediction': 'positive', 'confidence': 0.95}
    
    return jsonify(result)

# Register error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)