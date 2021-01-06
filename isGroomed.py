import os
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import smtplib

def main():
    print("Checking if south bowl is groomed")
    s = requests.session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
    s.headers['Accept-Encoding'] = "gzip,deflate,sdch"
    s.headers['Accept'] = 'application/json, text/javascript, */*'
    s.headers['Accept-Language'] = 'en-US,en;q=0.8'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'

    grooming = 'https://www.revelstokemountainresort.com/conditions/grooming'
    res = s.get(grooming)
    soup = BeautifulSoup(res.text, features="html.parser")
    groomed_table = soup.find_all('table')[0]
    hot_sauce = groomed_table.find_all('tr')[10].find_all('td')[2].string
    if hot_sauce == 'Groomed':
        print('groomed!')

        # text notification
        account_sid = 'ACc5bd72fe3380ada11fe04830f0c7c1e4'
        auth_token = 'f57e6003622213c3a0b24e7b23bec59f'
        client = Client(account_sid, auth_token)
        message = client.messages.create(body="Hot Sauce is groomed!", from_='+12513159803', to='+12508371392')




if __name__ == "__main__":
    main()
