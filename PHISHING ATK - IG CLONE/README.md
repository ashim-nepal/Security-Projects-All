# Instagram Login Clone

An educational cybersecurity project that replicates the Instagram login interface to demonstrate how phishing attacks work and how users can be tricked into revealing credentials. Built with React for the frontend and a MySQL database for credential storage. **Strictly for learning and awareness purposes.**

---

## Overview

This project is a realistic clone of the Instagram login page (late 2025) designed to simulate a phishing attack in a controlled environment. It showcases how easily attackers can mimic legitimate login pages to harvest credentials. The frontend uses React for a responsive, authentic UI, while the backend stores submitted usernames and passwords in a MySQL database for analysis. The goal is to educate developers, security enthusiasts, and end‑users about the dangers of phishing and the importance of verifying website authenticity.

---

## Features

- 🎨 **Realistic Instagram login UI** – mimicking the Late-2025 design  
- ⚛️ **React frontend** – fast, component‑based interface  
- 🗄️ **MySQL database** – stores captured credentials (for demonstration only)  
- 📱 **Responsive design** – works on desktop and mobile views  
- 🧪 **Educational tool** – to study phishing techniques and countermeasures  

---

## Preview

![Login Page]("./PROJECT_SHOWCASE/Screenshot at 2026-03-28 12-26-40.png")

![Credential Capture]("./PROJECT_SHOWCASE/Screenshot at 2026-03-28 12-40-30.png") 

![Database Stored]("./PROJECT_SHOWCASE/Screenshot at 2026-03-28 12-29-37.png")

---

## Disclaimer

- This project is created **strictly for educational and ethical security research**.  
- It demonstrates how phishing attacks operate to raise **awareness and promote safer online practices**.  
- **Do not use this tool to capture real credentials or to target any real users.** Use only in a controlled, local environment with explicit consent.  
- The author assumes no responsibility for any misuse.

---

## Learning Focus

- Understanding phishing attack mechanisms and user interface cloning  
- Building a realistic login form with React  
- Setting up a MySQL database to log submissions  
- Importance of security awareness and anti‑phishing measures (e.g., HTTPS, two‑factor authentication, browser warnings)

---
---

## How It Works

1. A user visits the fake Instagram login page.  
2. They enter their username and password, believing it to be the real Instagram.  
3. On submission, the credentials are sent to a backend API.  
4. The backend stores the username and password in a MySQL table (for demonstration purposes).  
5. The user is then redirected to the real Instagram or shown a generic error (depending on the simulation).  
6. **Educational note:** This mimics a real phishing attack, highlighting the need for vigilance.

---

## Future Improvements

- Add HTTPS support to simulate secure connections  
- Implement a more sophisticated redirect to the real Instagram after capture  
- Add logging of IP addresses and timestamps for analysis  
- Build an admin dashboard to view captured data (only for educational and research use only)

---

## Author

- Developed as a learning project in cybersecurity and frontend development  
- Inspired by real‑world phishing threats and the need for awareness
