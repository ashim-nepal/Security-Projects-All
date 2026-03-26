# VulnScanner Pro

An educational cybersecurity tool that scans a target website for common vulnerabilities and misconfigurations, generating a detailed report. Built with Flask for demonstration purposes.

---

## Overview

This project provides a lightweight, user‑friendly web interface to perform security audits on any domain. It checks for issues like missing HTTPS, insecure headers, XSS, SQL injection, CSRF, and more. The scan results are presented in a clean, color‑coded table with status indicators. Designed for studying security assessment techniques in a controlled environment.

---

## Features

- 🌐 **Scans any domain** (via URL input)  
- 🔍 **22+ security checks** including:  
  - HTTPS enforcement  
  - Security headers (HSTS, CSP, X‑Frame‑Options, etc.)  
  - Common web vulnerabilities (XSS, SQLi, CSRF, open redirect)  
  - Server information leakage  
  - DNS records, SSL certificate validation  
  - Rate limiting, CORS, and cookie security  
- 📊 **Nice, readable report** with status icons (✔ Safe, ⚠ Vulnerable/Warning, ℹ Info)  
- 🔁 **One‑click new scan** option  
- 🖥️ **Flask‑based web interface** – simple to deploy and use locally  

---

## 📸 Preview

![Screenshot]("./PROJECT_DEMO/Screenshot at 2026-03-26 12-54-53.png")

![Screenshot]("./PROJECT_DEMO/Screenshot at 2026-03-26 12-55-51.png")

![Screenshot]("./PROJECT_DEMO/Screenshot at 2026-03-26 12-56-05.png")

![Screenshot]("./PROJECT_DEMO/Screenshot at 2026-03-26 12-56-29.png")

---

## ⚠️ Disclaimer

- This tool is intended **strictly for educational and ethical security testing** on systems you own or have explicit permission to test. 

---

## 📜 Learning Focus

- Understanding common web vulnerabilities and how to detect them  
- Building a modular vulnerability scanner  
- Presenting security data in a user‑friendly format  
- Developing with Flask for rapid prototyping
