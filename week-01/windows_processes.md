# Windows Internal Architecture and Core Process Analysis — Learning Log

## Overview
- **Date:** September 7, 2026
- **Environment:** Host Windows Operating System (Task Manager Details Interface)
- **Objective:** Analyze critical, persistent Windows core processes to establish an architectural baseline for security monitoring and anomaly detection.

---

## Analyzed Windows Core Processes

### 1. Service Host (`svchost.exe`)
*   **What it does:** This is a helper process that acts like a container for smaller background jobs.
*   **Why there are many copies:** Windows has dozens of little tasks to do (like running Wi-Fi, sync tools, or playing sounds). Instead of making a standalone program for each one, Windows groups them together inside multiple `svchost.exe` files to keep the computer running smoothly.
*   **What I saw in Task Manager:** Multiple rows running under system accounts like `SYSTEM` or `LOCAL SERVICE`.

### 2. Windows Explorer (`explorer.exe`)
*   **What it does:** This process creates the actual visual desktop environment that I interact with.
*   **Why it matters:** It is responsible for drawing my taskbar, the start menu, my desktop wallpaper, and any file folders I open. If this process crashes or stops, my entire screen goes black except for open apps.
*   **What I saw in Task Manager:** It runs specifically under my personal Windows username because it belongs to my current user session.

### 3. Local Security Authority Subsystem Service (`lsass.exe`)
*   **What it does:** This is the core security guard of the Windows operating system.
*   **Why it matters for security:** It verifies my password when I log into my laptop and manages system permissions. Because it temporarily keeps login data in the computer's memory, hackers often target it to steal credentials.
*   **What I saw in Task Manager:** There is only one single copy of it running, and its username is strictly listed as `SYSTEM`. If I ever see a second one, or if it runs under a normal user name, it is a sign of malware.

---
*Next Objective: Review week one milestones and compile the comprehensive technical portfolio report.*
