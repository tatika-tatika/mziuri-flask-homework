from flask import Flask, render_template, jsonify

application = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 600},
    {"id": 4, "name": "Headphones", "price": 200},
]

@application.route("/")
def index():
    return render_template("index.html", products=products)


@application.route("/api/products")
def get_all_products():
    return jsonify(products)


@application.route("/api/products/<search>")
def get_products(search):
    filtered_products = []

    for product in products:
        if search.lower() in product["name"].lower():
            filtered_products.append(product)

    return jsonify(filtered_products)


if __name__ == "__main__":
    application.run(debug=True)

