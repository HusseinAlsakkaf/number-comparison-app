from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_numbers():
    data = request.json
    numbers = data.get('numbers', [])
    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400
    max_number = max(numbers)
    return jsonify({"max_number": max_number})

if __name__ == '__main__':
    app.run(debug=True)
