import requests
from bs4 import BeautifulSoup
import time
import smtplib
import cssselect
import variables

while True:
    url = "https://eu.finalfantasyxiv.com/lodestone/worldstatus/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    item = soup.find_all(class_='world-list__create_character')

    actual = item[-12:-11]

    if str(actual).find('un') == 64:
        time.sleep(60)
        continue
    else:
        msg = 'Subject: Cerberus is GOOD!!'
        fromaddr = variables.from_addr
        toaddrs  = ['lj@lukejames.dev']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(variables.from_addr, variables.app_password)
        
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        
        break
