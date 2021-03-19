
# At this point, we will be creating the functionality that allows 
# the user to add and delete products from their cart.

# In the app.py file
# Create a route with the following URL /cart that leads to the cart template 
# (it should display all the products in the cart with their price,
#  the total price and a button next to each product that allows the user to delete it from his cart)

# Create a variable named cart_item. This variable will hold all the products added to the cart.
# Create a route with the following URL /add_product_to_cart/<product_id> that triggers a function. This function should take the product id as a parameter, and append the product details to the cart_item variable.
# Create a route with the following URL /delete_product_from_cart/<product_id> that triggers a function. This function should take the product id as a parameter, and delete the product details from the cart_item variable.
# Note : If you feel comfortable with json, you could write the products into a cart.json file



from flask import Flask, render_template, request
import json

file_route = "static/productslist.json"

with open(file_route) as json_file:
    data = json.load(json_file)
    

print(data[0]['ProductPicUrl'])
products_in_cart = []


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    
    return render_template('products.html', data = data)


@app.route('/product/<product_id>')
def product(product_id):
    
    return render_template('product_id.html', data = data, id = product_id)

@app.route('/cart')
def cart():
    
    
    return render_template('cart.html', data = data, cart = products_in_cart)

@app.route('/add_to_cart/<item_id>')
def add_to_cart(item_id):
    total = 0
    for item in data:
        if item['ProductId'] == item_id:
            price = item['Price']
            products_in_cart.append(item)
    
    for item in products_in_cart:
        total += item['Price']
            
    return render_template('cart.html', data = data, cart = products_in_cart, total = total)

@app.route('/delete_from_cart/<item_id>')
def delete_from_cart(item_id):
    total = 0
    for item in data:
        if item['ProductId'] == item_id:
            products_in_cart.remove(item)
    
    for item in products_in_cart:
        total += item['Price']
            
    return render_template('cart.html', data = data, cart = products_in_cart, total = total)



app.run(debug=True, port=5001)    
    
        
        






