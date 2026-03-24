# HTTP REQUEST Load Testing Utility

A lightweight Python-based tool for sending controlled HTTP requests to a target endpoint for performance testing and analysis.

---

## Overview

This project is designed to simulate traffic against a specified URL in a **controlled and configurable manner**. It helps evaluate how an application responds under repeated requests while maintaining safe usage practices.

---

## Features

- 🌐 Configurable target URL  
- 🔢 Adjustable number of requests  
- ⏱️ Optional delay between requests  
- 📊 Basic response tracking (status / timing)  
- 🧪 Simple and lightweight implementation using Python  

---

## How It Works

1. Provide a target endpoint  
2. Define:
   - Total number of requests  
   - Delay between each request 
3. The tool sends requests sequentially or in a controlled loop  
4. Responses can be observed for behavior and stability  

---

## Configuration

Typical parameters:

- `url` → target endpoint  
- `requests` → number of requests to send  
- `delay` → time (in seconds) between each request  

---

## Preview

![Screenshot]("./Screenshot at 2026-03-24 17-24-11.png")

---

## Responsible Use

- This tool is intended strictly for **local testing and authorized environments**  
- The code is not available because of security reasons
- Excessive or uncontrolled usage may impact system stability  

---

## Usage Context

- Testing API responsiveness  
- Observing behavior under repeated requests  
- Learning basic performance testing concepts
