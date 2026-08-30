# Linux Fundamentals Part 1 — Hands-on Learning Log

## Overview
- **Date:** August 30, 2026
- **Source:** TryHackMe (Free Tier)
- **Environment:** Local Ubuntu Virtual Machine (No sandbox browser used)
- **Objective:** Develop foundational efficiency with the Linux command line and system navigation.

---

## Key Commands Practiced & Defined

### 1. File & Directory Navigation
*   `pwd` (Print Working Directory): Outputs the absolute path of the directory currently being accessed, allowing for precise orientation within the filesystem hierarchy.
*   `ls -la`: Lists all files and directories within the current working folder. 
    *   The `-l` flag triggers the long-list format, exposing detailed metadata such as file sizes, modification dates, and ownership permissions.
    *   The `-a` flag ensures all files are visible, including hidden system configuration files that begin with a period.
*   `cd [directory]`: Changes the current working directory to allow seamless movement throughout the folder structure.

### 2. Data Handling & Text Manipulation
*   `cat [file]`: Concatenates and displays the raw text content of a file directly onto the terminal output screen.
*   `grep [pattern] [file]`: Searches for specific text strings or structural patterns within a file. This is a critical tool for parsing log files and filtering massive datasets.

### 3. I/O Redirection
*   `>` (Overwrite Operator): Redirects the output of a command into a specified file, completely erasing and replacing any previous data within that file.
*   `>>` (Append Operator): Redirects the output of a command into a specified file, cleanly appending the text to the bottom of the file without altering existing data.

---

## System Exploration Log (15-Minute Phase)

Following the standard laboratory tasks, a 15-minute system evaluation was conducted using passive snapshot and active real-time system monitoring tools to understand baseline Linux behavior.

### `top` (Interactive Process Monitor)
- **Observation / Discovery:** Serves as a real-time command-line task manager. It provides fluid, continuous updates on CPU utilization, memory allocations, uptime statistics, and active process execution priority. Entering `q` cleanly terminates the interactive session.

### `ps aux` (Static Process Snapshot)
- **Observation / Discovery:** Generates a static baseline snapshot capturing every single program running at that exact millisecond. It catalogs running tasks by their executing USER, unique Process ID (PID), CPU/Memory percentage, and the absolute command path.

### `ls -la /var/log` (System Log Auditing)
- **Observation / Discovery:** Audited the storage directory where Linux aggregates its core system logs. Observed multiple `.log` files containing administrative metrics, authentication attempts, and boot sequences. The permission strings on the far left explicitly define which system roles are permitted to read or modify these files.

---

## Professional Reflections & Debugging Insights

### Confused Me / Lessons Learned:
*   **Search and Filter Command Logic:** While basic terminal syntax and I/O redirection are clear, the logical distinction and overlapping use cases between finding files on the system and utilizing `grep` to filter internal text patterns require further practice to master efficiently.

---
*Next Objective: Escalating technical capabilities in Linux Fundamentals Part 2.*
