


class LoterryTicket():

    tickets_created = 0


    def __init__(self, is_gold_ticket=False):
        self.is_gold_ticket = is_gold_ticket
        LoterryTicket.tickets_created += 1
        self.ticket_number = LoterryTicket.tickets_created
        if LoterryTicket.tickets_created % 5 == 0:
            self.is_gold_ticket = True
        if self.is_gold_ticket:
            print("you got a golden ticker")
            self.is_gold_ticket = False


    # def __str__ (self):
    #     return f"Ticket number {self.ticket_number}"
    
    def __repr__ (self):
        if LoterryTicket.tickets_created % 5 == 0:
            return f"Golden Ticket number {self.ticket_number}"
        else:
            return f"Ticket number {self.ticket_number}"
        

    def __add__(self, other):
        return self.ticket_number + other.ticket_number

    @classmethod
    def golden_ticket(cls):
        pass

    
list_of_tickets = []

for i in range(100):
    ticket = LoterryTicket()
    print(ticket)
    list_of_tickets.append(ticket)
    print(ticket + ticket)

print(list_of_tickets)



