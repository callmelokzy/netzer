import socket
import urllib.request
import urllib.error
import psutil
from tabulate import tabulate
from colours import Colors
import os


class INFO:

    @staticmethod       # getting private ip address
    def get_private_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        private_ip = s.getsockname()[0]
        s.close()
        return private_ip

    @staticmethod       # getting public ip using ident.me webste
    def get_public_ip():
        try:
            # urllib.request.urlopen('http://www.google.com', timeout=1)
            public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            return public_ip
        except urllib.error.URLError:
            return 'Not Connected to INTERNET!'

    @staticmethod  # getting specific interface card name using ip address
    def get_interface_name(ip_address):
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.address == ip_address:
                    return interface

    @staticmethod  # getting all interface card with their associated ip address
    def get_network_interfaces():
        interfaces = psutil.net_if_addrs()
        data = []
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    data.append([interface, addr.address])
        return tabulate(data, headers=["Interface", "Address"], tablefmt="fancy_grid")


    @staticmethod
    def get_address_by_interface(interface_name):
        interfaces = psutil.net_if_addrs()
        for interface, addrs in interfaces.items():
            if interface == interface_name:
                for addr in addrs:
                    if addr.family == socket.AF_INET:
                        return addr.address
        return None
