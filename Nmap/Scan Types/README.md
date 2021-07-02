# Nmap - Scan Types

## TCP Connect Scans

`RFC 793` defines the behaviour for the TCP protocol. If a port is closed the `RST` or Reset flag is sent back.

## SYN Scans

SYN Scans are also known as `Half-Open` or `Stealth` scans due to the way they work. When running them you require sudo permissions as they require the ability to create raw packets.

## UDP Scans

If a UDP port does not respond to a UDP scan it will be marked as `open|filtered`. If a port is closed, the target should send back a "port unrechable message" over the `ICMP` protocol.

## NULL, FIN and Xmas Scans

The `Xmas` scan uses the URG flag. In general these scan types would be used over regular TCP scans because of `firewall evasion`. `Microsoft Windows` generally responds to these scans with RST for every port.

## ICMP Network Scanning

To perform a ping sweep on the `172.16.x.x` network with netmask of `255.255.0.0` you can do `nmap -sn 172.16.0.0./16`.