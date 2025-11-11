from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Welcome to the 75 Hard AI Engineering API'}

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)