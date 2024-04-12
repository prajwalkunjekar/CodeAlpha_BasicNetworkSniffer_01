# Importing necessary functions and modules from Scapy
from scapy.all import sniff, IP

# Function to process each packet captured by the sniffer
def process_packet(packet):
    # Checking if the packet contains an IP layer
    if IP in packet:
        # Extracting source and destination IP addresses from the IP layer
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        # Printing the source and destination IP addresses
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

# Sniffing packets on the default interface
# prn parameter specifies the callback function to call for each packet
# store parameter is set to False to prevent storing packets in memory
sniff(prn=process_packet, store=False)
