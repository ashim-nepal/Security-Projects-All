# DNS Blocker – Simple Firewall for Linux

An educational system administration tool that blocks unwanted domains by modifying `/etc/hosts` to redirect them to `0.0.0.0`. Includes a web‑based admin dashboard with authentication, database‑managed domain list, and activity logging. Designed for Linux to demonstrate basic firewall concepts.

---

## Overview

This project provides a simple but effective DNS‑level content blocker. Domains to be blocked are stored in a database and applied to the system’s hosts file. An admin panel allows adding/removing domains, toggling blocking status, and viewing logs. It serves as a learning tool for understanding how `/etc/hosts` works, how to implement a firewall at the DNS layer, and how to build a lightweight web administration interface.

---

## Features

- 🚫 **Block domains** – adds entries to `/etc/hosts` redirecting to `0.0.0.0`  
- 🔓 **Unblock domains** – removes entries from the hosts file  
- 🗄️ **Database storage** – stores domains, status (blocked/unblocked), timestamps  
- 🔐 **Admin authentication** – login required to access the dashboard  
- 📋 **Activity logging** – logs updates, applied domains, counts, and errors  
- ⏱️ **Periodic sync** – automatically applies changes at defined intervals  
- 🐧 **Linux‑friendly** – designed for Linux

---

## Preview

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/FIREWALL-DNS%20Blocker/PROJECT_DEMO/Screenshot%20at%202026-03-28%2018-46-14.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/FIREWALL-DNS%20Blocker/PROJECT_DEMO/Screenshot%20at%202026-03-28%2018-46-53.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/FIREWALL-DNS%20Blocker/PROJECT_DEMO/Screenshot%20at%202026-03-28%2019-04-45.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/FIREWALL-DNS%20Blocker/PROJECT_DEMO/Screenshot%20at%202026-03-28%2019-06-55.png)

![Screenshot](https://raw.githubusercontent.com/ashim-nepal/Security-Projects-All/refs/heads/main/FIREWALL-DNS%20Blocker/PROJECT_DEMO/Screenshot%20at%202026-03-28%2020-04-31.png)

---

## Disclaimer

- This tool is intended **strictly for educational and legitimate system administration** on systems you own or have explicit permission to manage.  
- Modifying `/etc/hosts` requires root privileges; use responsibly.  

---

## Learning Focus

- Understanding DNS resolution and the `/etc/hosts` file  
- Implementing a simple firewall at the system level  
- Building a web interface with authentication  
- Logging and monitoring system changes  
- Working with databases (PGSQL in Supabase) in Python

---

## How It Works

1. **Admin adds a domain** via the web dashboard.  
2. Domain is stored in the database with status = `blocked`.  
3. A background process (or cron job) periodically reads the database and writes all blocked domains to `/etc/hosts` as `0.0.0.0 domain.com`.  
4. The system DNS resolver sees the entry and blocks the domain.  
5. To unblock, the admin toggles on status to off → entry is removed from hosts file.  
6. All actions are logged with timestamps.
