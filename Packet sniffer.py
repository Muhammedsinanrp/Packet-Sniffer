from scapy.all import sniff

def process_packet(packet):
    try:
        if packet.haslayer("IP"):
            src = packet["IP"].src
            dst = packet["IP"].dst
            print(f"[IP] {src} -> {dst}")

        if packet.haslayer("TCP"):
            print("   [TCP Packet]")

        elif packet.haslayer("UDP"):
            print("   [UDP Packet]")

    except Exception as e:
        pass

print("Starting packet capture... (Press Ctrl+C to stop)\n")

sniff(prn=process_packet, store=False)