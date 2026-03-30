# Cryptography Projects

A collection of educational cryptography projects demonstrating cryptography encryption for both text and files, along with a simple graphical interface for usability.

---

## Overview

This folder contains projects focused on practical implementations of symmetric encryption using AES and asymmetrical encryption. These projects highlight both fundamental concepts and applied use cases in a controlled environment.

---

## 1. Text Encrypter & Decrypter (AES)

A minimal tool for encrypting and decrypting plain text using AES (16-byte key).

### Features

- 🔑 AES-based text encryption  
- 🔄 Encrypt and decrypt functionality

### 🛠️ How It Works

1. Input plain text  
2. Encrypt using AES  
3. Output encrypted string  
4. Decrypt using the same key to retrieve original text  
5. Stores log about every events without erasing history

## Preview

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-39-01.png)
![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-39-49.png)

---

## 2. PDF Encrypter & Decrypter (AES + Tkinter)

A GUI-based utility to encrypt and decrypt PDF files using AES.

### Features

- 🔐 AES file encryption  
- 🖥️ Simple Tkinter interface  
- 📂 File selection dialog  
- 🔄 Encrypt and decrypt support  
- 💾 Custom `.secure` file format  

### 🛠️ How It Works

#### 🔒 Encryption
- Select a PDF file  
- Enter a password  
- Encrypt the file
- Saves as: `filename.pdf.secure`
- Stores log about every event without erasing history


#### 🔓 Decryption
- Select `.secure` file  
- Enter password  
- Decrypt the file
- Restores original PDF as `decrypted.pdf`

---

## Output

- Encrypted text (string output)  
- `*.secure` — encrypted PDF files  
- `decrypted.pdf` — restored files  

---

## Preview

![Screenshot](['./PROJECT_DEMO/Screenshot at 2026-03-24 15-41-52.png'](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-41-52.png))
![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-42-15.png)
![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-42-51.png)
![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-43-59.png)
![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/CRYPTOGRAPHY/PROJECT_DEMO/Screenshot%20at%202026-03-24%2015-44-13.png)

---

## Note

These projects are intended strictly for **educational and controlled use**.  
Improper use or loss of encryption keys/passwords may result in permanent data loss.

---

## Usage Context

- Understanding AES encryption  
- Practicing applied cryptography  
- Exploring file encryption with GUI integration
