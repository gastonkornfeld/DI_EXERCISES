
    
        



# # Analyse these code before executing them. What will be the outputs ?

# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle()
# print(nc.color)
# # >> What will be the output ?



# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)
# nc.grow()
# print(nc.diameter)






# class Car():

#     def __init__(self, color, manufactured, km_travelled):
#         self.color = color
#         self.manufactured = manufactured
#         self.km_travelled = km_travelled

#     def print_info(self):
#         return f"The {self.color} {self.manufactured} car have travelled {self.km_travelled}km.\n "

#     def travel(self, distance):
#         self.km_travelled += distance
#         return f"the car traveled {distance} and now have {self.km_travelled} km traveled"


# car1 = Car("black", "volskwagen", 200)


# print(car1.print_info())
# print(car1.travel(200))
# print(car1.travel(200))
# print(car1.travel(200))
# print(car1.travel(200))
# print(car1.travel(200))
# print(car1.travel(200))













# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis() 




















# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price

#     def present(self):
#         print(f'Title: {self.title}')

# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')

# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)