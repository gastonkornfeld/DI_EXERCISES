



class Superlist(list):
    def __init__(self):
        
        

    def __len__(self):
        return 1000

    def show_list(self):
        print(self.list)



list1 = Superlist()

print(len(list1))
list1.append(5)
list1.show_list()