from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint 1
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    if name is None:
        return jsonify({"error": "Parameter 'name' is required."}), 400
    return jsonify({"message": f"Hello, {name}!"})

# Endpoint 2
@app.route('/name', methods=['GET'])
def name():
    name = request.args.get('name')
    age = request.args.get('age')
    if name is None or age is None:
        return jsonify({"error": "Parameters 'name' and 'age' are required."}), 400
    return jsonify({"name": name, "age": age})

# Endpoint 3
@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    age = request.form.get('age')
    salary = request.form.get('salary')
    if name is None or age is None or salary is None:
        return jsonify({"error": "Parameters 'name', 'age', and 'salary' are required."}), 400
    # Process the data
    return jsonify({"message": "Thanks, your create user!"})

# Endpoint 4
@app.route('/profession', methods=['POST'])
def profession():
    name = request.form.get('name')
    age = request.form.get('age')
    salary = request.form.get('salary')
    if name is None or age is None or salary is None:
        return jsonify({"error": "Parameters 'name', 'age', and 'salary' are required."}), 400
    # Process the data
    return jsonify({"name": name, "Profession": "QA Engineer"})

# Endpoint 5
@app.route('/king', methods=['GET'])
def king():
    name = request.args.get('name')
    age = request.args.get('age')
    salary = request.args.get('salary')
    if name is None or age is None or salary is None:
        return jsonify({"error": "Parameters 'name', 'age', and 'salary' are required."}), 400
    return jsonify({"message": "Hail to the king, baby!"})

# Endpoint 6
@app.route('/cool', methods=['GET'])
def cool():
    name = request.args.get('name')
    age = request.args.get('age')
    salary = request.args.get('salary')
    if name is None or age is None or salary is None:
        return jsonify({"error": "Parameters 'name', 'age', and 'salary' are required."}), 400
    return jsonify({"message": "I am QA Engineer. Let's rock!"})

# Endpoint 7
@app.route('/salary', methods=['GET'])
def salary():
    name = request.args.get('name')
    age = request.args.get('age')
    salary = request.args.get('salary')
    if name is None or age is None or salary is None:
        return jsonify({"error": "Parameters 'name', 'age', and 'salary' are required."}), 400
    return jsonify({"salary": salary})

if __name__ == '__main__':
    app.run(debug=True)
