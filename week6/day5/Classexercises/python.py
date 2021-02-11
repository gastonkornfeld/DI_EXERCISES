
# Access the value of key ‘history’


# sampleDict = { 
#    "class":{ 
#       "student":{ 
#         "name":"Mike",
#         "marks":{
#             "physics":70,
#             "history":80
#         }
#       }
#    }
# }


# print(sampleDict["class"]["student"]["marks"]["history"])










# Delete set of keys from Python Dictionary


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]


del sampleDict["name"]
del sampleDict["salary"]

print(sampleDict)