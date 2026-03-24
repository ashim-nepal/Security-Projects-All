# Advanced Password Checker & Secure Vault

A compact security-focused project that analyzes password strength and securely stores encrypted data in a layered, obfuscated folder structure.

---

## Overview

This tool combines password analysis with encrypted storage. It evaluates input passwords through a simple Tkinter interface and generates detailed statistics, while also securely storing encrypted payloads for controlled recovery.

---

## Features

- 🔎 Password analysis:
  - Total characters  
  - Uppercase & lowercase letters  
  - Digits  
  - Special characters  
  - Spaces  

- 🖥️ Simple Tkinter-based interface  
- 🔐 AES encryption  
- 💾 Structured payload storage (`payload.json`)  
- 🗂️ Multi-layered folder obfuscation (vault system with decoy paths)  

---

## How It Works

1. Enter a password in the interface  
2. Click **Check Strength**  
3. The tool:
   - Displays detailed character breakdown  
   - Encrypts relevant data using AES  
   - Stores a structured payload for recovery  

---

## Secure Storage Design

- Data is saved inside a `vault/` directory  
- Multiple nested folders are generated:
  - Each level contains multiple directories  
  - Only one path leads to actual data  
  - Others act as decoy folders  
- Current depth: **3 layers** (configurable in code)

---

## Preview

![Screenshot]('./PROJECT_DEMO/Screenshot at 2026-03-24 15-59-34.png')
![Screenshot]('./PROJECT_DEMO/Screenshot at 2026-03-24 16-00-26+.png')
![Screenshot]('./PROJECT_DEMO/Screenshot at 2026-03-24 16-00-49.png')
![Screenshot]('./PROJECT_DEMO/Screenshot at 2026-03-24 16-01-23.png')

---

## 📄 Payload Structure

Example `payload.json`:

```json
{
  "encryption_type": "AES",
  "mode": "CBC",
  "key_size_bits": 256,
  "padding": "PKCS7",
  "cipher_text": "...",
  "iv": "...",
  "key_hint": "...",
  "note": "Decrypt using AES-256-CBC with stored IV and key"
}
