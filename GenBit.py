import requests
import random

def generate_random_string(length):
  chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  for i in range(length):
    random_index = random.randint(0, len(chars) - 1)
    result += chars[random_index]
  return result

while True:
  random_link = "https://bit.ly/" + generate_random_string(7)
  response = requests.get(random_link)
  if response.status_code == 200:
    print(random_link,response)
    break
  else:
    print(random_link,response)
    continue
