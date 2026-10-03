from flask import Flask, jsonify, render_template, request

# Point Flask to the templates directory
app = Flask(__name__, template_folder='templates')


# Route 1: Serve the Frontend HTML page
@app.route('/')
def home():
  return render_template('index.html')


# Route 2: API Endpoint for running algorithms
@app.route('/api/simulate', methods=['POST'])
def simulate():
  data = request.get_json()
  # Add your scheduling logic / simulation function here
  return jsonify({'status': 'success', 'data': data})


# Route 3: API Endpoint for comparing all algorithms
@app.route('/api/compare', methods=['POST'])
def compare():
  data = request.get_json()
  # Add your comparison logic here
  return jsonify({'status': 'success', 'results': {}})


if __name__ == '__main__':
  app.run(debug=True, port=5000)