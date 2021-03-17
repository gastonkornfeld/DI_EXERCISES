
# Note: For this exercise, we will use the JSON database provided in the assets below.

# This database contains a list of dictionnaries. Each dictionnary contains these keys:


# We will be using these keys to represent each item in our marketplace.
# You don’t have to use all the keys.

# Build a marketplace website, the website should have 3 pages:
# A homepage, with a welcome message, routed to /.
# A products page, that displays a list of all the products that are for sale, routed to /products.
# A product details page, that displays the detail of the selected product
#  (the product id should be passed into the URL), routed to /product/<product_id>








from flask import Flask, render_template, request
import json

file_route = "static/productslist.json"

with open(file_route) as json_file:
    data = json.load(json_file)
print(data)



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



app.run(debug=True, port=5001)    
    
        
        






