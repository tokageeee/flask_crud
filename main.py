from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

# Configure MySQL
with open('env.json') as f:
    data = json.load(f)

app.config['MYSQL_HOST'] = data['MYSQL_HOST']
app.config['MYSQL_USER'] = data['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = data['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = data['MYSQL_DB']

# Create MySQL instance
mysql = MySQL(app)

# Route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO stocks(name, price) VALUES (%s, %s)", (item['name'], item['price']))
    mysql.connection.commit()
    cur.close()
    return jsonify(item), 201

# Route to retrieve all items
@app.route('/items', methods=['GET'])
def get_all_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stocks")
    items = cur.fetchall()
    cur.close()
    return jsonify(items), 200

# Route to retrieve a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stocks WHERE id = %s", (item_id,))
    item = cur.fetchone()
    cur.close()
    if item:
        return jsonify(item), 200
    return jsonify({'error': 'Item not found'}), 404

# Route to update a specific item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    cur = mysql.connection.cursor()
    cur.execute("UPDATE items SET name = %s, price = %s WHERE id = %s", (item['name'], item['amount'], item_id))
    mysql.connection.commit()
    cur.close()
    return jsonify(item), 200

# Route to delete a specific item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM stocks WHERE id = %s", (item_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
