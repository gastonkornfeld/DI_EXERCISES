from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_crypto_data(id, sort):




  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
  parameters = {
    'start': id,
    'limit':'1',
    'sort' : sort,
    
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data['data']
  except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)


def crypto_price(id):
    
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
  'start':id,
  'limit':'1',
  'convert':'USD'
  }
    
    
  
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data['data'][0]['quote']['USD']['price']
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)




def get_info(id):
    
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
  'start':id,
  'limit':'1',
  'convert':'USD'
  }
    
    
  
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data['data'][0]
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)



# to get the first 30 by rank


def get_all_crypto():
    
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
  parameters = {
    'start':'1',
    'limit':'30',
    'sort' : "cmc_rank",
    
    
    
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data['data']
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)







# for the icon and website information




def get_details(id):
    
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
  parameters = {
    'id': id
    
    
    
    
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data['data'][str(id)]
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)




# print(get_details(1))