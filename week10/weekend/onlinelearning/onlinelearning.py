



from flask import Flask


app = Flask(__name__):





my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = list(map(lambda item : item**2, my_list))
print(new_list)



list2 = [(2,3), (4,6), (1,9), (6,5)]

list2.sort(key= lambda x : x[1])    
print(list2)