import time
import socket
import urllib.request
import urllib.error


class Netzer:

    def __init__(self):
        for i in range(25):
            # Print a loading message and the current progress
            message = "Checking Connection..." + "." * (i % 4)
            print(f"\r{message}", end="")
            # Sleep for a short amount of time to create the animation effect
            time.sleep(0.1)
            # Print a newline character to move the cursor to the next line
        print("Done ✅")

    @staticmethod
    def internet_private():
        ipaddr = socket.gethostbyname(socket.gethostname())
        if ipaddr == "127.0.0.1":
            return False
        else:
            return ipaddr

    @staticmethod
    def internet_public():
        try:
            urllib.request.urlopen('http://www.google.com', timeout=1)
            public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            return public_ip
        except urllib.error.URLError:
            return False


if __name__ == "__main__":

    netzer = Netzer()
    pvt_check = netzer.internet_private()
    pub_check = netzer.internet_public()
    print('Connected to Internet') if pvt_check and pub_check else print('No Internet')
    time.sleep(0.2)
    print('Public IPadrress: ', pub_check)
    time.sleep(0.2)
    print('Private IPaddress: ', pvt_check)
