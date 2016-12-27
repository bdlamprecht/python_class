#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract

RO_STRING = 'apic_readonly'
SNMP_PORT = 161
IP1 = '9.88.0.5'
IP2 = '9.88.0.6'

dev1 = (IP1, RO_STRING, SNMP_PORT)
dev2 = (IP2, RO_STRING, SNMP_PORT)

OID1 = '1.3.6.1.2.1.1.5.0'
OID2 = '1.3.6.1.2.1.1.1.0'
OID3 = '1.3.6.1.2.1.1.6.0'

def get_details(devx):
	print "---"
	print snmp_extract(snmp_get_oid(devx, oid=OID1))
	print "\n"
	print snmp_extract(snmp_get_oid(devx, oid=OID2))
	print "\n"
	print snmp_extract(snmp_get_oid(devx, oid=OID3))
	print "---"

get_details(dev1)
get_details(dev2)
