# Packet Sniffer using Scapy

This Python script is designed to capture and analyze network packets using the Scapy library. It provides a simple yet effective way to inspect network traffic and extract information such as source and destination IP addresses.

## Overview

Packet sniffing is a technique used in networking to intercept and log traffic passing over a digital network. This script leverages the Scapy library, a powerful packet manipulation tool, to capture packets on the default network interface.

## Features

- Captures network packets on the default interface.
- Extracts source and destination IP addresses from IP layer packets.
- Provides a callback function to process each captured packet.
- Does not store captured packets in memory to conserve resources.

## Usage

1. **Installation**: Ensure you have Python 3.x and the Scapy library installed on your system.

2. **Running the Script**: Execute the script using Python. It will start sniffing packets on the default network interface.

3. **Packet Processing**: For each packet captured, the script extracts the source and destination IP addresses from the IP layer and prints them to the console.

4. **Customization**: You can customize the script to suit your specific requirements. For example, you can modify the `process_packet` function to perform additional processing on the packets or apply filters based on specific criteria.

5. **Important Considerations**: 
   - **Permissions**: Running this script may require administrative privileges, depending on your operating system and network configuration. Ensure you have the necessary permissions before executing the script.
   - **Responsibility**: Packet sniffing tools can potentially intercept sensitive information. Always use them responsibly and in compliance with applicable laws and regulations.