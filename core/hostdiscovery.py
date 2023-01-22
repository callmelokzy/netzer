import nmap
import socket
from tabulate import tabulate
from colours import Colors


def scan_network(ip_range):
    # Create an instance of the nmap.PortScanner class
    nm = nmap.PortScanner()
    # Perform a SYN scan on the given IP range
    nm.scan(ip_range, arguments='-sT')
    # Iterate through the hosts in the scan results
    data = []
    hostname = ''
    for host in nm.all_hosts():
        # Check if the host is up
        if nm[host].state() == "up":
            # print(f'░░░░░ {host} is up ░░░░░░░░░░', end=" ")
            try:
                hostname = socket.gethostbyaddr(host)[0] + ''
            except socket.herror:
                hostname = 'unknown host '

        data.append([host, hostname])
    print(f"\n[+] {Colors.bold}{Colors.green}AVAILABLE TARGETS: {Colors.end}")
    return tabulate(data, headers=["Active Host", "Hostname"], tablefmt="fancy_grid")


def network_id(ip):
    ip_parts = ip.split('.')
    ip_parts[-1] = '0'
    return '.'.join(ip_parts)



