# Brute Force Word Mutation & Matching Tool

A controlled, educational project focused on generating password variations and validating them against a dataset.

---

## Overview

This tool creates multiple variations of a given word by applying combinations of prefixes, suffixes, numbers, and symbols. The generated outputs are stored for analysis and testing purposes.

An extended version of the tool introduces a comparison mechanism that checks generated variants against entries from a CSV-based password dataset and records successful matches.

---

## Core Functionality

- Generates mutated wordlists using:
  - Prefixes and suffixes  
  - Numeric patterns  
  - Special characters
  - Characters combo(Vapital and small) and many more
- Stores all generated combinations in a text file  
- Supports dataset comparison mode:
  - Reads password entries from a CSV file  
  - Matches generated variants against the dataset  
  - Exports matched results to a separate CSV file  

---

## Output

- `wordlist.txt` — generated password variations (for version 1)
- `cracked_data.csv` — matched entries from dataset (for version 2)

---

## Preview
**Version 1**
![Screenshot](https://github.com/ashim-nepal/Security-Projects-All/blob/main/BRUTE_FORCE_PROJECTS/PROJECT_IMAGES/Screenshot%20at%202026-03-24%2013-09-46.png)

![Screenshot](https://github.com/ashim-nepal/Security-Projects-All/blob/main/BRUTE_FORCE_PROJECTS/PROJECT_IMAGES/Screenshot%20at%202026-03-24%2013-11-15.png)

**Version 2**
![Screenshot](https://github.com/ashim-nepal/Security-Projects-All/blob/main/BRUTE_FORCE_PROJECTS/PROJECT_IMAGES/Screenshot%20at%202026-03-24%2013-16-54.png)

![Screenshot](https://github.com/ashim-nepal/Security-Projects-All/blob/main/BRUTE_FORCE_PROJECTS/PROJECT_IMAGES/Screenshot%20at%202026-03-24%2013-17-59.png)

---

## Note

This project is not publicly distributed to prevent misuse. It is intended strictly for **learning, experimentation, and controlled environments**.

---

## Usage Context

Designed for:
- Understanding brute-force concepts  
- Testing password strength in isolated environments  
- Practicing data comparison techniques
