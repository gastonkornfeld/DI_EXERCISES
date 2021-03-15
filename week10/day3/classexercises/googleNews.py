import random
from requests import get
import json
import time
import requests

def get_new(topic):
        
    r = get("https://newsapi.org/v2/everything", params= {"q": topic, "from": "2021-03-12", "sortBy" : "popularity", "apiKey":"5719809a4f814d0d9f8cb98e7a3d97de"})
    convert = json.loads(r.text)
    print(convert.keys())
    
    for article in convert["articles"][:1]:
        hhh = article["title"]
        return f"{hhh}"
        

url = "https://t.me/Hanukabot"
boot_token = "1665405087:AAHZBLPzpM79K7xDf9zeuXjlRrXwOxrBQyk"

print(get_new("python"))

# convert1 = json.load(r2)
# convert2 = json.load(r3)
# print(convert)
# print(convert1)
# print(convert2)

# print(r3.text)
































token = "1616515608:AAGlt2OLkKzEF6HCAJgSOetlPdAcmjpIaC4"

current_id = 0

def get_messages(offset):
    get_updates = f"https://api.telegram.org/bot{boot_token}/getUpdates"
    r = requests.get(get_updates, params={"offset": offset+1}) # Making a request
# the offset parameters eliminates the id so the message dont get displayed forever 
    return r.json() # Converts the response to a dictionary


while True:
    # Check for new messages
    msgs = get_messages(current_id)

    for update in msgs['result']:
        current_id = update['update_id'] #keep a trace of the last update

        content = update["message"]["text"] #content of the message
        user_id = update["message"]["from"]["id"]
        if content == "/WhatsYourName":
            send_message = f"https://api.telegram.org/bot{boot_token}/sendMessage"
            requests.get(send_message, params={"chat_id":user_id, "text":"Eyal !"})
        else:
            new_to_display = get_new(content)
            send_message = f"https://api.telegram.org/bot{boot_token}/sendMessage"
            requests.get(send_message, params={"chat_id":user_id, "text":new_to_display})

        print(content)

    # Sleep 2s
    time.sleep(2)
