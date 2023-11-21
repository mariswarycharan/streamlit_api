from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Your API logic here
    data = {'message': 'Hello from your API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
