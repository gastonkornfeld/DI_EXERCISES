import json

def getJSON(filePathAndname):
    with open(filePathAndname, 'r') as fp:
        return json.load(fp)


# db_info = getJSON('users.json')



