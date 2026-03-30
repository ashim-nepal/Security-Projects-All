# Log Analyzer + Intrusion Detection System

A terminal‑based tool that analyzes authentication logs (e.g., `/var/log/auth.log`) to detect potential intrusion attempts. It extracts failed logins, suspicious IPs, and generates reports in multiple formats, with optional visualizations and continuous monitoring.

---

## Overview

This project provides a lightweight yet powerful log analysis framework for Linux systems. It parses authentication logs to identify brute‑force attacks, unusual login patterns, and other indicators of compromise. Designed for system administrators and security enthusiasts, it demonstrates how to extract actionable intelligence from log files using Python.

---

## Features

- 📄 **Parses authentication logs** (supports standard `/var/log/auth.log`)  
- 🔍 **Detects failed login attempts** and suspicious IPs  
- 📊 **Multiple output formats** – console (human‑readable), JSON, or file export
- ⏱️ **Continuous monitoring mode** – runs at configurable intervals  
- ⚙️ **Customizable configuration** via external file  
- 🚀 **Easy to integrate** with other security tools via JSON output  

---

## 📸 Preview

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/LOG_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-28%2021-46-53.png)  

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/LOG_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-28%2021-47-37.png)  

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/LOG_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-28%2021-48-17.png)  

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/LOG_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-28%2021-49-21.png)  

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/LOG_ANALYZER/PROJECT_DEMO/Screenshot%20at%202026-03-28%2021-50-01.png)  

---

## Disclaimer

- This tool is intended **strictly for educational and authorized system monitoring**.  
- Always ensure you have permission to access and analyze logs on any system.

---

## Learning Focus

- Understanding Linux authentication logs and their structure  
- Implementing log parsing and pattern matching  
- Building a modular CLI tool with Python’s `argparse`
- Continuous monitoring and scheduling  

---
---

## How It Works

1. **Read log file** – the script parses the specified log file line by line.  
2. **Extract events** – identifies failed login attempts, user names, IP addresses, and timestamps using regex patterns.  
3. **Aggregate data** – counts attempts per IP, user, etc.  
4. **Detect anomalies** – flags IPs with excessive failures (configurable threshold).  
5. **Output results** – prints to console, exports to JSON, or saves to a file. 
7. **Continuous mode** – runs in a loop, re‑scanning the log at intervals, and optionally appends results.

---

## Future Improvements

- Add support for other log formats (e.g., Apache, nginx)  
- Implement real‑time log tailing (`tail -f`)  
- Integrate with external threat intelligence feeds (e.g., abuseipdb.com)  
- Provide a web dashboard for historical data  
- Add alerting (email, webhook) on detected intrusions
