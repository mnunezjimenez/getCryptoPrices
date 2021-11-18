from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

queryParameters = {
    'slug' : "glitch,solana",
    'convert' : 'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '3b9fb98d-f3d0-478d-bd23-0edf0f3dae35',
}
session = Session()
session.headers.update(headers)
try:
  responseAPI = session.get(url, params=queryParameters)  
  print('Successful connection')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

solanaPrice = json.loads(responseAPI.text)['data']['5426']['quote']['USD']['price']
glitchPrice = json.loads(responseAPI.text)['data']['8236']['quote']['USD']['price'] 
print("Solana price is: ", solanaPrice)
print("Glitch price is: ", glitchPrice)
solanaBoughtAt = 215.83
glitchBoughtAt = 2.03
##Calculate portfolio return: 
#   1. Calculate alt coin return: (actualPrice - priceBoughtAt)/priceBoughtAt) * 100
#   2. Multiply alt coin return by the weight of that particular coin of your portfolio, in this case is half and half so 0.5
#   3. Sum
portfolioReturn = round((((solanaPrice - solanaBoughtAt)/solanaBoughtAt) * 100 * 0.5) + (((glitchPrice - glitchBoughtAt)/glitchBoughtAt) * 100 *0.5),2)
print("Portfolio return: ", portfolioReturn,"%")
