from hashlib import new
import requests
import socket
import threading
from http import client, server
from encodings import utf_8
import re

HOST = 'localhost' 
PORT = 3000         

def currency_exchange_rate(first_currency, second_currency, amount):
    global send_data

        # API currency exchange rate from rapidapi.com

    url = "https://currency-converter5.p.rapidapi.com/currency/convert"

    querystring = {"format":"json","from":first_currency,"to":second_currency,"amount":amount}
    headers = {
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
        'x-rapidapi-key': "b1a9b8e40fmsh223361486c2a33fp1edd29jsnce6831a58edf"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)


    '''
        A spliter is used to split the data from the server
        into the client.
    '''

    new_response = (response.text).split(",")
    new_text1 = new_response[6]
    new_text2 = new_text1.split(":")
    new_text3 = new_text2[1]
    new_text4 = re.findall("\d+.\d+", (new_text3))
    new_text5 = str(new_text4).split("'")
    new_text6 = new_text5[1]
    print(new_text1)
    print(new_text5)
    
    client.send(f'{new_text6}'.encode('utf-8')) # send the data back to the client


while True:
    print('Waiting for connection from client ..')
    server = socket.socket() # create a socket object
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # reuse the socket
    server.bind((HOST, PORT)) # waiting for connection from client
    server.listen(5) # max 5 byte connection
 
    client, addr = server.accept() # waiting reciver data from client
    print(f'Connected by {str(addr)}')

    data = client.recv(1024).decode('utf-8') # reciver data from client
    print(f'Import {data} from client.')
    new_data = data.split(".") # split the data from client

    first_currency = new_data[0]
    second_currency = new_data[1]
    amount = int(new_data[2])

    t1 = threading.Thread(target = currency_exchange_rate , args = (first_currency, second_currency, amount))
    t1.start()
    t1.join()

    client.close()