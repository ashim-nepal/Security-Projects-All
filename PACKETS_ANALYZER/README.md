# 🛡️ NetGuard Pro - Network Attack Detection System

A PCAP-based network security analyzer that detects common attack patterns and generates professional reports. Built with Python, Tkinter, and Scapy for educational and cybersecurity purposes.

---

## 📌 Overview

NetGuard Pro analyzes captured network traffic (PCAP files) to identify potential threats, including:

- SYN Floods  
- Port Scans  
- ARP Spoofing  
- DNS Tunneling  
- Brute Force Attempts  

It provides detailed, real-time results in a user-friendly GUI and produces structured reports for further analysis.

---

## ⚙️ Features

- 🖥️ **Graphical Interface** with Tkinter  
- 📂 **PCAP File Analysis**  
- 🔍 **Threat Detection**:
  - High, Medium, and Informational severity levels  
- 💾 **Professional Report Generation** (TXT) with:
  - Scan summary  
  - Detected threats  
  - Security recommendations  
- 🗑️ Clear results functionality for repeated use  

---

## 🛠️ How It Works

1. Load a PCAP file through the GUI.  
2. Click **Start Analysis** to process the network traffic.  
3. Threats are detected based on packet inspection (SYN counts, TCP payloads, DNS queries, ARP tables, etc.).  
4. Results are displayed in a table with attack type, details, and severity.  
5. Optionally, save a professional report with detailed statistics and recommendations.  

---

## 📂 Output

Reports are saved in the `reports/` folder and include:

- Scan ID and timestamp  
- Total packets analyzed  
- Threat summary and risk score  
- Detailed list of detected attacks  
- Security recommendations  

---

## 📸 Preview

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/PACKETS_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-24%2018-26-39.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/PACKETS_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-24%2018-27-04.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/PACKETS_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-24%2018-29-45.png)

---

## ⚠️ Disclaimer

- This project is intended **for educational and controlled security research only**.   
- All analysis is local and based on user-provided PCAP files.

---

## 📜 Learning Objectives

- Understanding network traffic analysis  
- Identifying common network attacks  
- Practicing cybersecurity reporting and threat visualization
