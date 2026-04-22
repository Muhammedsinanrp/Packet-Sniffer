# Packet Sniffer (Python)

A basic network packet sniffer built using Python and Scapy to capture and analyze live network traffic.

## 🚀 Features
- Captures live network packets
- Displays source and destination IP addresses
- Identifies TCP and UDP traffic
- Real-time packet analysis

## 🛠️ Technologies Used
- Python
- Scapy

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/yourusername/packet-sniffer.git

2. Navigate into the folder:
   cd packet-sniffer

3. Install dependencies:
   pip install -r requirements.txt

## ▶️ Usage

Run the script:
python packet_sniffer.py

The tool will start capturing live packets. Press `Ctrl + C` to stop.

## ⚠️ Requirements
- Run with administrator/root privileges for packet capture
  - Linux/macOS: use `sudo`
  - Windows: run terminal as Administrator

## 📁 Project Structure

packet-sniffer/
│── packet_sniffer.py
│── README.md
│── requirements.txt

## ⚠️ Disclaimer
This tool is for educational purposes only. Do not use it to monitor networks without proper authorization.

## 📌 Future Improvements
- Add packet filtering (HTTP, DNS)
- Display packet payload data
- Save captured packets to a file (PCAP)
- Build a GUI for visualization
