#!usr/bin/env/python
#tool author: krisna pranav

import scapy.all as scapy
import argparse              #imports
import time

#scan function
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast / arp_request
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#     client_list = []
#     for element in answered_list:
#         client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
#         client_list.append(client_dict)
#     return client_list

#result printing
def print_result(result_list):
    print("Scanning Your Network...")
    time.sleep(3)
    print("_" * 45)
    print("IP\t\t\tMAC Address")
    print("-" * 45)

    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


#add user parser
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", dest="target_ip", help="Target IP / Range IP")
options = parser.parse_args()
target = options.target_ip

print_result(scan(target))
