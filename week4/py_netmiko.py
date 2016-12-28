from netmiko import ConnectHandler

gtac_usern = 'rwuser'
gtac_passw = 'Password2'

acs_usern  = 'bl839s'
acs_passw  = 's5372g3ATa!!'

dev1 = {
    'device_type': 'cisco_ios',
    'ip': '9.88.128.5',
    'username': gtac_usern,
    'password': gtac_passw,
}

dev2 = {
    'device_type': 'cisco_ios',
    'ip': '9.88.128.6',
    'username': gtac_usern,
    'password': gtac_passw,
    'secret': gtac_passw,
    'port': '22',
}

dev3 = {
    'device_type': 'juniper',
    'ip': '9.88.254.5',
    'username': acs_usern,
    'password': acs_passw,
}

dev4 = {
    'device_type': 'juniper',
    'ip': '9.88.254.6',
    'username': acs_usern,
    'password': acs_passw,
}

rch_vsc_a = ConnectHandler(**dev1)
rch_vsc_b = ConnectHandler(**dev2)

hpr_ecd_a = ConnectHandler(**dev3)
hpr_ecd_b = ConnectHandler(**dev4)

## Cisco Examples ##

# Demonstrating changing config
rch_vsc_b.enable()
rch_vsc_b.send_command("sh run | i logging buff")
config = ['logging buff 99999 info']
rch_vsc_b.send_config_set(config)
rch_vsc_b.send_command("sh run | i logging buff")

# Changing config back to default
rch_vsc_b.send_command("sh run | i logging buff")
config = ['logging buff 1024000 info']
rch_vsc_b.send_config_set(config)
rch_vsc_b.send_command("sh run | i logging buff")

## Juniper Examples ##

hpr_ecd_b.send_command("show interfaces terse | match irb")
config = ['set system arp aging-timer 6']
hpr_ecd_b.send_config_set(config)
hpr_ecd_b.commit()
config = ['rollback 1']
hpr_ecd_b.send_config_set(config)
hpr_ecd_b.commit()

