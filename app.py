from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure to set a secret key for session handling

# Dummy product data
products = [
    {"id": 1, "name": "Product 1", "price": 20.00, "image_url": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Product 2", "price": 30.00, "image_url": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Product 3", "price": 40.00, "image_url": "https://via.placeholder.com/150"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Find the product by id
    product = next(item for item in products if item["id"] == product_id)
    # Get the current cart from session or create an empty cart if it doesn't exist
    cart = session.get('cart', [])
    cart.append(product)  # Add the product to the cart
    session['cart'] = cart  # Save the updated cart in the session
    return redirect(url_for('index'))  # Redirect to the index page

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)  # Calculate total price
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)  # Calculate total price
    return render_template('checkout.html', cart=cart, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)

products = [
    {"id": 1, "name": "Product 1", "price": 20.00, "image_url": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Product 2", "price": 30.00, "image_url": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Product 3", "price": 40.00, "image_url": "https://via.placeholder.com/150"},
    # Add more products here if desired
]
