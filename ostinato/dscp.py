#! /usr/bin/env python

# This script was programmatically generated
# by Ostinato version 0.8 revision a7bfec8ecb93@
# The script should work out of the box mostly,
# but occassionally might need minor tweaking
# Please report any bugs at http://ostinato.org

# standard modules
import logging
import os
import sys
import time

# import ostinato modules
from ostinato.core import DroneProxy, ost_pb
from ostinato.protocols.udp_pb2 import Udp, udp
from ostinato.protocols.hexdump_pb2 import HexDump, hexDump
from ostinato.protocols.eth2_pb2 import Eth2, eth2
from ostinato.protocols.ip4_pb2 import Ip4, ip4
from ostinato.protocols.mac_pb2 import Mac, mac

# initialize the below variables appropriately to avoid manual input
host_name = '9.0.49.183'
tx_port_number = 3

# setup logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# get inputs, if required
while len(host_name) == 0:
    host_name = raw_input('Drone\'s Hostname/IP: ')
while tx_port_number < 0:
    tx_port_number = int(raw_input('Tx Port Number: '))

drone = DroneProxy(host_name)

try:
    # connect to drone
    log.info('connecting to drone(%s:%d)' 
            % (drone.hostName(), drone.portNumber()))
    drone.connect()

    # setup tx port list
    tx_port = ost_pb.PortIdList()
    tx_port.port_id.add().id = tx_port_number;

    # ------------#
    # add streams #
    # ------------#
    stream_id = ost_pb.StreamIdList()
    stream_id.port_id.id = tx_port_number
    stream_id.stream_id.add().id = 24
    stream_id.stream_id.add().id = 29
    stream_id.stream_id.add().id = 30
    stream_id.stream_id.add().id = 31
    drone.addStream(stream_id)

    # ------------------#
    # configure streams #
    # ------------------#
    stream_cfg = ost_pb.StreamConfigList()
    stream_cfg.port_id.id = tx_port_number

    # stream 24 DSCP 46
    s = stream_cfg.stream.add()
    s.stream_id.id = 24
    s.core.name = 'DSCP 46'
    s.core.is_enabled = True
    s.control.num_packets = 0xA
    s.control.packets_per_sec = 10

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kMacFieldNumber
    p.Extensions[mac].dst_mac = 0x90003
    p.Extensions[mac].src_mac = 0x90001

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kEth2FieldNumber
    p.Extensions[eth2].type = 0x800
    p.Extensions[eth2].is_override_type = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kIp4FieldNumber
    p.Extensions[ip4].is_override_ver = True
    p.Extensions[ip4].is_override_hdrlen = True
    p.Extensions[ip4].is_override_totlen = True
    p.Extensions[ip4].is_override_cksum = True
    p.Extensions[ip4].tos = 0x46
    p.Extensions[ip4].totlen = 46
    p.Extensions[ip4].proto = 0x11
    p.Extensions[ip4].cksum = 0x26da
    p.Extensions[ip4].src_ip = 0x93d0133
    p.Extensions[ip4].dst_ip = 0x93d0135
    p.Extensions[ip4].is_override_proto = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kUdpFieldNumber
    p.Extensions[udp].is_override_src_port = True
    p.Extensions[udp].is_override_dst_port = True
    p.Extensions[udp].is_override_totlen = True
    p.Extensions[udp].is_override_cksum = True
    p.Extensions[udp].src_port = 0x35
    p.Extensions[udp].dst_port = 0x35
    p.Extensions[udp].totlen = 26
    p.Extensions[udp].cksum = 0xefa6

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
    p.Extensions[hexDump].content = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    p.Extensions[hexDump].pad_until_end = False

    # stream 29 DSCP 26
    s = stream_cfg.stream.add()
    s.stream_id.id = 29
    s.core.name = 'DSCP 26'
    s.core.is_enabled = True
    s.core.ordinal = 0x1
    s.control.num_packets = 0xA
    s.control.packets_per_sec = 10

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kMacFieldNumber
    p.Extensions[mac].dst_mac = 0x90003
    p.Extensions[mac].src_mac = 0x90001

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kEth2FieldNumber
    p.Extensions[eth2].type = 0x800
    p.Extensions[eth2].is_override_type = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kIp4FieldNumber
    p.Extensions[ip4].is_override_ver = True
    p.Extensions[ip4].is_override_hdrlen = True
    p.Extensions[ip4].is_override_totlen = True
    p.Extensions[ip4].is_override_cksum = True
    p.Extensions[ip4].tos = 0x26
    p.Extensions[ip4].totlen = 46
    p.Extensions[ip4].proto = 0x11
    p.Extensions[ip4].cksum = 0x26da
    p.Extensions[ip4].src_ip = 0x93d0133
    p.Extensions[ip4].dst_ip = 0x93d0135
    p.Extensions[ip4].is_override_proto = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kUdpFieldNumber
    p.Extensions[udp].is_override_src_port = True
    p.Extensions[udp].is_override_dst_port = True
    p.Extensions[udp].is_override_totlen = True
    p.Extensions[udp].is_override_cksum = True
    p.Extensions[udp].src_port = 0x35
    p.Extensions[udp].dst_port = 0x35
    p.Extensions[udp].totlen = 26
    p.Extensions[udp].cksum = 0xefa6

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
    p.Extensions[hexDump].content = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    p.Extensions[hexDump].pad_until_end = False

    # stream 30 DSCP 18
    s = stream_cfg.stream.add()
    s.stream_id.id = 30
    s.core.name = 'DSCP 18'
    s.core.is_enabled = True
    s.core.ordinal = 0x2
    s.control.num_packets = 0xA
    s.control.packets_per_sec = 10

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kMacFieldNumber
    p.Extensions[mac].dst_mac = 0x90003
    p.Extensions[mac].src_mac = 0x90001

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kEth2FieldNumber
    p.Extensions[eth2].type = 0x800
    p.Extensions[eth2].is_override_type = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kIp4FieldNumber
    p.Extensions[ip4].is_override_ver = True
    p.Extensions[ip4].is_override_hdrlen = True
    p.Extensions[ip4].is_override_totlen = True
    p.Extensions[ip4].is_override_cksum = True
    p.Extensions[ip4].tos = 0x18
    p.Extensions[ip4].totlen = 46
    p.Extensions[ip4].proto = 0x11
    p.Extensions[ip4].cksum = 0x26da
    p.Extensions[ip4].src_ip = 0x93d0133
    p.Extensions[ip4].dst_ip = 0x93d0135
    p.Extensions[ip4].is_override_proto = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kUdpFieldNumber
    p.Extensions[udp].is_override_src_port = True
    p.Extensions[udp].is_override_dst_port = True
    p.Extensions[udp].is_override_totlen = True
    p.Extensions[udp].is_override_cksum = True
    p.Extensions[udp].src_port = 0x35
    p.Extensions[udp].dst_port = 0x35
    p.Extensions[udp].totlen = 26
    p.Extensions[udp].cksum = 0xefa6

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
    p.Extensions[hexDump].content = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    p.Extensions[hexDump].pad_until_end = False

    # stream 31 DSCP 0
    s = stream_cfg.stream.add()
    s.stream_id.id = 31
    s.core.name = 'DSCP 0'
    s.core.is_enabled = True
    s.core.ordinal = 0x3
    s.control.num_packets = 0xA
    s.control.packets_per_sec = 10

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kMacFieldNumber
    p.Extensions[mac].dst_mac = 0x90003
    p.Extensions[mac].src_mac = 0x90001

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kEth2FieldNumber
    p.Extensions[eth2].type = 0x800
    p.Extensions[eth2].is_override_type = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kIp4FieldNumber
    p.Extensions[ip4].is_override_ver = True
    p.Extensions[ip4].is_override_hdrlen = True
    p.Extensions[ip4].is_override_totlen = True
    p.Extensions[ip4].is_override_cksum = True
    p.Extensions[ip4].totlen = 46
    p.Extensions[ip4].proto = 0x11
    p.Extensions[ip4].cksum = 0x26da
    p.Extensions[ip4].src_ip = 0x93d0133
    p.Extensions[ip4].dst_ip = 0x93d0135
    p.Extensions[ip4].is_override_proto = True

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kUdpFieldNumber
    p.Extensions[udp].is_override_src_port = True
    p.Extensions[udp].is_override_dst_port = True
    p.Extensions[udp].is_override_totlen = True
    p.Extensions[udp].is_override_cksum = True
    p.Extensions[udp].src_port = 0x35
    p.Extensions[udp].dst_port = 0x35
    p.Extensions[udp].totlen = 26
    p.Extensions[udp].cksum = 0xefa6

    p = s.protocol.add()
    p.protocol_id.id = ost_pb.Protocol.kHexDumpFieldNumber
    p.Extensions[hexDump].content = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    p.Extensions[hexDump].pad_until_end = False

    drone.modifyStream(stream_cfg)
    # clear tx/rx stats
    log.info('clearing tx stats')
    drone.clearStats(tx_port)

    log.info('starting transmit')
    drone.startTransmit(tx_port)

    # wait for transmit to finish
    log.info('waiting for transmit to finish ...')
    while True:
        try:
            time.sleep(5)
            tx_stats = drone.getStats(tx_port)
            if tx_stats.port_stats[0].state.is_transmit_on == False:
                break
        except KeyboardInterrupt:
            log.info('transmit interrupted by user')
            break

    # stop transmit and capture
    log.info('stopping transmit')
    drone.stopTransmit(tx_port)

    # get tx stats
    log.info('retreiving stats')
    tx_stats = drone.getStats(tx_port)

    log.info('tx pkts = %d' % (tx_stats.port_stats[0].tx_pkts))

    # delete streams
    log.info('deleting tx_streams')
    drone.deleteStream(stream_id)

    # bye for now
    drone.disconnect()

except Exception as ex:
    log.exception(ex)
    sys.exit(1)
