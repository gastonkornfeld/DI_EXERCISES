
# Exercise 1
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
#  Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.


sandwiches_orders = ["chesse", "bacon and onion", "tuna", "salmon", "eggplant and mushrooms"]
print(sandwiches_orders)
finished_sandwiches = []

for sandwich in sandwiches_orders:
    print(f"there is an order of {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
    

for sandwich in finished_sandwiches:
    sandwiches_orders.remove(sandwich)
    print(f"{sandwich} sandwich is ready")
    


    



