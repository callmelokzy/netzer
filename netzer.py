from core.colours import Colors
from core.info import INFO
import time
from core.hostdiscovery import scan_network
from core.hostdiscovery import network_id

def banner():
        print(f''' 
{Colors.red} {Colors.bold}
{Colors.silver}░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{Colors.silver}░░░{Colors.red}     ,-.              {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}    / \  `.  __..-,0  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}   :   \ --''_..-'.'  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}   |    . .-' `. '.   {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}   :     .     .`.'   {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}    \     `.  /  ..   {Colors.silver}░░░                                     
{Colors.silver}░░░{Colors.red}     \      `.   ' .  {Colors.silver}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{Colors.silver}░░░{Colors.red}      `,       `.   \ {Colors.end}                                              {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}     ,|,`.    {Colors.gray}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}    '.||,  ``-{Colors.gray}░{Colors.blue}███╗{Colors.gray}░░{Colors.blue}██╗███████╗████████╗███████╗███████╗██████╗{Colors.gray}░░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}     |--|     {Colors.gray}░{Colors.blue}████╗{Colors.gray}░{Colors.blue}██║██╔════╝╚══██╔══╝╚════██║██╔════╝██╔══██╗{Colors.gray}░  {Colors.silver}░░░               
{Colors.silver}░░░{Colors.red}     |--|     {Colors.gray}░{Colors.blue}██╔██╗██║█████╗{Colors.gray}░░░░░{Colors.blue}██║{Colors.gray}░░░░░{Colors.blue}███╔═╝█████╗{Colors.gray}░░{Colors.blue}██████╔╝{Colors.gray}░  {Colors.silver}░░░   
{Colors.silver}░░░{Colors.red}     /||\\     {Colors.gray}░{Colors.blue}██║╚████║██╔══╝{Colors.gray}░░░░░{Colors.blue}██║{Colors.gray}░░░{Colors.blue}██╔══╝{Colors.gray}░░{Colors.blue}██╔══╝{Colors.gray}░░{Colors.blue}██╔══██╗{Colors.gray}░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}    /░||░\\    {Colors.gray}░{Colors.blue}██║{Colors.gray}░{Colors.blue}╚███║███████╗{Colors.gray}░░░{Colors.blue}██║{Colors.gray}░░░{Colors.blue}███████╗███████╗██║{Colors.gray}░░{Colors.blue}██║{Colors.gray}░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}   /░░||░░\\   {Colors.gray}░{Colors.blue}╚═╝{Colors.gray}░░{Colors.blue}╚══╝╚══════╝{Colors.gray}░░░{Colors.blue}╚═╝{Colors.gray}░░░{Colors.blue}╚══════╝╚══════╝╚═╝{Colors.gray}░░{Colors.blue}╚═╝{Colors.gray}░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}__/░░░||░░░\\__{Colors.gray}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  {Colors.silver}░░░
{Colors.silver}░░░{Colors.red}              {Colors.end}      ver -ve[0.4]        dumb coded by LOKZY        {Colors.silver}░░░
{Colors.silver}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{Colors.end}
''')





if __name__ == "__main__":

    start_time = time.time()
    banner()
    print(f'[+] {Colors.bold}{Colors.green}ACTIVE INTERFACES:{Colors.end}')
    interface_with_internet = INFO.get_interface_name(INFO.get_private_ip())
    print(f'{INFO.get_network_interfaces()} \n')

    ans = str(input(f"Continue with {Colors.yellow} [-{interface_with_internet}-] {Colors.end}? [y/n]:") or interface_with_internet)
    if ans.lower() == 'y':
        print(f'[+] {Colors.bold}{Colors.green}INTERFACE:  {interface_with_internet} {Colors.end}')
    else:
        interface_with_internet = input(f"Enter the interface name to use (eg: wlan0): ").strip()
        if ans in INFO.get_network_interfaces():
            print(f'[+] {Colors.bold}{Colors.green}INTERFACE:  {interface_with_internet} {Colors.end}')
        else:
            print(f'{Colors.bold}{Colors.red}Invalid Interface!')

    # Specify the target IP address
    base_ip = INFO.get_address_by_interface(interface_with_internet)
    network_address = str(network_id(base_ip))

    # Try all IP addresses in the network
    network_address += '/24'

    print(scan_network(network_address))

    print(f'Total running Time: {round(time.time()-start_time,3)}sec')
