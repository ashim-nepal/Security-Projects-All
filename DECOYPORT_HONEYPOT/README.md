# 🎯 DecoyPort-Honeypot

### An A Deception Engine with Real-Time Anomaly Detection

A web-based honeypot system that creates decoy services to lure attackers, detects anomalies, and provides AI-powered actionable suggestions for incident response(future development).

---

## Overview

DecoyPort-Honeypot is an advanced deception-based security tool that transforms the traditional honeypot concept into an intelligent, self-learning defense system. Unlike static honeypots that are easily fingerprinted, this platform dynamically creates decoy services, analyzes attacker behavior using, and generates context-aware suggestions. The simple web dashboard provides real-time visibility into attacks, anomalies, and recommended countermeasures.

---

## Features

- 🎭 **Dynamic Decoy Management** – Create and manage multiple decoy services (SSH, HTTP, SMB) through an intuitive web interface
- 🔍 **Real-Time Attack Detection** – Log all interactions with decoys including source IP, request data, and timestamps
- 📊 **Professional Dashboard** – Real-time threat scores, interactive charts, and live anomaly feeds with severity indicators
- 🔌 **Real Decoy Integration** – Deploy actual listening services that capture real attack traffic from tools like curl, nmap, and hydra
- 👍 **Feedback System** – Colour based threat categorization mechanism for easy tracking

---

## 📸 Preview

![Screenshot](./screenshots/console_output.png) 

---

## ⚠️ Disclaimer

- This tool is intended **strictly for educational purposes, authorized security testing, and authorized system monitoring**.  
- Only deploy on systems you own or have explicit written permission to test. 

---

## 📜 Learning Focus

- Building deception-based security systems (honeypots, decoy services)
- Developing full-stack web applications with Flask and Bootstrap
- Real-time data streaming with WebSockets
- Database design and ORM (SQLAlchemy)
- Background task scheduling and automation

---

## How It Works

1. **Decoy Creation** – User creates a decoy through the web interface (name, type, IP, port). The decoy is stored in the database and optionally deployed as a real service.

2. **Attack Detection** – When an attacker probes the decoy (via curl, nmap, etc.), all interactions are logged to the database with source IP, timestamp, and request data.

3. **Anomaly Detection** – The simple tracking algorithm trains on interaction features (time of day, source IP frequency, request length) and automatically flags suspicious activities as anomalies.

4. **Analyst Response** – Security analysts review suggestions in the dashboard, apply them with one click, and provide feedback to improve future predictions.

---

## Future Improvements


- **Advanced ML Models** – Implement Ai models for enhanced anomaly detection accuracy

- **More Decoy Types** – Expand support to FTP, SMTP, RDP, databases, and custom protocol decoys for broader coverage

- **Attack Visualization** – Generate network graphs showing attack paths, patterns, and lateral movement across decoys

- **Multi-User Support** – Implement role-based access control  for team collaboration and permission management

- **Export Reports** – Generate PDF/CSV incident summaries for compliance documentation and stakeholder reporting

