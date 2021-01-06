import os
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.messages.create(body="Hot Sauce is groomed!", from_='+12513159803', to='+12508371392')

        # email notification
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('kategranstrom2000@gmail.com', os.environ['EMAIL_PASSWORD'])
        msg = MIMEMultipart()
        msg['FROM'] = 'kategranstrom2000@gmail.com'
        msg['To'] = 'goobies@telus.net'
        msg['Subject'] = 'Hot Sauce is Groomed!'

        s.send_message(msg)
        del msg
        s.quit()

if __name__ == "__main__":
    main()
