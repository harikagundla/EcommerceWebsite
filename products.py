import json
import os

PRODUCT_FILE = "data/products.json"

def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r") as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCT_FILE, "w") as f:
        json.dump(products, f)

def add_product(name, price, category, image):
    products = load_products()
    products.append({"name": name, "price": price, "category": category, "image": image})
    save_products(products)
