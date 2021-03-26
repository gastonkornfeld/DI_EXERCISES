







# Create the following methods: show_outgoing_messages(self),
#  show_incoming_messages(self), show_messages_from(self, number)

# Test your code !!!

# Bonus: Build a nice menu for a user to create a new phone, 
# call, message using call , send_message and __init__

# Extra bonus: add options to the menu using each of the functions: 
# show_outgoing_messages, show_incoming_messages, show_messages_from





# Exercise 1 : Call History
# Create a class called Phone that accepts the parameters self and phone_number 
# (i.e phone number 0512345678)

class Phone():
#  in the __init__() as well as creates the attribute call_history (an empty list).

# Add an attribute messages (empty list) to the __init__().

    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []
# Add a method show_call_history that will pleasantly print your call history.

    def print_call_history(self):
        print(f"Call History from number {self.number}")
        for phone_call in self.call_history:
            print(phone_call)

    def print_message_history(self):
        print(f"Message History from number {self.number}")
        for message in self.messages:
            print(message)

# Add a method call that accepts self and other_phone 
# (i.e another Phone object) as parameters,
#  this function should add a string of whom called who to each phone’s call_history.

    def make_a_call(self, other_phone):
        print(f'the phone {self.number} is calling the phone {other_phone.number}')
        print("ring ring")
        self.call_history.append(f'make a call to the number {other_phone.number}')
        other_phone.call_history.append(f'receive a call from the number {self.number}')

# Create a send_message method similar to our call method 
# (will this need any additional parameters?), 
# save each message as a dictionary with to, from and content as the keys.

    def send_a_message(self, other_phone, message_to_send):
        print(f'the phone {self.number} send a message  to the phone {other_phone.number}\n message content: {message_to_send}')
        self.messages.append(f"Send a message to the number {other_phone.number}, message: {message_to_send}")
        other_phone.messages.append(f"receive a message from the number {self.number}, message: {message_to_send}")
        
        

gato_phone = Phone('0559468324')
alisa_phone = Phone('054345456')
# gato_phone.make_a_call(alisa_phone)
# gato_phone.make_a_call(alisa_phone)
gato_phone.send_a_message(alisa_phone, "hello alisa")
alisa_phone.send_a_message(gato_phone,"hello gaston")

gato_phone.send_a_message(alisa_phone, "how is everithing")
alisa_phone.send_a_message(gato_phone,"ooo going well how about you")
# print(gato_phone.print_call_history())
# print(alisa_phone.print_call_history())
print(alisa_phone.print_message_history())

