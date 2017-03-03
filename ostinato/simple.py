#!/usr/bin/python

from simple_ostinato import Drone
from simple_ostinato.protocols import Mac, Ethernet, IPv4, Payload

# connect to the drone instance that runs on localhost
drone = Drone('9.0.49.183')

# fetch port information
drone.fetch_ports()

# store the two ports we are going to use in dedicated variables
#port_tx = drone.get_port_by_name('veth0')[0]
#port_rx = drone.get_port_by_name('veth1')[0]

port_tx = 0
port_rx = 0


# Create a new stream
stream = port_tx.add_stream(
    Mac(source='00:11:22:aa:bb:cc', destination='00:01:02:03:04:05'),
    Ethernet(),
    IPv4(source='10.0.0.1', destination='10.0.0.2'),
    Payload())

# Configure the stream
stream.name = 'simple_mac_stream'
stream.packets_per_sec = 1000
stream.num_packets = 100
stream.enable()
stream.save()

# Clear the stats on the transmitting and receiving port
port_tx.clear_stats()
port_rx.clear_stats()

# Send and capture
port_rx.start_capture()
port_tx.start_send()
time.sleep(1)
port_tx.stop_send()
port_rx.stop_capture()

# Get the stats and print them
tx_stats = port_tx.get_stats()
rx_stats = port_rx.get_stats()
print str(tx_stats)
print str(rx_stats)

# We can also store the capture:
capture = port_rx.save_capture(port_rx.get_capture(), 'capture.pcap')
