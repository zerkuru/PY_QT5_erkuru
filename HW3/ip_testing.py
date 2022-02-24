import os
import platform
import ipaddress
import subprocess
from tabulate import tabulate



def host_ping(pinglist):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    for host in pinglist:
        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0

def host_range_ping(starthost, endhost):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    iplist = starthost.split('.')
    last_oct = iplist[-1]
    iplistend = endhost.split('.')
    end_oct = iplistend[-1]
    pinglist = []

    while int(last_oct) <= int(end_oct):
        pinglist.append('.'.join(iplist))
        last_oct = int(last_oct) + 1
        iplist[-1] = str(last_oct)

    for host in pinglist:
        command = ['ping', param, '1', host]
        return subprocess.call(command) == 0


def host_range_ping_tab(starthost, endhost):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    iplist = starthost.split('.')
    last_oct = iplist[-1]
    iplistend = endhost.split('.')
    end_oct = iplistend[-1]
    pinglist = []

    while int(last_oct) <= int(end_oct):
        pinglist.append('.'.join(iplist))
        last_oct = int(last_oct) + 1
        iplist[-1] = str(last_oct)
    Uplist = []
    Downlist = []
    for host in pinglist:
        command = ['ping', param, '1', host]
        if subprocess.call(command) == 0:
            Uplist.append(host)
        else:
            Downlist.append(host)
    dictlist = []
    if len(Uplist)>len(Downlist):
        for i in Uplist:
            indexUp = Uplist.index(i)
            try:
                j = Downlist[indexUp]
            except IndexError:
                j = ""
            newdict = {"up": i, "down": j}
            dictlist.append(newdict)
    else:
        for i in Downlist:
            indexUp = Downlist.index(i)
            try:
                j = Uplist[indexUp]
            except IndexError:
                j = ""
            newdict = {"up": j, "down": i}
            dictlist.append(newdict)
    print(tabulate(dictlist, headers='keys'))




