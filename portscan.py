#! /usr/bin/env python 
# -*- coding:utf-8 -*-

import socket
from optparse import OptionParser


def open(ip,port):
    s = socket.socket()
    try:
        s.connect((ip,port))
        return True
    except:
        return False

def scan(ip,port):
    for x in port:
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close"%(ip,x))

def rscan(ip,s,e):
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port close"%(ip,x))

def main():

    usage = "usage: xxx.py -i <ip address> -p <port>"  # 帮助
    parser = OptionParser(usage=usage)
    parser.add_option("-i", "--ip", type="string", dest="ipaddress", help="your target ip here")
    parser.add_option("-p", "--port", type="string", dest="port", help="your target port here")
    (options, args) = parser.parse_args()  # 获取选项和参数进行赋值

    ip = options.ipaddress
    port = options.port

    defaultport = [135,139,445,1433,3306,3389,5944]

    if ',' in port:#portscan.py -i 127.0.0.1 -p 80,21,89
        port = port.split(',')
        a = []
        for x in port:
            a.append(x)
        scan(ip,a)
    elif '-' in port:#portscan.py -i 127.0.0.1 -p 80-89
        port = port.split('-')
        s = int(port[0])
        e = int(port[1])
        rscan(ip,s,e)
    elif "all" in port:#portscan.py -i 127.0.0.1 all
        rscan(ip,1,65535)
    elif "default" in port:#portscan.py -i 127.0.0.1 -p default
        scan(ip,defaultport)

    pass


if __name__ == '__main__':
    main()
