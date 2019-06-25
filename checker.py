'''
Simple script to web-scrape FFXIV server data to glean when I can create a
character to join my friends.

Runs from a modified version of Chris Albon's web scraping script.
'''

# Import external modules
import requests
import time
import smtplib
import cssselect
from bs4 import BeautifulSoup

# Import personal data
import variables

# run this script until needed no longer
while True:
    # Set up all that is necessary go make some beautiful soup
    url = "https://eu.finalfantasyxiv.com/lodestone/worldstatus/"
    headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
               AppleWebKit/537.36 (KHTML, like Gecko)  \
               Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    # once soup is made, find the best element relating to server status.
    status_list = soup.find_all(class_='world-list__create_character')

    # this returns cerberus from the list of servers.
    # The server i am interested in. 12 from end.
    cerberus_status = status_list[-12:-11]

    # it will find the 'un' in 'unavaialiable' at pos 64 in the string.
    if str(cerberus_status).find('un') == 64:
        time.sleep(60)
        continue
    # unless it doesnt then it must be available, therefore: email me!
    else:
        msg = 'Subject: Cerberus is GOOD!!'
        fromaddr = variables.from_addr
        toaddrs = ['lj@lukejames.dev']  # email me if you want.
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # hidden app password and real email.
        server.login(variables.from_addr, variables.app_password)

        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        break
