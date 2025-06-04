#!/bin/Bash

# Challenge today is to create a script that list all the devices on the network and ask the user to ping one of the ip address.
# There is a few different ways to list all deivices on your network you could use an arp command or an nmap command.
# We will run the a command that prints all address then ask the user to ping a specific one by entering an ip address.

echo "Listing all network interfaces with their IP addresses:"
echo "--------------------------------------------------------"

# Use `ip` command to get info
while IFS= read -r line; do
    iface=$(echo "$line" | awk -F: '{print $2}' | xargs)
    echo "Interface: $iface"
    
    # Get IPv4 address
    ipv4=$(ip -4 addr show "$iface" | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    if [ -n "$ipv4" ]; then
        echo "  IPv4: $ipv4"
    else
        echo "  IPv4: None"
    fi

    # Get IPv6 address
    ipv6=$(ip -6 addr show "$iface" | grep -oP '(?<=inet6\s)[\da-f:]+')
    if [ -n "$ipv6" ]; then
        echo "  IPv6: $ipv6"
    else
        echo "  IPv6: None"
    fi

    echo
done < <(ip -o link show | awk -F': ' '{print $2}' | sort | uniq)