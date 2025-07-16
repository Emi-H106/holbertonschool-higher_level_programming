from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

def read_json_file():
    with open('products.json') as f:
        return json.load(f)
    
def read_csv_file():
    products = []
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price'])
            })
    return products

def read_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
        items_list = data.get('items', [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json_file()
    elif source == 'csv':
        products_list = read_csv_file()
    elif source == 'sql':
        try:
            products_list = read_sqlite()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"Database error: {e}")
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_list if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            products_list = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid ID")
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

